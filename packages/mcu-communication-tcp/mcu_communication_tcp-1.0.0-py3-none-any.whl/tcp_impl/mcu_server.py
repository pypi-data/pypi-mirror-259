import socket
import threading
import queue
import time
from mcu_functions.functions import create_ping_request, create_query_serial_number_request
from mcu_protocol import request, response


class TCPServer:
    def __init__(self, host='0.0.0.0', port=12345, ping_interval=30, max_ping_failures=3, send_interval=0.001):
        self.host = host
        self.port = port
        self.ping_interval = ping_interval
        self.max_ping_failures = max_ping_failures
        self.send_interval = send_interval
        self.client_map = {}  # Temporary ID -> Connection
        self.serial_map = {}  # Serial Number -> Connection
        self.request_queue = queue.Queue()
        self.response_map = {}  # Request ID -> Response Event
        self.request_id = 0
        self.connection_lock = threading.Lock()
        self.keep_running = True
        self.ready_to_send = False
        self.server_thread = threading.Thread(target=self.run_server)
        self.process_thread = threading.Thread(target=self.process_requests)

    def start(self):
        self.server_thread.start()
        self.process_thread.start()

    def run_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()
            while self.keep_running:
                client_socket, _ = server_socket.accept()
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def initialize_connection(self, client_socket):
        pass

    def handle_client(self, client_socket):
        temp_id = None
        try:
            # Initial Ping
            if self.ping_client(client_socket):
                # Query Serial Number
                serial_number = self.query_serial_number(client_socket)
                if serial_number:
                    with self.connection_lock:
                        temp_id = len(self.client_map) + 1
                        self.client_map[temp_id] = client_socket
                        self.serial_map[serial_number] = client_socket
                    self.ready_to_send = True
                    # Handle ongoing communication
                    self.communicate_with_client(client_socket, serial_number)
        finally:
            with self.connection_lock:
                if temp_id and temp_id in self.client_map:
                    del self.client_map[temp_id]
                client_socket.close()

    def ping_client(self, client_socket):
        # Construct and send a ping request
        request_id = self.generate_request_id()
        ping_request = create_ping_request(request_id)
        self.send_binary_with_length_prefix(client_socket, ping_request)

        # Wait for a response with a timeout
        client_socket.settimeout(5)  # Set a 5-second timeout for example
        try:
            response_binary = self.receive_binary_with_length_prefix(client_socket)
            ping_reps = response.response.GetRootAs(response_binary, 0)
            if (ping_reps.RequestId() == request_id):
                return True  # Return True if the ping response is valid
            else:
                return False
        except socket.timeout:
            return False  # Return False if there was a timeout (no response)

    def query_serial_number(self, client_socket):
        # Construct and send a query serial number request
        request_id = self.generate_request_id()
        serial_number_request = create_query_serial_number_request(request_id)
        self.send_binary_with_length_prefix(client_socket, serial_number_request)

        # Wait for a response with a timeout
        client_socket.settimeout(5)  # Set a 5-second timeout for example
        try:
            response_binary = self.receive_binary_with_length_prefix(client_socket)
            if response_binary:
                # Parse the response using FlatBuffers
                serial_number_resp = response.response.GetRootAs(response_binary,
                                                                 0)  # Assume 'response' is the FlatBuffers table for responses

                # Check if the response's request ID matches the one we sent
                if serial_number_resp.RequestId() == request_id:
                    # Extract the serial number from the response
                    # Assuming the response has a method to get the serial number, e.g., GetSerialNumber()
                    serial_number = serial_number_resp.GetSerialNumber()
                    return serial_number  # Return the extracted serial number

        except socket.timeout:
            pass  # Handle timeout, e.g., by logging or retrying

        return None  # Return None if there was a timeout or if the response did not match

    def communicate_with_client(self, client_socket, serial_number):
        # Handle messages from the client
        pass

    def process_requests(self):
        while self.keep_running:
            if not self.request_queue.empty():
                request, serial_number = self.request_queue.get()
                client_socket = self.serial_map.get(serial_number)
                if client_socket:
                    try:
                        self.send_binary_with_length_prefix(client_socket, request)
                        ##client_socket.sendall(request)
                    except Exception as e:
                        print(f"Error sending request: {e}")
                    time.sleep(self.send_interval)

    def send_request(self, serial_number, request_binary):
        # Add the request to the queue
        self.request_queue.put((request_binary, serial_number))

    def send_binary_with_length_prefix(self, client_socket, binary_data):
        # Send the length of the binary data as a 4-byte integer
        length = len(binary_data)
        client_socket.sendall(length.to_bytes(4, byteorder='big'))
        # Send the binary data itself
        client_socket.sendall(binary_data)

    def receive_binary_with_length_prefix(self, client_socket):
        # First, receive the 4-byte length prefix
        length_prefix = client_socket.recv(4)
        if not length_prefix or len(length_prefix) < 4:
            return None  # Connection closed or error, or not enough data for length prefix

        # Convert the length prefix to an integer
        message_length = int.from_bytes(length_prefix, byteorder='big')

        # Now receive the rest of the message based on the length prefix
        message = b''
        while len(message) < message_length:
            chunk = client_socket.recv(message_length - len(message))
            if not chunk:
                return None  # Connection closed or error
            message += chunk

        # At this point, `message` contains the complete message data if it's equal to message_length
        if len(message) == message_length:
            return message  # Return the complete message
        else:
            return None  # The message is incomplete

    def stop(self):
        self.keep_running = False
        self.server_thread.join()
        self.process_thread.join()

    def generate_request_id(self):
        # Increment and return a unique request ID
        self.request_id += 1
        return self.request_id

    def get_active_serial_numbers(self):
        # Return a list of active serial numbers
        return list(self.serial_map.keys())

    def is_ready_to_send(self):
        # Return the server's readiness to send messages
        return self.ready_to_send
