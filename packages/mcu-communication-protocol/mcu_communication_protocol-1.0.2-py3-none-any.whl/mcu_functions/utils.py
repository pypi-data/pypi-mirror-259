from mcu_protocol import content_payload, empty_payload, meta_info, unix_time_stamp, function_id,motor_basic_info
from mcu_protocol import request, response

import time
import flatbuffers


def create_timestamp():
    return time.perf_counter_ns()


def print_hex(name, data):
    hex_values = " ".join(f"{b:02x}" for b in data)
    length = len(data)

    print(f"{'Name:':<15} {name}")
    print(f"{'Length:':<15} {length}")
    print(f"{'Data (Hex):':<15} {hex_values}")


def create_request_with_empty_payload(request_id, function_id):
    builder = flatbuffers.Builder(0)
    # Start and end the empty_payload, since it has no fields
    empty_payload.Start(builder)
    payload = empty_payload.End(builder)

    # Start the request
    request.Start(builder)
    request.AddRequestId(builder, request_id)
    request.AddFunctionId(builder, function_id)  # Use enumeration for 'ping'
    request.AddPayloadType(builder, content_payload.content_payload.empty_payload)  # Use enumeration for empty_payload
    request.AddPayload(builder, payload)
    req = request.End(builder)

    builder.Finish(req)
    return builder.Output()


def create_response_with_empty_playload(request_id):
    builder = flatbuffers.Builder(0)
    # Start and end the empty_payload, since it has no fields
    empty_payload.Start(builder)
    payload = empty_payload.End(builder)

    # Start the request
    response.Start(builder)
    response.AddRequestId(builder, request_id)

    response.AddPayloadType(builder, content_payload.content_payload.empty_payload)  # Use enumeration for empty_payload
    response.AddPayload(builder, payload)
    resp = response.End(builder)

    builder.Finish(resp)
    return builder.Output()


def create_request_with_timestamp_payload(request_id, function_id, timestamp):
    builder = flatbuffers.Builder(0)

    unix_time_stamp.Start(builder)
    unix_time_stamp.AddValue(builder, timestamp)
    timestamp_payload = unix_time_stamp.End(builder)

    # Start the request
    request.Start(builder)
    request.AddRequestId(builder, request_id)
    request.AddFunctionId(builder, function_id)
    request.AddPayloadType(builder,content_payload.content_payload.unix_time_stamp )
    request.AddPayload(builder, timestamp_payload)
    req = request.End(builder)

    builder.Finish(req)
    return builder.Output()



def create_response_with_timestamp_payload(request_id, timestamp):
    builder = flatbuffers.Builder(0)

    unix_time_stamp.Start(builder)
    unix_time_stamp.AddValue(builder, timestamp)
    timestamp_payload = unix_time_stamp.End(builder)

    # Start the request
    response.Start(builder)
    response.AddRequestId(builder, request_id)
    response.AddPayloadType(builder, content_payload.content_payload.unix_time_stamp)
    response.AddPayload(builder, timestamp_payload)
    resp = response.End(builder)

    builder.Finish(resp)
    return builder.Output()


def create_motor_info_response(request_id, driver_type, com_address):
    builder = flatbuffers.Builder(0)

    motor_basic_info.Start(builder)  # Start building the motor_speed object
    motor_basic_info.AddDriverType(builder, driver_type)  # Add the driver_type value
    motor_basic_info.AddComAddress(builder, com_address)  # Add com_address  object
    motor_basic_info_obj = motor_basic_info.End(builder)  # Finalize the motor_speed object

    response.Start(builder)
    response.AddRequestId(builder, request_id)
    response.AddPayloadType(builder, content_payload.content_payload.motor_basic_info)
    response.AddPayload(builder, motor_basic_info_obj)
    resp = response.End(builder)
    builder.Finish(resp)
    return builder.Output()

def create_motor_info_request(request_id,fnid, driver_type, com_address):
    builder = flatbuffers.Builder(0)
    motor_basic_info.Start(builder)  # Start building the motor_speed object
    motor_basic_info.AddDriverType(builder, driver_type)  # Add the driver_type value
    motor_basic_info.AddComAddress(builder, com_address)  # Add com_address  object
    motor_basic_info_obj = motor_basic_info.End(builder)  # Finalize the motor_speed object

    request.Start(builder)
    request.AddRequestId(builder, request_id)
    request.AddFunctionId(builder, fnid)
    request.AddPayloadType(builder, content_payload.content_payload.motor_basic_info)
    request.AddPayload(builder, motor_basic_info_obj)
    req = request.End(builder)
    builder.Finish(req)
    return builder.Output()

def get_binary_with_length_prefix(binary_data, byte_length_for_data_length=4):
    # Send the length of the binary data as a 4-byte integer
    length = len(binary_data)
    return length.to_bytes(byte_length_for_data_length, byteorder='big') + binary_data


def send_binary_with_length_prefix(client_socket, binary_data):
    # Send the length of the binary data as a 4-byte integer
    length = len(binary_data)

    # print(f"sending length: {length}")
    client_socket.sendall(length.to_bytes(4, byteorder='big'))
    # print(f"sending binary data: {binary_data}")
    # Send the binary data itself
    client_socket.sendall(binary_data)
    # print(f"Finsih sending binary data: {binary_data}")


def receive_bit_array_with_length_prefix(bytearray_data,byte_length_for_data_length=4):
    """
  Reads the first 4 bytes of a bytearray as an integer representing the length
  of the remaining data and returns the remaining data.

  Args:
    bytearray_data: A bytearray containing the data to be processed.

  Returns:
    The remaining data after the length prefix, or None if there is an error.
  """

    if len(bytearray_data) < byte_length_for_data_length:
        return None  # Not enough data for the length prefix

    # Extract the length prefix as a 4-byte integer
    length_prefix = int.from_bytes(bytearray_data[:byte_length_for_data_length], byteorder='big')

    # Check if the data length matches the expected length
    if len(bytearray_data) != length_prefix + byte_length_for_data_length:
        return None  # Invalid data length

    # Return the remaining data after the length prefix
    return bytearray_data[byte_length_for_data_length:]


def receive_binary_with_length_prefix(client_socket):
    # First, receive the 4-byte length prefix
    length_prefix = client_socket.recv(4)
    if not length_prefix or len(length_prefix) < 4:
        return None  # Connection closed or error, or not enough data for length prefix

    # Convert the length prefix to an integer
    message_length = int.from_bytes(length_prefix, byteorder='big')
    # print(f"Message length: {message_length}")
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


def get_function_name_by_value(value):
    for name, val in function_id.__dict__.items():
        if val == value:
            return name
    return None  # If the value doesn't match any attribute
