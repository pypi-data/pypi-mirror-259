import asyncio

from twisted.internet import reactor, defer
from twisted.internet.threads import deferToThread

import mcu_protocol.function_id
from js_enhanced_logging import logger
from mcu_tcp_impl.mcu_server import MCUFactory
from mcu_functions import functions # create_set_microcontroller_meta_info_request,parse_respone_with_empty_payload
import time
class Device:
    def __init__(self, serial_number):
        self.serial_number = serial_number


        # Initialize other device-specific attributes

class DeviceManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DeviceManager, cls).__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.mcu_factory = MCUFactory()
        self.devices = {}  # Maps serial numbers to device instances
        self.ready = False
        self.pending_requests = {}  # Maps request IDs to deferred objects
        self.avg_response_time = 0  # Average response time in milliseconds
        self.total_responses = 0  # Total number of responses received

    def start(self,host="0.0.0.0",port=13370):
        logger.info("Starting the TCP server...")
        self.mcu_factory.dispatcher.on('connection_ready', self.on_connection_ready)
        self.mcu_factory.dispatcher.on('response_received', self.on_message_received)
        self.mcu_factory.dispatcher.on('request_timeout', self.on_request_timeout)
        self.mcu_factory.dispatcher.on('connection_lost', self.on_connection_lost)
        reactor.listenTCP(port, self.mcu_factory, interface=host)
        reactor.run(installSignalHandlers=False)  # Use False to not interfere with FastAPI's signal handlers

    def stop(self):
        logger.info("Stopping the TCP server...")
        if reactor.running:
            reactor.stop()

    def on_connection_ready(self, serial_number):
        if serial_number not in self.devices:
            self.devices[serial_number] = Device(serial_number)
        self.ready = True
        logger.info(f"Connection ready for device with serial number: {serial_number}")

    async def send_request(self, request_id, serial_number, request_binary,parsing_function=None):
        if not self.ready:
            logger.warning("DeviceManager is not ready.")
            return {"error": "DeviceManager is not ready"}

        if serial_number in self.devices:
            deferred_request = defer.Deferred()
            send_timestamp = time.time() * 1000  # Get current time in milliseconds
            self.pending_requests[request_id] = (deferred_request, send_timestamp)

            # Define a synchronous function to send the request
            def send():
                try:
                    self.mcu_factory.send_request(request_id, serial_number, request_binary)
                except Exception as e:
                    deferred_request.errback(e)
            # Run the synchronous 'send' function in a separate thread
            deferToThread(send)

            # Create an asyncio Future that will be returned by this coroutine
            future = asyncio.Future()

            # When the deferred is called back, set the result of the asyncio Future
            def callback(result):
                if not future.done():
                    future.set_result(parsing_function(result))

            # If there's an error, set the exception of the asyncio Future
            def errback(failure):
                if not future.done():
                    future.set_exception(failure.value)

            # Register the callback and errback
            deferred_request.addCallbacks(callback, errback)

            # Wait for the asyncio Future to be completed
            try:
                result = await future
                return result
            except Exception as e:
                return {"error": str(e)}
        else:
            logger.warning(f"Device with serial number '{serial_number}' not connected")
            return None
    def on_connection_lost(self, serial_number):
        if serial_number  in self.devices:
            self.devices.pop(serial_number)
        if len(self.devices) == 0:
            self.ready = False
        logger.info(f"Connection lost for device with serial number: {serial_number}")
    def on_message_received(self, request_id, serial_number, responseObj):

        #logger.info(f"Received message for request ID: {request_id} at {time.time()*1000}")
        if request_id in self.pending_requests:
            deferred_request, send_timestamp = self.pending_requests.pop(request_id)
            response_timestamp = time.time() * 1000  # Get current time in milliseconds
            response_time = response_timestamp - send_timestamp

            # Update the average response time
            self.total_responses += 1
            self.avg_response_time = ((self.avg_response_time * (
                        self.total_responses - 1)) + response_time) / self.total_responses

            deferred_request.callback(responseObj)  # Pass the response object to the deferred
        else:
            logger.warning(f"Received message for unknown request ID: {request_id}")

    def on_request_timeout(self, request_id):
        if request_id in self.pending_requests:
            deferred_request = self.pending_requests.pop(request_id)
            deferred_request.errback(Exception("Request timed out"))
        else:
            logger.warning(f"Timeout for unknown request ID: {request_id}")

    @property
    def average_response_stats(self):
        return self.avg_response_time,self.total_responses
    async def ping(self, serial_number):
        request_id = self.mcu_factory.generate_request_id()
        request_binary =functions.create_ping_request(request_id)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_respone_with_empty_payload)
        return response

    # Define methods for each STM32 board functionality
    async def set_meta_info(self, serial_number,  row, column, ejection_delay_list, ejection_lasting_list, port_drive_mapping_list):
        request_id  = self.mcu_factory.generate_request_id()
        request_binary = functions.create_set_microcontroller_meta_info_request(
            request_id, row, column, ejection_delay_list, ejection_lasting_list, port_drive_mapping_list
        )
        response = await self.send_request(request_id,serial_number, request_binary,functions.parse_respone_with_empty_payload)

        return response  # Parse and return the response
    async def read_meta_info(self, serial_number):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_read_microcontroller_meta_info_request(request_id)
        request_id,row, column, ejection_delay, ejection_lasting, port_drive_mapping = await self.send_request(request_id, serial_number, request_binary,functions.parse_read_microcontroller_meta_info_response)
        return request_id,row, column, ejection_delay, ejection_lasting, port_drive_mapping

    async def set_authorization_date(self, serial_number, authorization_date):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_request_with_timestamp_request(request_id,mcu_protocol.function_id.function_id.mcu_set_authorization_date, authorization_date)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_respone_with_empty_payload)
        return response

    async def read_authorization_date(self, serial_number):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_request_with_empty_payload(request_id,mcu_protocol.function_id.function_id.mcu_read_authorization_date)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_unixtime_stamp_response)
        return response

    async def set_last_usage_time(self, serial_number, last_usage_time):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_request_with_timestamp_request(request_id,mcu_protocol.function_id.function_id.mcu_set_last_usage_time, last_usage_time)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_respone_with_empty_payload)
        return response

    async def read_last_usage_time(self, serial_number):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_request_with_empty_payload(request_id,mcu_protocol.function_id.function_id.mcu_read_last_usage_time)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_unixtime_stamp_response)
        return response

    async def read_run_time(self, serial_number):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_request_with_empty_payload(request_id,mcu_protocol.function_id.function_id.mcu_read_run_time)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_unixtime_stamp_response)
        #logger.info(f"finish read_run_time at {time.time()*1000} in server api")
        return response

    async def set_motor_speed(self, serial_number, fnid,motor_speed,driver_type,com_address):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_set_speed_request(request_id=request_id,fnid=fnid, speed=motor_speed,driver_type=driver_type,com_address=com_address)#request_id, fnid, speed, driver_type, com_address
        response = await self.send_request(request_id, serial_number, request_binary, functions.parse_motor_info_response)
        return response

    async def read_motor_speed(self, serial_number, fnid,driver_type,com_address):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_read_speed_request(request_id,fnid,driver_type,com_address)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_read_speed_response)
        return response

    async def set_motor_direction(self, serial_number, fnid,driver_type,com_address,direction):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_set_motor_direction_request(request_id,fnid,driver_type,com_address,direction)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_motor_info_response)
        return response

    async def read_motor_direction(self, serial_number, fnid,driver_type,com_address):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_read_motor_direction_request(request_id,fnid,driver_type,com_address)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_read_motor_direction_response)
        return response

    async def set_motor_control_operation(self, serial_number,operation_value,driver_type,com_address):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_motor_control_operation_request(request_id,operation_value,driver_type,com_address)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_motor_info_response)
        return response

    async def read_motor_stats(self, serial_number,driver_type,com_address):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_motor_stats_request(request_id,driver_type,com_address)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_motor_stats_response)
        return response

    async def set_io_status(self, serial_number,io_address,io_status,delay_in_ms=-1,lasting_time_in_ms=-1,repeat=-1):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_io_set_status_request(request_id, io_address,io_status,delay_in_ms,lasting_time_in_ms,repeat)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_respone_with_empty_payload)
        return response

    async def read_io_status(self, serial_number,io_address):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_io_read_status_request(request_id, io_address)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_io_read_status_response)
        return response

    async def set_io_batch_status(self, serial_number,io_address_list,io_status_list,delay_in_ms_list,lasting_time_in_ms_list,repeat_list):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_io_set_status_batch_request(request_id, io_address_list,io_status_list,delay_in_ms_list,lasting_time_in_ms_list,repeat_list)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_respone_with_empty_payload)
        return response
    async def read_io_batch_status(self, serial_number,io_address_list):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_io_read_status_batch_request(request_id, io_address_list)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_io_read_status_batch_response)
        return response

    async def set_trigger_start_count(self, serial_number):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_request_with_empty_payload(request_id,mcu_protocol.function_id.function_id.trigger_start_count)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_respone_with_empty_payload)
        return response

    async def set_trigger_stop_reset_count(self, serial_number):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_request_with_empty_payload(request_id,mcu_protocol.function_id.function_id.trigger_stop_reset_count)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_respone_with_empty_payload)
        return response

    async def set_trigger_simulate(self, serial_number,simulation_count):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_trigger_simulate_request(request_id,simulation_count)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_respone_with_empty_payload)
        return response

    async def read_trigger_count(self, serial_number):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_request_with_empty_payload(request_id,mcu_protocol.function_id.function_id.trigger_read_trigger_count)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_trigger_read_trigger_count_response)
        return response

    async def set_temperature_query_interval(self, serial_number, interval_in_ms):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_sensor_set_query_interval_request(request_id,mcu_protocol.function_id.function_id.sensor_set_temperature_query_interval, interval_in_ms)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_respone_with_empty_payload)
        return response
    async def read_temperature(self, serial_number):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_request_with_empty_payload(request_id,mcu_protocol.function_id.function_id.sensor_read_temperature)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_sensor_read_sensor_response)
        return response

    async def set_pressure_query_interval(self, serial_number, interval_in_ms):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_sensor_set_query_interval_request(request_id,mcu_protocol.function_id.function_id.sensor_set_pressure_query_interval, interval_in_ms)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_respone_with_empty_payload)
        return response

    async def read_pressure(self, serial_number):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_request_with_empty_payload(request_id,mcu_protocol.function_id.function_id.sensor_read_pressure)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_sensor_read_sensor_response)
        return response

    async def ejector_operation_cmd(self, serial_number, trigger_id, group_id, open_status_list, delay_time_list, lasting_time_list):
        request_id = self.mcu_factory.generate_request_id()
        request_binary = functions.create_ejector_operation_cmd_request(request_id, trigger_id, group_id, open_status_list, delay_time_list, lasting_time_list)
        response = await self.send_request(request_id, serial_number, request_binary,functions.parse_respone_with_empty_payload)
        return response