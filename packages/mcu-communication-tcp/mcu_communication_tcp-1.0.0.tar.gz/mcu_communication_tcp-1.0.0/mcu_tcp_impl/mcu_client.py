import socket
from js_enhanced_logging import logger
import argparse
from mcu_functions.functions import (
    create_ping_request,
    create_ping_response,
    create_query_serial_number_response, create_io_read_status_batch_response
)
from mcu_functions.utils import (
    send_binary_with_length_prefix,
    receive_binary_with_length_prefix,
    get_function_name_by_value
)
import mcu_protocol.request as Request
import mcu_protocol.function_id as FunctionId
import mcu_protocol.response as Response
from mcu_protocol import (serial_number, unix_time_stamp,meta_info,motor_basic_info,motor_speed,
                          motor_stats,motor_direction,motor_operation,motor_control_operation,
                          io_operation,io_operation_batch,io_address_batch,io_status,io_address_long,sensor_query_interval)
from mcu_functions.functions import (create_response_with_timestamp_payload,create_response_with_empty_playload,
                                     create_read_microcontroller_meta_info_response,create_read_speed_response,create_motor_stats_response,create_read_motor_direction_response,
                                    create_io_set_status_response,create_trigger_read_trigger_count_response,create_read_sensor_data_response,create_sensor_set_query_interval_request
                                     )
import time
import threading

import flatbuffers
import json
import os
host = "localhost"
port = 13370
start_time = time.time()  # Record the start time

mcu_storage = {
    "serial_number": "python_simulator",
    "authorization_date": 0,
    "meta_info": {}
}


running = False  # Flag to control the thread
thread_lock = threading.Lock()  # Lock for thread-safe variable access

def increment_trigger_count():
    global mcu_storage, running
    for item in range(100):  # Simulate 1000 triggers
        with thread_lock:  # Acquire the lock before modifying
            if running:
                trigger_value = mcu_storage.get("trigger_count", 0)
                trigger_value += 1
                mcu_storage["trigger_count"] = trigger_value
                if mcu_storage["trigger_count"]%10==0:
                    logger.info(f"Trigger count: {mcu_storage['trigger_count']} Running variable is now {running}")  # Log the trigger count
        time.sleep(0.01)  # 50ms delay

def start_trigger_count():
    global running, thread
    logger.info(f"Starting trigger count")
    running = True
    thread = threading.Thread(target=increment_trigger_count)
    thread.start()

def stop_reset_trigger_count():
    global running, mcu_storage
    running = False
    logger.info(f"Stopping trigger count Running variable is now {running}")
    with thread_lock:
        logger.info(f"Resetting trigger count to 0")
        mcu_storage["trigger_count"] = 0

def read_trigger_count():
    logger.info(f"Reading trigger count from memory")
    with thread_lock:
        return mcu_storage["trigger_count"]
def write_json(data, filename='data.json', subdir='app_data'):
    # Get the user's home directory
    home_dir = os.path.expanduser('~')
    # Construct the file path
    file_path = os.path.join(home_dir, subdir, filename)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write the JSON data to the file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
def read_json(filename='data.json', subdir='app_data'):
    # Get the user's home directory
    home_dir = os.path.expanduser('~')
    # Construct the file path
    file_path = os.path.join(home_dir, subdir, filename)

    # Read the JSON data from the file
    try:
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None

def parse_motor_basic_info(motor_basic_info_obj):

    if motor_basic_info_obj is not None:
        # Directly use the fields of the motor_basic_info object
        driver_type = motor_basic_info_obj.DriverType()
        com_address = motor_basic_info_obj.ComAddress()
    else:
        driver_type, com_address = None, None
    return driver_type, com_address
def handle_mcu_ping(request_id,payload):
    response_binary = create_ping_response(request_id)
    logger.info(f"Request id {request_id} Ping returned with {response_binary}")
    return response_binary

def handle_mcu_query_device_serial_number(request_id,payload):
    serial_number_string = f"python_simulator_{host}_{port}_2"
    response_binary = create_query_serial_number_response(request_id, serial_number_string)
    logger.info(f"Request id {request_id} Reading serial number returned with {serial_number_string}")
    return response_binary

def handle_mcu_set_authorization_date(request_id,payload):
    unix_time_stamp_resp = unix_time_stamp.unix_time_stamp()
    unix_time_stamp_resp.Init(payload.Bytes, payload.Pos)
    unix_time_stamp_resp_value = unix_time_stamp_resp.Value()

    logger.info(f"request id {request_id} Received request to set authorization date to {unix_time_stamp_resp_value}")

    mcu_storage["authorization_date"] = unix_time_stamp_resp_value
    try:
        logger.info(f"Writing mcu_storage to file system")
        write_json(mcu_storage)
    except Exception as e:
        logger.error(f"Failed to write to JSON: {e}")
    finally:
        return create_response_with_empty_playload(request_id)

def handle_mcu_read_authorization_date(request_id,payload):
    answer  = mcu_storage["authorization_date"]
    binary_response = create_response_with_timestamp_payload(request_id,answer)
    logger.info(f"Request id {request_id} Reading authorization date returned with {answer}")
    return binary_response

def handle_mcu_set_last_usage_time(request_id,payload):
    unix_time_stamp_resp = unix_time_stamp.unix_time_stamp()
    unix_time_stamp_resp.Init(payload.Bytes, payload.Pos)
    unix_time_stamp_resp_value = unix_time_stamp_resp.Value()
    logger.info(f"Request id {request_id} Received request to set last usage time to {unix_time_stamp_resp_value}")
    mcu_storage["last_usage"] = unix_time_stamp_resp_value
    try:
        logger.info(f"Writing mcu_storage to file system")
        write_json(mcu_storage)
    except Exception as e:
        logger.error(f"Failed to write to JSON: {e}")
    finally:
        return create_response_with_empty_playload(request_id)

def handle_mcu_read_last_usage_time(request_id,payload):
    answer  = mcu_storage["last_usage"]
    binary_response = create_response_with_timestamp_payload(request_id,answer)
    logger.info(f"Request id {request_id} Reading last usage time returned with {answer}")
    return binary_response


def handle_mcu_read_run_time(request_id,payload):
    answer  =int((time.time())*1000)
    binary_response = create_response_with_timestamp_payload(request_id,answer)
    logger.info(f"Request id {request_id} Reading run time returned with {answer}")
    return binary_response
def handle_mcu_set_metainfo(request_id,payload):
    meta_info_resp = meta_info.meta_info()
    meta_info_resp.Init(payload.Bytes, payload.Pos)
    row = meta_info_resp.Row()
    column = meta_info_resp.Column()
    ejection_delay_count = meta_info_resp.EjectionDelayLength()  # Get the length of the vector
    ejection_delay = [meta_info_resp.EjectionDelay(i) for i in range(ejection_delay_count)]  # Retrieve each element

    ejection_lasting_count = meta_info_resp.EjectionLastingLength()  # Get the length of the vector
    ejection_lasting = [meta_info_resp.EjectionLasting(i) for i in
                        range(ejection_lasting_count)]  # Retrieve each element

    port_drive_mapping_count = meta_info_resp.PortDriveMappingLength()  # Get the length of the vector
    port_drive_mapping = [meta_info_resp.PortDriveMapping(i) for i in
                          range(port_drive_mapping_count)]  # Retrieve each element

    logger.info(f"Request id {request_id} Received request to set meta info with row {row} and column {column} returned with ejection_delay {ejection_delay} and ejection_lasting {ejection_lasting} and port_drive_mapping {port_drive_mapping}")
    mcu_storage["meta_info"] = {
        "row": row,
        "column": column,
        "ejection_delay": ejection_delay,
        "ejection_lasting": ejection_lasting,
        "port_drive_mapping": port_drive_mapping
    }
    try:
        logger.info(f"Writing mcu_storage to file system")
        write_json(mcu_storage)
    except Exception as e:
        logger.error(f"Failed to write to JSON: {e}")
    finally:
        return create_response_with_empty_playload(request_id)

def handle_mcu_read_meta_info(request_id,payload):
    meta_info_resp = mcu_storage["meta_info"]
    row = meta_info_resp["row"]
    column = meta_info_resp["column"]
    ejection_delay = meta_info_resp["ejection_delay"]
    ejection_lasting = meta_info_resp["ejection_lasting"]
    port_drive_mapping = meta_info_resp["port_drive_mapping"]
    binary_response = create_read_microcontroller_meta_info_response(request_id, row, column, ejection_delay, ejection_lasting, port_drive_mapping)
    logger.info(f"Request id  {request_id} Reading meta info with row {row} and column {column} returned with ejection_delay {ejection_delay} and ejection_lasting {ejection_lasting} and port_drive_mapping {port_drive_mapping}")
    return binary_response


def handle_motor_set_speed_real_time(request_id,payload):
    motor_speed_req = motor_speed.motor_speed()
    motor_speed_req.Init(payload.Bytes, payload.Pos)
    speed = motor_speed_req.Speed()
    # Directly access the motor_basic_info object from motor_speed
    motor_basic_info_obj = motor_speed_req.MotorInfo()
    driver_type, com_address = parse_motor_basic_info(motor_basic_info_obj)


    logger.info(f"Request id {request_id} Received request to set motor speed real time with speed {speed} and driver_type {driver_type} and com_address {com_address}")
    mcu_storage["motor_speed_real_time"] = {
        "speed":speed,
        "driver_type":driver_type,
        "com_address":com_address
    }
    try:
        logger.info(f"Writing mcu_storage to file system with motor_speed_real_time {mcu_storage['motor_speed_real_time']}")
        write_json(mcu_storage)
    except Exception as e:
        logger.error(f"Failed to write to JSON: {e}")
    return create_response_with_empty_playload(request_id)

def handle_motor_read_speed_real_time(request_id,payload):
    motor_basic_info_obj = motor_basic_info.motor_basic_info()
    motor_basic_info_obj.Init(payload.Bytes, payload.Pos)
    driver_type, com_address = parse_motor_basic_info(motor_basic_info_obj)


    motor_speed_real_time = mcu_storage["motor_speed_real_time"]
    speed = motor_speed_real_time["speed"]
    driver_type = motor_speed_real_time["driver_type"]
    com_address = motor_speed_real_time["com_address"]
    binary_response = create_read_speed_response(request_id, speed, driver_type, com_address)
    logger.info(f"Request id {request_id} Reading motor speed real time with driver_type {driver_type} and com_address {com_address} returned with speed {speed}")
    return binary_response

def handle_motor_set_work_speed(request_id,payload):
    motor_speed_resp = motor_speed.motor_speed()
    motor_speed_resp.Init(payload.Bytes, payload.Pos)
    speed = motor_speed_resp.Speed()

    motor_basic_info_obj = motor_speed_resp.MotorInfo()
    driver_type, com_address = parse_motor_basic_info(motor_basic_info_obj)

    logger.info(f"Request id {request_id} Received request to set motor work speed with speed {speed} and driver_type {driver_type} and com_address {com_address}")
    mcu_storage["motor_work_speed"] = {
        "speed":speed,
        "driver_type":driver_type,
        "com_address":com_address
    }

    try:
        logger.info(f"Writing mcu_storage to file system with motor_work_speed {mcu_storage['motor_work_speed']}")
        write_json(mcu_storage)
    except Exception as e:
        logger.error(f"Failed to write to JSON: {e}")
    return create_response_with_empty_playload(request_id)

def handle_motor_read_work_speed(request_id,payload):
    motor_basic_info_obj = motor_basic_info.motor_basic_info()
    motor_basic_info_obj.Init(payload.Bytes, payload.Pos)
    driver_type, com_address = parse_motor_basic_info(motor_basic_info_obj)


    motor_work_speed = mcu_storage["motor_work_speed"]
    speed = motor_work_speed["speed"]
    driver_type = motor_work_speed["driver_type"]
    com_address = motor_work_speed["com_address"]

    binary_response = create_read_speed_response(request_id, speed, driver_type, com_address)

    logger.info(f"Request id {request_id} Reading motor work speed with driver_type {driver_type} and com_address {com_address} returned with speed {speed}")
    return binary_response

def handle_motor_set_rotation_direction(request_id,payload):
    motor_direction_resp = motor_direction.motor_direction()
    motor_direction_resp.Init(payload.Bytes, payload.Pos)
    direction = motor_direction_resp.Direction()

    motor_basic_info_obj = motor_direction_resp.MotorInfo()
    driver_type, com_address = parse_motor_basic_info(motor_basic_info_obj)
    logger.info(f"Request id {request_id} Received request to set motor rotation direction with direction {direction} and driver_type {driver_type} and com_address {com_address}")
    mcu_storage["motor_direction"] = {
        "direction":direction,
        "driver_type":driver_type,
        "com_address":com_address
    }

    try:
        logger.info(f"Writing mcu_storage to file system with motor_direction {mcu_storage['motor_direction']}")
        write_json(mcu_storage)
    except Exception as e:
        logger.error(f"Failed to write to JSON: {e}")
    return create_response_with_empty_playload(request_id)

def handle_motor_read_rotation_direction(request_id,payload):
    motor_basic_info_obj = motor_basic_info.motor_basic_info()
    motor_basic_info_obj.Init(payload.Bytes, payload.Pos)
    driver_type, com_address = parse_motor_basic_info(motor_basic_info_obj)

    motor_direction = mcu_storage["motor_direction"]
    direction = motor_direction["direction"]
    driver_type = motor_direction["driver_type"]
    com_address = motor_direction["com_address"]


    binary_response = create_read_motor_direction_response(request_id, direction, driver_type, com_address)

    logger.info(
        f"Request id {request_id} Reading motor direction with driver_type {driver_type} and com_address {com_address} returned with direction {direction}")
    return binary_response

def handle_motor_set_control_operation(request_id,payload):
    motor_operation_resp = motor_control_operation.motor_control_operation()
    motor_operation_resp.Init(payload.Bytes, payload.Pos)
    operation = motor_operation_resp.Value()

    motor_basic_info_obj = motor_operation_resp.MotorInfo()
    driver_type, com_address = parse_motor_basic_info(motor_basic_info_obj)

    logger.info(f"Request id {request_id} Received request to set motor control operation with operation {operation} and driver_type {driver_type} and com_address {com_address}")
    mcu_storage["motor_control_operation"] = {
        "operation":operation,
        "driver_type":driver_type,
        "com_address":com_address
    }

    try:
        logger.info(f"Writing mcu_storage to file system with motor_control_operation {mcu_storage['motor_control_operation']}")
        write_json(mcu_storage)
    except Exception as e:
        logger.error(f"Failed to write to JSON: {e}")
    return create_response_with_empty_playload(request_id)

def handle_motor_read_stats(request_id,payload):
    motor_basic_info_obj = motor_basic_info.motor_basic_info()
    motor_basic_info_obj.Init(payload.Bytes, payload.Pos)
    driver_type, com_address = parse_motor_basic_info(motor_basic_info_obj)
    motor_stats_json = mcu_storage.get("motor_stats", {})
    avg_load = motor_stats_json.get("avg_load",78.1)
    max_load = motor_stats_json.get("max_load", 120.1)
    realtime_speed = motor_stats_json.get("realtime_speed", 2000.19)
    logger.info(f"Request id {request_id} Reading motor stats with driver_type {driver_type} and com_address {com_address} returned with with avg_load {avg_load} and max_load {max_load} realtime_speed {realtime_speed}")

    return create_motor_stats_response(request_id,driver_type,com_address,avg_load,max_load,realtime_speed )

def handle_io_set_status(request_id,payload):
    from mcu_functions.functions import create_io_set_status_response
    io_operation_req = io_operation.io_operation()
    io_operation_req.Init(payload.Bytes, payload.Pos)
    io_address = io_operation_req.IoAddress()
    io_status = io_operation_req.Status()
    delay_in_ms = io_operation_req.DelayInMs()
    lasting_time_in_ms = io_operation_req.LastingTimeInMs()
    repeat = io_operation_req.Repeat()


    logger.info(f"Request id {request_id} Received request to set IO status with io_address {io_address} and io_status {io_status} and delay_in_ms {delay_in_ms} and lasting_time_in_ms {lasting_time_in_ms} and repeat {repeat}")
    return create_io_set_status_response(request_id)

def handle_io_batch_set_status(request_id,payload):
    from mcu_functions.functions import create_io_set_status_batch_response
    io_operation_batch_req = io_operation_batch.io_operation_batch()
    io_operation_batch_req.Init(payload.Bytes, payload.Pos)
    io_operation_list_length = io_operation_batch_req.ValuesLength()
    io_operation_list = [io_operation_batch_req.Values(i) for i in
                         range(io_operation_list_length)]

    def io_operation_to_dict(io_op):
        """Convert an io_operation object to a dictionary for easier logging."""
        return {
            'IoAddress': io_op.IoAddress(),
            'Status': io_op.Status(),
            'DelayInMs': io_op.DelayInMs(),
            'LastingTimeInMs': io_op.LastingTimeInMs(),
            'Repeat': io_op.Repeat()
        }
    readable_io_operations = [io_operation_to_dict(io_op) for io_op in io_operation_list]

    logger.info(f"Request id {request_id} Received request to set IO status batch with io_operation_list {readable_io_operations}")

    mcu_storage["io_batch_status"] = readable_io_operations
    try:
        logger.info(f"Writing mcu_storage to file system with io_batch_status {mcu_storage['io_batch_status']}")
        write_json(mcu_storage)
    except Exception as e:
        logger.error(f"Failed to write to JSON: {e}")
    return create_io_set_status_batch_response(request_id)

def handle_io_read_status(request_id,payload):
    from mcu_functions.functions import create_io_read_status_response
    io_address_long_resp = io_address_long.io_address_long()
    io_address_long_resp.Init(payload.Bytes, payload.Pos)
    io_address = io_address_long_resp.Value()
    io_status = mcu_storage.get("io_status", {}).get(io_address, False)
    logger.info(f"Request id {request_id} Reading IO status with io_address {io_address} returned with io_status {io_status}")
    return  create_io_read_status_response(request_id,io_status)

def handle_io_batch_read_status(request_id,payload):
    io_address_batch_req = io_address_batch.io_address_batch()
    io_address_batch_req.Init(payload.Bytes, payload.Pos)
    io_address_list_length = io_address_batch_req.ValuesLength()
    io_address_list = [io_address_batch_req.Values(i) for i in
                            range(io_address_list_length)]


    io_batch_status = mcu_storage.get("io_batch_status", {})
    io_status_list = [io_status_obj.get("Status", False) for io_status_obj in io_batch_status]
    logger.info(f"Request id {request_id} Reading IO status batch with io_address_list {io_address_list} returned with io_status_list {io_status_list}")

    return create_io_read_status_batch_response(request_id,io_status_list)

def handle_trigger_start_count(request_id,payload):
    logger.info(f"Request id {request_id} Received request to start trigger count")
    start_trigger_count()
    return create_response_with_empty_playload(request_id)

def handle_trigger_stop_reset_count(request_id,payload):
    stop_reset_trigger_count()
    logger.info(f"Request id {request_id} Received request to stop/reset trigger count")
    return create_response_with_empty_playload(request_id)

def handle_trigger_simulate(request_id,payload):
    logger.info(f"Request id {request_id} Received request to simulate trigger")
    return create_response_with_empty_playload(request_id)


def handle_trigger_read_trigger_count(request_id,payload):
    trigger_count = read_trigger_count()
    logger.info(f"Request id {request_id} Received request to read trigger count")
    return create_trigger_read_trigger_count_response(request_id,trigger_count)

def handle_sensor_read_temperature(request_id,payload):
    sensor_data_list = [23,24,25,26,27,28,29,30,31,32]
    logger.info(f"Request id {request_id} Received request to read temperature and replied with sensor data list {sensor_data_list}")
    return create_read_sensor_data_response(request_id,sensor_data_list)

def handle_sensor_set_temperature_query_interval(request_id,payload):
    sensor_query_interval_req = sensor_query_interval.sensor_query_interval()
    sensor_query_interval_req.Init(payload.Bytes, payload.Pos)
    interval = sensor_query_interval_req.Interval()
    logger.info(f"Request id {request_id} Received request to set temperature query interval {interval}")
    return create_response_with_empty_playload(request_id)

def handle_sensor_read_pressure(request_id,payload):
    sensor_data_list = [0.78,0.56,0.23,0.33,0.45,0.67,0.22,0.33,0.31,0.32]
    logger.info(f"Request id {request_id} Received request to read pressure and replied with sensor data list {sensor_data_list}")
    return create_read_sensor_data_response(request_id,sensor_data_list)

def handle_sensor_set_pressure_query_interval(request_id,payload):
    sensor_query_interval_req = sensor_query_interval.sensor_query_interval()
    sensor_query_interval_req.Init(payload.Bytes, payload.Pos)
    interval = sensor_query_interval_req.Interval()
    logger.info(f"Request id {request_id} Received request to set pressure query interval {interval}")
    return create_response_with_empty_playload(request_id)

def handle_ejector_operation_cmd(request_id,payload):
    logger.info(f"Request id {request_id} Received request to ejector operation cmd")
    return create_response_with_empty_playload(request_id)

# Map function IDs to their corresponding handler functions
# class function_id(object):
#     none = 0
#     mcu_ping = 1
#     mcu_query_device_serial_number = 2
#     mcu_set_microcontroller_meta_info = 3
#     mcu_read_microcontroller_meta_info = 4
#     mcu_set_authorization_date = 5
#     mcu_read_authorization_date = 6
#     mcu_set_last_usage_time = 7
#     mcu_read_last_usage_time = 8
#     mcu_read_run_time = 9
#     motor_set_speed_real_time = 10
#     motor_read_speed_real_time = 11
#     motor_set_work_speed = 12
#     motor_read_work_speed = 13
#     motor_set_rotation_direction = 14
#     motor_read_rotation_direction = 15
#     motor_set_control_operation = 16
#     motor_read_stats = 17
#     io_set_status = 20
#     io_batch_set_status = 21
#     io_read_status = 22
#     io_batch_read_status = 23
#     trigger_start_count = 30
#     trigger_stop_reset_count = 31
#     trigger_simulate = 32
#     trigger_read_trigger_count = 33
#     sensor_read_temperature = 40
#     sensor_set_temperature_query_interval = 41
#     sensor_read_pressure = 42
#     sensor_set_pressure_query_interval = 43
#     ejector_operation_cmd = 50
function_handlers = {
    FunctionId.function_id.mcu_ping: handle_mcu_ping,
    FunctionId.function_id.mcu_query_device_serial_number: handle_mcu_query_device_serial_number,
    FunctionId.function_id.mcu_set_authorization_date: handle_mcu_set_authorization_date,
    FunctionId.function_id.mcu_read_authorization_date: handle_mcu_read_authorization_date,
    FunctionId.function_id.mcu_set_microcontroller_meta_info:handle_mcu_set_metainfo,
    FunctionId.function_id.mcu_read_microcontroller_meta_info:handle_mcu_read_meta_info,
    FunctionId.function_id.mcu_set_last_usage_time: handle_mcu_set_last_usage_time,
    FunctionId.function_id.mcu_read_last_usage_time: handle_mcu_read_last_usage_time,
    FunctionId.function_id.mcu_read_run_time: handle_mcu_read_run_time,
    FunctionId.function_id.motor_set_speed_real_time: handle_motor_set_speed_real_time,
    FunctionId.function_id.motor_read_speed_real_time: handle_motor_read_speed_real_time,
    FunctionId.function_id.motor_set_work_speed: handle_motor_set_work_speed,
    FunctionId.function_id.motor_read_work_speed: handle_motor_read_work_speed,
    FunctionId.function_id.motor_set_rotation_direction: handle_motor_set_rotation_direction,
    FunctionId.function_id.motor_read_rotation_direction: handle_motor_read_rotation_direction,
    FunctionId.function_id.motor_set_control_operation: handle_motor_set_control_operation,
    FunctionId.function_id.motor_read_stats: handle_motor_read_stats,
    FunctionId.function_id.io_set_status: handle_io_set_status,
    FunctionId.function_id.io_batch_set_status: handle_io_batch_set_status,
    FunctionId.function_id.io_read_status: handle_io_read_status,
    FunctionId.function_id.io_batch_read_status: handle_io_batch_read_status,
    FunctionId.function_id.trigger_start_count: handle_trigger_start_count,
    FunctionId.function_id.trigger_stop_reset_count: handle_trigger_stop_reset_count,
    FunctionId.function_id.trigger_simulate: handle_trigger_simulate,
    FunctionId.function_id.trigger_read_trigger_count: handle_trigger_read_trigger_count,
    FunctionId.function_id.sensor_read_temperature: handle_sensor_read_temperature,
    FunctionId.function_id.sensor_set_temperature_query_interval: handle_sensor_set_temperature_query_interval,
    FunctionId.function_id.sensor_read_pressure: handle_sensor_read_pressure,
    FunctionId.function_id.sensor_set_pressure_query_interval: handle_sensor_set_pressure_query_interval,
    FunctionId.function_id.ejector_operation_cmd: handle_ejector_operation_cmd




    # Add more mappings as needed
}
def handle_request(request_binary, client_socket):
    #print("Received a request from the server the binary is: ", request_binary)
    # Parse the request using FlatBuffers
    buf = bytearray(request_binary)
    req = Request.request.GetRootAs(buf, 0)
    request_id = req.RequestId()
    function_id = req.FunctionId()
    #logger.debug(f"Received request with function ID :{function_id} and request ID {request_id} with {client_socket}")
    # Decide what response to send based on the function ID
    handler = function_handlers.get(function_id)

    if handler:
        response_binary = None
        # Call the handler function and get the response binary
        try:
            response_binary = handler(request_id,req.Payload())
        except Exception as e:
            logger.error(f"ReqestId {request_id} Failed to handle request with function ID {function_id}: {e}")
            response_binary = None

    else:
        logger.warning(f"Received unknown function ID {function_id} from the server")
        return None
    #print(f"Sending out with send_binary_with_length_prefix")
    # Send the response back to the server
    send_binary_with_length_prefix(client_socket, response_binary)


def main(host, port):
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect((host, port))
                logger.info(f"Connected to {host}:{port}")

                client_address = client_socket.getpeername()  # Returns a tuple (IP, port)
                logger.info(f"Handling client at {client_address}")
                # Main loop to listen for requests from the server
                while True:
                    try:
                        request_binary = receive_binary_with_length_prefix(client_socket)
                    except Exception as e1:
                        logger.error(f"Failed to parse a request from the server: {e1}")
                        break
                    if not request_binary:
                        logger.error("Server closed the connection or sent an incomplete message.")
                        break
                    try:
                        handle_request(request_binary, client_socket)
                    except Exception as e1:
                        logger.fatal(f"Failed to handle_request from the server: {e1}")


            except ConnectionRefusedError:  # Handle initial connection refusals

                logger.warning(f"Connection refused by server. Retrying in 5 seconds...")

                time.sleep(1)  # Wait before retrying

            except Exception as e:  # Other connection errors

                logger.error(f"Connection error: {e}. Retrying in 5 seconds...")

                time.sleep(5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP Client Simulator")
    parser.add_argument("--host", default="localhost", help="Host address of the TCP server")
    parser.add_argument("--port", type=int, default=13370, help="Port number of the TCP server")
    args = parser.parse_args()
    host = args.host
    port = args.port
    start_time = time.time()  # Record the start time

    mcu_storage= read_json()
    if mcu_storage is None:
        mcu_storage = {
            "serial_number": "python_simulator",
            "authorization_date": 0,
            "io_batch_status": [],
            "trigger_count":0,
            "meta_info": {}
        }
    main(args.host, args.port)
