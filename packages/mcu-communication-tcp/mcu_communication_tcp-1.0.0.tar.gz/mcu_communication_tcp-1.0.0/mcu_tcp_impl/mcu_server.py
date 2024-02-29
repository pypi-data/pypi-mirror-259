from twisted.internet import reactor, protocol, defer
from twisted.internet.threads import deferToThread
import logging
import queue
import time
from mcu_functions.functions import create_ping_request, create_query_serial_number_request
from mcu_protocol import request, response, serial_number  # Assuming you have your mcu_protocol definitions
from mcu_functions.utils import get_binary_with_length_prefix,receive_bit_array_with_length_prefix


class EventDispatcher:
    def __init__(self):
        self.listeners = {}

    def on(self, event, callback):
        self.listeners.setdefault(event, []).append(callback)

    def emit(self, event, *args):
        for callback in self.listeners.get(event, []):
            callback(*args)

class MCUProtocol(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.serial_number = None
        self.ready = False
        self.ping_ready = False
        self.buffer = b''  # Initialize an empty buffer
        self.byte_length_for_data_length = 4
        self.MAX_BUFFER_SIZE=1024

    def connectionMade(self):
        self.ping_client()

    def connectionLost(self, reason):
        # Called when the connection is closed
        if self.serial_number:
            logging.info(f"Client with serial number '{self.serial_number}' disconnected. Reason: {reason}")
            self.factory.dispatcher.emit('connection_lost', self.serial_number)
            # Optionally remove from the factory's protocols dictionary
            if self.serial_number in self.factory.protocols:
                del self.factory.protocols[self.serial_number]

    def ping_client(self):
        request_id = self.factory.generate_request_id()
        ping_request = create_ping_request(request_id)
        prefixed_length_ping_request = get_binary_with_length_prefix(ping_request)
        self.transport.write(prefixed_length_ping_request)
        self.factory.set_timeout(request_id, self.ping_timeout)

    def ping_timeout(self,reqest_id):
        # Handle ping timeout if needed
        logging.warning(f"Ping request timed out for request id {reqest_id}")
        self.transport.loseConnection()

    def query_serial_number(self):
        request_id = self.factory.generate_request_id()
        query_request = create_query_serial_number_request(request_id)
        prefixed_length_query_request = get_binary_with_length_prefix(query_request)
        self.transport.write(prefixed_length_query_request)
        self.factory.set_timeout(request_id, self.serial_number_timeout)

    def serial_number_timeout(self,reqest_id):
        # Handle serial number query timeout if needed
        logging.warning(f"Serial number query timed out for request id {reqest_id}")
        self.transport.loseConnection()

    def dataReceived(self, data):
        self.buffer += data  # Append new data to the buffer
        #logging.info(f"Received data: at {time.time()*1000:.0f} ms {len(data)} bytes")
        req_id = None
        while self.buffer:
            try:
                response_binary = receive_bit_array_with_length_prefix(self.buffer,self.byte_length_for_data_length)

                responseObj = response.response.GetRootAs(response_binary, 0)
                req_id = responseObj.RequestId()
                self.factory.handle_response(responseObj, self)
                self.buffer = self.buffer[len(response_binary)+4:]

            except Exception as e:
                # Partial data or parsing error
                if len(self.buffer) > self.MAX_BUFFER_SIZE:  # Prevent buffer overflow
                    logging.error("Buffer overflow. Clearing buffer.")
                    self.buffer = b''
                break  # Exit the loop and wait for more data


class MCUFactory(protocol.Factory):
    def __init__(self):
        self.dispatcher = EventDispatcher()
        self.protocols = {}  # Track protocols by serial number
        self.request_id = 0
        self.timeouts = {}  # Store timeouts for requests
        self.serial_number = "NOT_SET"



    def buildProtocol(self, addr):
        return MCUProtocol(self)

    def generate_request_id(self):
        self.request_id += 1
        return self.request_id

    def set_timeout(self, request_id, callback, timeout=5):  # Default timeout of 5 seconds
        self.timeouts[request_id] = reactor.callLater(timeout, callback, request_id)

    def clear_timeout(self, request_id):
        if request_id in self.timeouts:
            timeout = self.timeouts.pop(request_id)
            if timeout.active():
                timeout.cancel()

    def handle_response(self, response_obj, protocol):
        request_id = response_obj.RequestId()
        self.clear_timeout(request_id)

        if not protocol.ready and not protocol.ping_ready:
            protocol.ping_ready=True
            logging.info(f"Ping succesful with request id {request_id}")
            protocol.query_serial_number()
        elif not protocol.ready and protocol.ping_ready:
            try:
                sn = self.handle_serial_number(response_obj, protocol,request_id)
                logging.info(f"Get Serial number successful with {sn} with request_id  {request_id}")
                protocol.ready=True
                protocol.serial_number = sn
                self.protocols[sn]=protocol
                self.dispatcher.emit('connection_ready', sn)
            except Exception as e:
                logging.error(f"Serial Number parsing error {e}")
        else:
            self.dispatcher.emit('response_received', request_id, protocol.serial_number,response_obj)


    def handle_timeout(self, request_id):
        if request_id in self.timeouts:
            del self.timeouts[request_id]
            self.dispatcher.emit('request_timeout', request_id)

    def send_request(self, request_id,serial_number, request_binary):
        if serial_number in self.protocols:
            protocol = self.protocols[serial_number]
            #request_id = self.generate_request_id()
            #self.dispatcher.on('response_received', callback)
            protocol.transport.write(get_binary_with_length_prefix(request_binary))
            self.set_timeout(request_id, self.handle_timeout)
            return request_id
        else:
            logging.warning(f"Device with serial number '{serial_number}' not connected")
            raise Exception(f"Device with serial number '{serial_number}' not connected")
            return None

    def handle_serial_number(self, serial_number_resp, protocol,request_id):
        #serial_number_resp = response.response.GetRootAs(response_binary,0)
        if serial_number_resp.RequestId() == request_id:
            serial_num_obj = serial_number.serial_number()
            serial_num_obj.Init(serial_number_resp.Payload().Bytes, serial_number_resp.Payload().Pos)

            # Retrieve the value of the serial number
            serial_value = serial_num_obj.Value().decode('utf-8')
            protocol.serial_number = serial_value
            return serial_value




