from mcu_protocol import function_id
from .utils import create_request_with_empty_payload, create_response_with_empty_playload, \
    create_request_with_timestamp_payload, create_response_with_timestamp_payload, create_timestamp,create_motor_info_response,create_motor_info_request
from mcu_protocol import content_payload, empty_payload, meta_info, unix_time_stamp, serial_number, motor_speed, \
    motor_stats, motor_direction, motor_basic_info, motor_control_operation,motor_basic_info,io_operation,io_address_long,io_status,io_address_batch,io_status_batch,io_operation_batch,trigger_start_position,read_trigger_count,sensor_data,sensor_query_interval,ejector_data
from mcu_protocol import request, response
import time
import flatbuffers
import numpy as np
import logging

#### ping
def create_ping_request(request_id):
    return create_request_with_empty_payload(request_id, function_id.function_id.mcu_ping)


def create_ping_response(request_id):
    return create_response_with_empty_playload(request_id)

def parse_respone_with_empty_payload(response):
    request_id = response.RequestId()
    return request_id

#### serial number
def create_query_serial_number_request(request_id):
    return create_request_with_empty_payload(request_id, function_id.function_id.mcu_query_device_serial_number)


def create_query_serial_number_response(request_id, serial_number_string):
    builder = flatbuffers.Builder(0)

    # Create the serial number string and get its offset
    serial_str_offset = builder.CreateString(serial_number_string)

    # Start the serial_number table and add the value
    serial_number.Start(builder)
    serial_number.AddValue(builder, serial_str_offset)
    serial_number_offset = serial_number.End(builder)

    # Start the response table
    response.Start(builder)
    # Add the request ID
    response.AddRequestId(builder, request_id)
    # Set the payload type to serial_number
    response.AddPayloadType(builder, content_payload.content_payload.serial_number)
    # Add the payload
    response.AddPayload(builder, serial_number_offset)
    response_offset = response.End(builder)

    # Finish the response
    builder.Finish(response_offset)
    return builder.Output()

def create_request_with_timestamp_request(request_id, fnid,timestamp):
    return create_request_with_timestamp_payload(request_id, fnid, timestamp)
def parse_unixtime_stamp_response(response):
    #logging.info(f"Parsing unix time stamp response at {time.time()*1000}")
    unix_time_stamp_resp = unix_time_stamp.unix_time_stamp()
    unix_time_stamp_resp.Init(response.Payload().Bytes, response.Payload().Pos)
    unix_time_stamp_resp_value = unix_time_stamp_resp.Value()
    request_id = response.RequestId()
    #logging.info(f"Finish Unix time stamp response parsed at {time.time()*1000}")
    return request_id ,unix_time_stamp_resp_value

#### set microcontroller meta info
def create_set_microcontroller_meta_info_request(requestId, row, column, ejection_delay, ejection_lasting,
                                                 port_drive_mapping):
    builder = flatbuffers.Builder(0)

    if(len(ejection_delay) != len(ejection_lasting)):
        raise ValueError(f"Ejection delay length {len(ejection_delay)} and ejection lasting length {len(ejection_lasting)} should be the same")

    # Create vectors before starting the meta_info table
    ejection_delay_vector = builder.CreateNumpyVector(np.array(ejection_delay, dtype='int8'))
    ejection_lasting_vector = builder.CreateNumpyVector(np.array(ejection_lasting, dtype='int8'))
    port_drive_mapping_vector = builder.CreateNumpyVector(np.array(port_drive_mapping, dtype='int8'))

    meta_info.Start(builder)
    meta_info.AddRow(builder, row)
    meta_info.AddColumn(builder, column)
    meta_info.AddEjectionDelay(builder, ejection_delay_vector)
    meta_info.AddEjectionLasting(builder, ejection_lasting_vector)
    meta_info.AddPortDriveMapping(builder, port_drive_mapping_vector)
    payload = meta_info.End(builder)

    request.Start(builder)
    request.AddRequestId(builder, requestId)
    request.AddFunctionId(builder, function_id.function_id.mcu_set_microcontroller_meta_info)
    request.AddPayloadType(builder, content_payload.content_payload.meta_info)
    request.AddPayload(builder, payload)
    req = request.End(builder)
    builder.Finish(req)
    return builder.Output()


def create_set_microcontroller_meta_info_response(request_id):
    return create_response_with_empty_playload(request_id)



def parse_read_microcontroller_meta_info_response(response):
    meta_info_resp = meta_info.meta_info()
    meta_info_resp.Init(response.Payload().Bytes, response.Payload().Pos)
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

    request_id = response.RequestId()
    return request_id,row, column, ejection_delay, ejection_lasting, port_drive_mapping
#### read microcontroller meta info
def create_read_microcontroller_meta_info_request(request_id):
    return create_request_with_empty_payload(request_id, function_id.function_id.mcu_read_microcontroller_meta_info)


def create_read_microcontroller_meta_info_response(request_id, row, column, ejection_delay, ejection_lasting,
                                                   port_drive_mapping):
    builder = flatbuffers.Builder(0)
    ejection_delay_vector = builder.CreateNumpyVector(np.array(ejection_delay, dtype='int8'))
    ejection_lasting_vector = builder.CreateNumpyVector(np.array(ejection_lasting, dtype='int8'))
    port_drive_mapping_vector = builder.CreateNumpyVector(np.array(port_drive_mapping, dtype='int8'))

    meta_info.Start(builder)
    meta_info.AddRow(builder, row)
    meta_info.AddColumn(builder, column)
    meta_info.AddEjectionDelay(builder, ejection_delay_vector)
    meta_info.AddEjectionLasting(builder, ejection_lasting_vector)
    meta_info.AddPortDriveMapping(builder, port_drive_mapping_vector)
    payload = meta_info.End(builder)

    response.Start(builder)
    response.AddRequestId(builder, request_id)
    response.AddPayloadType(builder, content_payload.content_payload.meta_info)
    response.AddPayload(builder, payload)
    resp = response.End(builder)
    builder.Finish(resp)

    return builder.Output()

############### Motor #############
def create_set_speed_request(request_id, fnid, speed, driver_type, com_address):
    builder = flatbuffers.Builder(0)

    motor_basic_info.Start(builder)
    motor_basic_info.AddDriverType(builder, driver_type)
    motor_basic_info.AddComAddress(builder, com_address)
    motor_basic_info_obj = motor_basic_info.End(builder)


    motor_speed.Start(builder)  # Start building the motor_speed object
    motor_speed.AddSpeed(builder, speed)  # Add the speed value
    motor_speed.AddMotorInfo(builder, motor_basic_info_obj)  # Add the motor_basic_info object (optional, can be None
    motor_speed_obj = motor_speed.End(builder)  # Finalize the motor_speed object

    request.Start(builder)
    request.AddRequestId(builder, request_id)
    request.AddFunctionId(builder, fnid)
    request.AddPayloadType(builder, content_payload.content_payload.motor_speed)
    request.AddPayload(builder, motor_speed_obj)
    req = request.End(builder)
    builder.Finish(req)

    return builder.Output()
def parse_set_speed_request(request):
    motor_speed_req = motor_speed.motor_speed.GetRootAs(request.Payload().Bytes, request.Payload().Pos)
    speed = motor_speed_req.Speed()

    # Directly access the motor_basic_info object from motor_speed
    motor_basic_info_obj = motor_speed_req.MotorInfo()

    if motor_basic_info_obj is not None:
        # Directly use the fields of the motor_basic_info object
        driver_type = motor_basic_info_obj.DriverType()
        com_address = motor_basic_info_obj.ComAddress()
    else:
        driver_type, com_address = None, None

    request_id = request.RequestId()
    return request_id, speed, driver_type, com_address
def create_set_speed_response(request_id, driver_type, com_address):
    return create_motor_info_response(request_id, driver_type, com_address)
def parse_motor_info_response(response):
    motor_basic_info_resp = motor_basic_info.motor_basic_info()
    motor_basic_info_resp.Init(response.Payload().Bytes, response.Payload().Pos)
    driver_type = motor_basic_info_resp.DriverType()
    com_address = motor_basic_info_resp.ComAddress()

    request_id = response.RequestId()
    return request_id ,driver_type, com_address

def parse_read_speed_response(response):
    motor_speed_resp = motor_speed.motor_speed()
    motor_speed_resp.Init(response.Payload().Bytes, response.Payload().Pos)
    speed = motor_speed_resp.Speed()
    # Directly access the motor_basic_info object from motor_speed
    motor_basic_info_obj = motor_speed_resp.MotorInfo()

    if motor_basic_info_obj is not None:
        # Directly use the fields of the motor_basic_info object
        driver_type = motor_basic_info_obj.DriverType()
        com_address = motor_basic_info_obj.ComAddress()
    else:
        driver_type, com_address = None, None
    request_id = response.RequestId()
    return request_id,speed, driver_type, com_address

def create_read_speed_request(request_id, fnid,driver_type, com_address):
    return create_motor_info_request(request_id,fnid,driver_type,com_address)

def create_read_speed_response(request_id, speed, driver_type, com_address):
    builder = flatbuffers.Builder(0)

    motor_basic_info.Start(builder)
    motor_basic_info.AddDriverType(builder, driver_type)
    motor_basic_info.AddComAddress(builder, com_address)
    motor_basic_info_obj = motor_basic_info.End(builder)

    motor_speed.Start(builder)  # Start building the motor_speed object
    motor_speed.AddSpeed(builder, speed)  # Add the speed value
    motor_speed.AddMotorInfo(builder, motor_basic_info_obj)  # Add the motor_basic_info object (optional, can be None
    motor_speed_obj = motor_speed.End(builder)  # Finalize the motor_speed object


    response.Start(builder)
    response.AddRequestId(builder, request_id)
    response.AddPayloadType(builder, content_payload.content_payload.motor_speed)
    response.AddPayload(builder, motor_speed_obj)
    resp = response.End(builder)
    builder.Finish(resp)

    return builder.Output()


def create_set_motor_direction_request(request_id, fnid, direction, driver_type, com_address):
    builder = flatbuffers.Builder(0)

    motor_basic_info.Start(builder)
    motor_basic_info.AddDriverType(builder, driver_type)
    motor_basic_info.AddComAddress(builder, com_address)
    motor_basic_info_obj = motor_basic_info.End(builder)

    motor_direction.Start(builder)  # Start building the motor_speed object
    motor_direction.AddDirection(builder, direction)  # Add the speed value
    motor_direction.AddMotorInfo(builder, motor_basic_info_obj)  # Add the motor_basic_info object (optional, can be None
    motor_direction_obj = motor_speed.End(builder)  # Finalize the motor_speed object


    request.Start(builder)
    request.AddRequestId(builder, request_id)
    request.AddFunctionId(builder, fnid)
    request.AddPayloadType(builder, content_payload.content_payload.motor_direction)
    request.AddPayload(builder, motor_direction_obj)
    req = request.End(builder)
    builder.Finish(req)

    return builder.Output()

def create_set_motor_direction_response(request_id, driver_type, com_address):
    return create_motor_info_response(request_id, driver_type, com_address)

def create_read_motor_direction_request(request_id, fnid, driver_type, com_address):
    return create_motor_info_request(request_id,fnid,driver_type,com_address)

def create_read_motor_direction_response(request_id, direction, driver_type, com_address):
    builder = flatbuffers.Builder(0)

    motor_basic_info.Start(builder)
    motor_basic_info.AddDriverType(builder, driver_type)
    motor_basic_info.AddComAddress(builder, com_address)
    motor_basic_info_obj = motor_basic_info.End(builder)

    motor_direction.Start(builder)  # Start building the motor_direction object
    motor_direction.AddDirection(builder, direction)  # Add the direction value
    motor_direction.AddMotorInfo(builder, motor_basic_info_obj)  # Add the motor_basic_info object
    motor_direction_obj = motor_direction.End(builder)  # Finalize the motor_direction object

    response.Start(builder)
    response.AddRequestId(builder, request_id)
    response.AddPayloadType(builder, content_payload.content_payload.motor_direction)
    response.AddPayload(builder, motor_direction_obj)
    resp = response.End(builder)
    builder.Finish(resp)

    return builder.Output()

def parse_read_motor_direction_response(response):
    motor_direction_resp = motor_direction.motor_direction()
    motor_direction_resp.Init(response.Payload().Bytes, response.Payload().Pos)
    direction = motor_direction_resp.Direction()

    motor_basic_info_obj = motor_direction_resp.MotorInfo()

    if motor_basic_info_obj is not None:
        # Directly use the fields of the motor_basic_info object
        driver_type = motor_basic_info_obj.DriverType()
        com_address = motor_basic_info_obj.ComAddress()
    else:
        driver_type, com_address = None, None
    request_id = response.RequestId()
    return request_id,direction, driver_type, com_address

def create_motor_control_operation_request(request_id, operation_value, driver_type, com_address):
    builder = flatbuffers.Builder(0)

    motor_basic_info.Start(builder)
    motor_basic_info.AddDriverType(builder, driver_type)
    motor_basic_info.AddComAddress(builder, com_address)
    motor_basic_info_obj = motor_basic_info.End(builder)

    # Start building motor_control_operation
    motor_control_operation.Start(builder)
    motor_control_operation.AddValue(builder, operation_value)  # operation_value is an enum, treated as an integer
    motor_control_operation.AddMotorInfo(builder, motor_basic_info_obj)  # Assuming there's a MotorInfo field
    motor_control_op_obj = motor_control_operation.End(builder)

    # Create the request
    request.Start(builder)
    request.AddRequestId(builder, request_id)
    request.AddFunctionId(builder,
                          function_id.function_id.motor_set_control_operation)  # Adjust based on your function ID
    request.AddPayloadType(builder, content_payload.content_payload.motor_control_operation)
    request.AddPayload(builder, motor_control_op_obj)
    req = request.End(builder)

    # Finish the buffer
    builder.Finish(req)

    # Get the serialized request
    serialized_request = builder.Output()
    return serialized_request

def create_motor_control_operation_response(request_id,com_address,driver_type):
    return create_motor_info_response(request_id,driver_type,com_address)



def create_motor_stats_request(request_id, driver_type, com_address):
    return create_motor_info_request(request_id, function_id.function_id.motor_read_stats, driver_type, com_address)

def create_motor_stats_response(request_id, driver_type, com_address,avg_load, max_load,read_time_speed):
    builder = flatbuffers.Builder(0)

    motor_basic_info.Start(builder)
    motor_basic_info.AddDriverType(builder, driver_type)
    motor_basic_info.AddComAddress(builder, com_address)
    motor_basic_info_obj = motor_basic_info.End(builder)

    # Start building motor_stats
    motor_stats.Start(builder)
    motor_stats.AddAvgLoad(builder, avg_load)  # Add the average load value (float)
    motor_stats.AddMaxLoad(builder, max_load)  # Add the max load value (float)
    motor_stats.AddRealtimeSpeed(builder,read_time_speed)
    motor_stats.AddMotorInfo(builder, motor_basic_info_obj)  # Assuming there's a MotorInfo field
    motor_stats_obj = motor_stats.End(builder)

    # Create the response
    response.Start(builder)
    response.AddRequestId(builder, request_id)
    response.AddPayloadType(builder, content_payload.content_payload.motor_stats)
    response.AddPayload(builder, motor_stats_obj)
    resp = response.End(builder)

    # Finish the buffer
    builder.Finish(resp)

    # Get the serialized response
    serialized_response = builder.Output()
    return serialized_response
def parse_motor_stats_response(response):
    motor_stats_resp = motor_stats.motor_stats()
    motor_stats_resp.Init(response.Payload().Bytes, response.Payload().Pos)
    avg_load = motor_stats_resp.AvgLoad()
    max_load = motor_stats_resp.MaxLoad()
    read_time_speed = motor_stats_resp.RealtimeSpeed()
    motor_basic_info_obj = motor_stats_resp.MotorInfo()

    if motor_basic_info_obj is not None:
        # Directly use the fields of the motor_basic_info object
        driver_type = motor_basic_info_obj.DriverType()
        com_address = motor_basic_info_obj.ComAddress()
    else:
        driver_type, com_address = None, None
    request_id = response.RequestId()
    return request_id,driver_type, com_address,avg_load, max_load,read_time_speed
def create_io_set_status_request(request_id,io_address,io_status,delay_in_ms=-1,lasting_time_in_ms=-1,repeat=-1):
    builder = flatbuffers.Builder(0)



    io_operation.Start(builder)
    io_operation.AddIoAddress(builder, io_address)
    io_operation.AddStatus(builder, io_status)
    io_operation.AddDelayInMs(builder, delay_in_ms)
    io_operation.AddLastingTimeInMs(builder, lasting_time_in_ms)
    io_operation.AddRepeat(builder, repeat)
    io_operation_obj = io_operation.End(builder)


    # Create the request
    request.Start(builder)
    request.AddRequestId(builder, request_id)
    request.AddFunctionId(builder, function_id.function_id.io_set_status)  # Adjust based on your function ID
    request.AddPayloadType(builder, content_payload.content_payload.io_operation)
    request.AddPayload(builder, io_operation_obj)
    req = request.End(builder)

    # Finish the buffer
    builder.Finish(req)

    # Get the serialized request
    serialized_request = builder.Output()
    return serialized_request

def parse_io_set_status_request(request):
    io_operation_req = io_operation.io_operation()
    io_operation_req.Init(request.Payload().Bytes, request.Payload().Pos)
    io_address = io_operation_req.IoAddress()
    io_status = io_operation_req.Status()
    delay_in_ms = io_operation_req.DelayInMs()
    lasting_time_in_ms = io_operation_req.LastingTimeInMs()
    repeat = io_operation_req.Repeat()
    request_id = request.RequestId()
    return request_id, io_address, io_status, delay_in_ms, lasting_time_in_ms, repeat
def create_io_set_status_response(request_id):
    return create_response_with_empty_playload(request_id)

def parse_io_set_status_response(response):
    request_id = response.RequestId()
    return request_id

def create_io_read_status_request(request_id,io_address):
    builder = flatbuffers.Builder(0)

    io_address_long.Start(builder)
    io_address_long.AddValue(builder, io_address)
    io_address_long_obj = io_address_long.End(builder)

    request.Start(builder)
    request.AddRequestId(builder, request_id)
    request.AddFunctionId(builder, function_id.function_id.io_read_status)  # Adjust based on your function ID
    request.AddPayloadType(builder, content_payload.content_payload.io_address_long)
    request.AddPayload(builder, io_address_long_obj)
    req = request.End(builder)

    # Finish the buffer
    builder.Finish(req)

    # Get the serialized request
    serialized_request = builder.Output()
    return serialized_request

def parse_io_read_status_request(request):
    io_address_long_req = io_address_long.io_address_long.GetRootAs(request.Payload().Bytes, request.Payload().Pos)
    io_address = io_address_long_req.Value()
    request_id = request.RequestId()
    return request_id, io_address

def create_io_read_status_response(request_id, io_status_val):
    builder = flatbuffers.Builder(0)

    io_status.Start(builder)
    io_status.AddStatus(builder, io_status_val)
    io_status_obj = io_status.End(builder)

    response.Start(builder)
    response.AddRequestId(builder, request_id)
    response.AddPayloadType(builder, content_payload.content_payload.io_status)
    response.AddPayload(builder, io_status_obj)
    resp = response.End(builder)

    # Finish the buffer
    builder.Finish(resp)

    # Get the serialized response
    serialized_response = builder.Output()
    return serialized_response

def parse_io_read_status_response(response):
    io_status_resp = io_status.io_status()
    io_status_resp.Init(response.Payload().Bytes, response.Payload().Pos)
    io_status_val = io_status_resp.Status()

    request_id = response.RequestId()
    return request_id, io_status_val

def create_io_read_status_batch_request(request_id, io_address_list):
    builder = flatbuffers.Builder(0)

    io_address_long_vector = builder.CreateNumpyVector(np.array(io_address_list, dtype='int64'))

    io_address_batch.Start(builder)
    io_address_batch.AddValues(builder, io_address_long_vector)
    io_address_batch_obj = io_address_batch.End(builder)

    request.Start(builder)
    request.AddRequestId(builder, request_id)
    request.AddFunctionId(builder, function_id.function_id.io_batch_read_status)  # Adjust based on your function ID
    request.AddPayloadType(builder, content_payload.content_payload.io_address_batch)
    request.AddPayload(builder, io_address_batch_obj)
    req = request.End(builder)

    # Finish the buffer
    builder.Finish(req)

    # Get the serialized request
    serialized_request = builder.Output()
    return serialized_request

def parse_io_read_status_batch_request(request):
    io_address_batch_req = io_address_batch.io_address_batch()
    io_address_batch_req.Init(request.Payload().Bytes, request.Payload().Pos)
    io_address_list_length = io_address_batch_req.ValuesLength()
    io_address_list = [io_address_batch_req.Values(i) for i in
                        range(io_address_list_length)]
    request_id = request.RequestId()
    return request_id, io_address_list

def create_io_read_status_batch_response(request_id, io_status_list):
    builder = flatbuffers.Builder(0)

    io_status_vector = builder.CreateNumpyVector(np.array(io_status_list, dtype='bool'))
    io_status_batch.Start(builder)
    io_status_batch.AddValues(builder, io_status_vector)
    io_status_batch_obj = io_status_batch.End(builder)


    response.Start(builder)
    response.AddRequestId(builder, request_id)
    response.AddPayloadType(builder, content_payload.content_payload.io_status_batch)
    response.AddPayload(builder, io_status_batch_obj)
    resp = response.End(builder)

    # Finish the buffer
    builder.Finish(resp)

    # Get the serialized response
    serialized_response = builder.Output()
    return serialized_response

def parse_io_read_status_batch_response(response):
    io_status_batch_resp = io_status_batch.io_status_batch()
    io_status_batch_resp.Init(response.Payload().Bytes, response.Payload().Pos)
    io_status_list_length = io_status_batch_resp.ValuesLength()
    io_status_list = [io_status_batch_resp.Values(i) for i in
                        range(io_status_list_length)]
    request_id = response.RequestId()

    return request_id, io_status_list

def create_io_set_status_batch_request(request_id, io_address_list, io_status_list, delay_in_ms_list, lasting_time_in_ms_list, repeat_list):
    builder = flatbuffers.Builder(0)

    # Pre-serialize each io_operation and collect their offsets
    io_operation_offsets = []
    for io_address, io_status ,delay_in_ms,lasting_time_in_ms ,repeat in zip(io_address_list, io_status_list,delay_in_ms_list, lasting_time_in_ms_list, repeat_list):
        io_operation.Start(builder)
        io_operation.AddIoAddress(builder, io_address)
        io_operation.AddStatus(builder, io_status)
        io_operation.AddDelayInMs(builder, delay_in_ms)
        io_operation.AddLastingTimeInMs(builder, lasting_time_in_ms)
        io_operation.AddRepeat(builder, repeat)
        io_operation_offset = io_operation.End(builder)
        io_operation_offsets.append(io_operation_offset)

    # Create the vector of io_operation offsets
    io_operation_batch.StartValuesVector(builder, len(io_operation_offsets))
    # Add the offsets in reverse order (required by FlatBuffers)
    for offset in reversed(io_operation_offsets):
        builder.PrependUOffsetTRelative(offset)
    values_vector = builder.EndVector(len(io_operation_offsets))

    # Create the io_operation_batch object
    io_operation_batch.Start(builder)
    io_operation_batch.AddValues(builder, values_vector)
    io_operation_batch_obj = io_operation_batch.End(builder)

    request.Start(builder)
    request.AddRequestId(builder, request_id)
    request.AddFunctionId(builder, function_id.function_id.io_batch_set_status)  # Adjust based on your function ID
    request.AddPayloadType(builder, content_payload.content_payload.io_operation_batch)
    request.AddPayload(builder, io_operation_batch_obj)
    req = request.End(builder)

    # Finish the buffer
    builder.Finish(req)

    # Get the serialized request
    serialized_request = builder.Output()
    return serialized_request

def parse_io_set_status_batch_request (request):
    io_operation_batch_req = io_operation_batch.io_operation_batch()
    io_operation_batch_req.Init(request.Payload().Bytes, request.Payload().Pos)
    io_operation_list_length = io_operation_batch_req.ValuesLength()
    io_operation_list = [io_operation_batch_req.Values(i) for i in
                        range(io_operation_list_length)]

    request_id = request.RequestId()
    return request_id, io_operation_list


def create_io_set_status_batch_response(request_id):
    return create_response_with_empty_playload(request_id)
def create_trigger_simulate_request(request_id,simulate_count):
    builder = flatbuffers.Builder(0)

    read_trigger_count.Start(builder)
    read_trigger_count.AddCount(builder, simulate_count)
    read_trigger_count_obj = read_trigger_count.End(builder)

    request.Start(builder)
    request.AddRequestId(builder, request_id)
    request.AddFunctionId(builder, function_id.function_id.trigger_simulate)
    request.AddPayloadType(builder, content_payload.content_payload.read_trigger_count)
    request.AddPayload(builder, read_trigger_count_obj)
    req = request.End(builder)

    # Finish the buffer
    builder.Finish(req)

    # Get the serialized request
    serialized_request = builder.Output()
    return serialized_request

def create_trigger_read_trigger_count_response(request_id, trigger_count):
    builder = flatbuffers.Builder(0)

    read_trigger_count.Start(builder)
    read_trigger_count.AddCount(builder, trigger_count)
    read_trigger_count_obj = read_trigger_count.End(builder)

    response.Start(builder)
    response.AddRequestId(builder, request_id)
    response.AddPayloadType(builder, content_payload.content_payload.read_trigger_count)
    response.AddPayload(builder, read_trigger_count_obj)
    resp = response.End(builder)

    # Finish the buffer
    builder.Finish(resp)

    # Get the serialized response
    serialized_response = builder.Output()
    return serialized_response

def parse_trigger_read_trigger_count_response(response):
    read_trigger_count_resp = read_trigger_count.read_trigger_count()
    read_trigger_count_resp.Init(response.Payload().Bytes, response.Payload().Pos)
    trigger_count = read_trigger_count_resp.Count()

    request_id = response.RequestId()
    return request_id, trigger_count

def create_read_sensor_data_response(request_id, sensor_data_list):
    builder = flatbuffers.Builder(0)
    sensor_data_array = np.array(sensor_data_list)

    sensor_data_vector = builder.CreateNumpyVector(sensor_data_array)

    sensor_data.Start(builder)
    sensor_data.AddSensorDataArray(builder, sensor_data_vector)
    sensor_data_obj = sensor_data.End(builder)

    response.Start(builder)
    response.AddRequestId(builder, request_id)
    response.AddPayloadType(builder, content_payload.content_payload.sensor_data)
    response.AddPayload(builder, sensor_data_obj)
    resp = response.End(builder)

    # Finish the buffer
    builder.Finish(resp)

    # Get the serialized response
    serialized_response = builder.Output()
    return serialized_response

def parse_sensor_read_sensor_response(response):
    sensor_data_resp = sensor_data.sensor_data()
    sensor_data_resp.Init(response.Payload().Bytes, response.Payload().Pos)
    sensor_value = sensor_data_resp.SensorDataArrayAsNumpy()

    request_id = response.RequestId()
    return request_id, sensor_value.tolist()

def create_sensor_set_query_interval_request(request_id,fnid, interval):
    builder = flatbuffers.Builder(0)

    sensor_query_interval.Start(builder)
    sensor_query_interval.AddInterval(builder, interval)
    sensor_query_interval_obj = sensor_query_interval.End(builder)

    request.Start(builder)
    request.AddRequestId(builder, request_id)
    request.AddFunctionId(builder, fnid)
    request.AddPayloadType(builder, content_payload.content_payload.sensor_query_interval)
    request.AddPayload(builder, sensor_query_interval_obj)
    req = request.End(builder)

    # Finish the buffer
    builder.Finish(req)

    # Get the serialized request
    serialized_request = builder.Output()
    return serialized_request

def parse_sensor_set_query_interval_request(request):
    sensor_query_interval_req = sensor_query_interval.sensor_query_interval()
    sensor_query_interval_req.Init(request.Payload().Bytes, request.Payload().Pos)
    interval = sensor_query_interval_req.Interval()

    request_id = request.RequestId()
    return request_id, interval

# table ejector_data {
#   trigger_id: long;
#   group_id: int32;
#   open_status: [bool];
#   delay_time: [uint8];
#   lasting_time: [uint8];
# }
def create_ejector_operation_cmd_request(request_id, trigger_id, group_id, open_status, delay_time, lasting_time):
    builder = flatbuffers.Builder(0)

    open_status_vector = builder.CreateNumpyVector(np.array(open_status, dtype='bool'))
    delay_time_vector = builder.CreateNumpyVector(np.array(delay_time, dtype='uint8'))
    lasting_time_vector = builder.CreateNumpyVector(np.array(lasting_time, dtype='uint8'))


    ejector_data.Start(builder)
    ejector_data.AddTriggerId(builder, trigger_id)
    ejector_data.AddGroupId(builder, group_id)
    ejector_data.AddOpenStatus(builder, open_status_vector)
    ejector_data.AddDelayTime(builder, delay_time_vector)
    ejector_data.AddLastingTime(builder, lasting_time_vector)
    ejector_data_obj = ejector_data.End(builder)

    request.Start(builder)
    request.AddRequestId(builder, request_id)
    request.AddFunctionId(builder, function_id.function_id.ejector_operation_cmd)
    request.AddPayloadType(builder, content_payload.content_payload.ejector_data)
    request.AddPayload(builder, ejector_data_obj)
    req = request.End(builder)

    # Finish the buffer
    builder.Finish(req)

    # Get the serialized request
    serialized_request = builder.Output()
    return serialized_request
