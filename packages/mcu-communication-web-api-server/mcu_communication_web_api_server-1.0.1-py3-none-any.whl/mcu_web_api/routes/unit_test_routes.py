from fastapi import APIRouter, Form, HTTPException
from mcu_tcp_impl.server_api import DeviceManager
from typing import Optional
from datetime import datetime
from fastapi import Query
from mcu_web_api import check_default_serial_number
from mcu_functions import functions
from mcu_protocol import function_id
from typing import List, Optional
from enum import Enum
from fastapi import HTTPException, Query, APIRouter, BackgroundTasks
from fastapi.responses import StreamingResponse
from typing import Optional, Iterator
import time
import json
import logging


router = APIRouter()
device_manager = DeviceManager()
tag = "Unit Test Operations"


@router.post("/upper_startup_senario", tags=[tag])
async def upper_startup_senario():
    """
    **Upper startup senario.** (上位机启动场景。)
    turn**: A JSON object containing the request ID of the upper startup senario action. (**返回**：包含上位机启动场景操作的请求ID的JSON对象。如果发生错误，则返回一个json错误对象。)
    """
    serial_number = available_serial_number = list(device_manager.devices.keys())[0]
    if serial_number is None:
        raise HTTPException(status_code=500, detail="No device connected.")
    try:
        #authenticating the device
        request_id1 ,auth_timestamp = await device_manager.read_authorization_date(serial_number)
        requestid2,last_usage_timestamp = await device_manager.read_last_usage_time(serial_number)
        request_id3,row, column, ejection_delay, ejection_lasting, port_drive_mapping = await device_manager.read_meta_info(serial_number)
        request_id4,lower_up_timestamp = await device_manager.read_run_time(serial_number)
        request_ids = [request_id1,requestid2,request_id3,request_id4]
        result = {"request_ids": request_ids,"auth_timestamp":auth_timestamp,"last_usage_timestamp":last_usage_timestamp,"meta_info":[row, column, ejection_delay, ejection_lasting, port_drive_mapping],"lower_up_timestamp":lower_up_timestamp}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class DeviceModel(str,Enum):
    v12 = "12"
    v16 = "16"
    v20 = "20"
    v24 = "24"
    v30 = "30"


class ExitCount(str,Enum):
    C7 = "7"
    C8 = "8"
    C9 = "9"
    C10 = "10"
    C24 = "24"

class MOTOR_OPTIONS (str,Enum):
    不需要NO_NEED= "0不需要NO_NEED"
    台达Delta= "1台达Delta"
    禾川HECHUAN= "2禾川HECHUAN"
    STEPMotor= "3STEPMotor"
    SIMENTVFD= "4SIMENTVFD"

class MODBUS_TARGET (str,Enum):
    TARGET_1: "1"
    TARGET_2: "2"



@router.post("/setup_senario", tags=[tag])
async def mcu_setup_senario(
                            serial_number: Optional[str] = Query(None, description="**Optional** The serial number of the ejector device. (**可选** 设备的序列号。)"),
                            device_type_model: DeviceModel = Query(..., description="**Required** Machine Model. (**必选** 机器型号。)") , # Make this required
                            exit_count_model: ExitCount = Query(...,description="**Required** Exit Count. (**必选** 出料口数量。)"),
                            main_motor_model: int = Query(...,description="**Required** Main Motor Type. (**必选** 主电机类型。)"),
                            rolling_motor_model: int = Query(...,description="**Required** Rolling Motor Type. (**必选** 同步带滚动电机类型。)"),
                            lifting_motor_model: int = Query(...,description="**Required** Lifting Motor Type. (**必选** 上料电机类型。)"),
                            ejection_delay: str = Query("15,15,15,15,15,15,15,15"),  # Received as comma-separated string
                            ejection_lasting: str = Query("15,15,15,15,15,15,15,15"),  # Received as comma-separated string
                            sensor_query_interval_in_ms: int = Query(default=5000,description="**Required** Sensor Query Interval in milliseconds. (**必选** 传感器查询间隔时间。)"),
                            default_main_motor_work_speed:int = Query(default=2200,description="**Required** Default Main Motor Workspeed. (**必选** 默认主电机工作速度。)"),
                            default_rolling_motor_work_speed:int = Query(default=1750,description="**Required** Default Rolling Motor Workspeed. (**必选** 默认同步带滚动电机工作速度。)"),
                            default_lifting_motor_works_peed:int = Query(default=50,description="**Required** Default Lifting Motor Workspeed. (**必选** 默认上料电机工作速度。)"),

):
    serial_number = check_default_serial_number(serial_number, device_manager)
    device_model_type_value = int(device_type_model.value)
    exit_count_value = int(exit_count_model.value)
    main_motor_model_value = main_motor_model
    rolling_motor_model_value = rolling_motor_model
    lifting_motor_model_value = lifting_motor_model

    row = exit_count_value
    column = device_model_type_value
    port_drive_mapping_list = [main_motor_model_value,rolling_motor_model_value,lifting_motor_model_value]
    ejection_delay_list = [int(x) for x in ejection_delay.split(',')]
    ejection_lasting_list = [int(x) for x in ejection_lasting.split(',')]

    try:
        start_time = time.time()
        meta_info_request_id = await device_manager.set_meta_info(serial_number, row, column, ejection_delay_list, ejection_lasting_list, port_drive_mapping_list)
        end_time = time.time()
        meta_info_duration = (end_time - start_time) * 1000

        start_time = time.time()
        temperture_sensor_query_interval_request_id = await device_manager.set_temperature_query_interval(serial_number, sensor_query_interval_in_ms)
        end_time = time.time()
        temperture_sensor_query_interval_duration = (end_time - start_time) * 1000

        start_time = time.time()
        pressure_sensor_query_interval_request_id = await device_manager.set_pressure_query_interval(serial_number, sensor_query_interval_in_ms)
        end_time = time.time()
        pressure_sensor_query_interval_duration = (end_time - start_time) * 1000

        start_time = time.time()
        default_main_motor_work_speed_request_id,default_main_motor_work_speed_driver_type, default_main_motor_work_speed_com_address = await device_manager.set_motor_speed(serial_number,function_id.function_id.motor_set_work_speed, default_main_motor_work_speed,main_motor_model_value,1)
        end_time = time.time()
        default_main_motor_work_speed_duration = (end_time - start_time) * 1000
        start_time = time.time()
        default_rolling_motor_work_speed_request_id,default_rolling_motor_work_speed_driver_type, default_rolling_motor_work_speed_com_address = await device_manager.set_motor_speed(serial_number,function_id.function_id.motor_set_work_speed, default_rolling_motor_work_speed,rolling_motor_model_value,2)
        end_time = time.time()
        default_rolling_motor_work_speed_duration = (end_time - start_time) * 1000
        start_time = time.time()
        default_lifting_motor_work_speed_request_id ,default_lifting_motor_work_speed_driver_type, default_lifting_motor_work_speed_com_address= await device_manager.set_motor_speed(serial_number,function_id.function_id.motor_set_work_speed, default_lifting_motor_works_peed,lifting_motor_model_value,1)
        end_time = time.time()
        default_lifting_motor_work_speed_duration = (end_time - start_time) * 1000
        result = {"meta_info_request_id": meta_info_request_id,
                  "temperture_sensor_query_interval_request_id":temperture_sensor_query_interval_request_id,
                  "pressure_sensor_query_interval_request_id":pressure_sensor_query_interval_request_id,
                  "default_main_motor_work_speed_request_id":default_main_motor_work_speed_request_id,
                  "default_main_motor_work_speed_driver_type":default_main_motor_work_speed_driver_type,
                    "default_main_motor_work_speed_com_address":default_main_motor_work_speed_com_address,
                  "default_rolling_motor_work_speed_request_id":default_rolling_motor_work_speed_request_id,
                    "default_rolling_motor_work_speed_driver_type":default_rolling_motor_work_speed_driver_type,
                    "default_rolling_motor_work_speed_com_address":default_rolling_motor_work_speed_com_address,
                  "default_lifting_motor_work_speed_request_id":default_lifting_motor_work_speed_request_id,
                  "default_lifting_motor_work_speed_driver_type":default_lifting_motor_work_speed_driver_type,
                    "default_lifting_motor_work_speed_com_address":default_lifting_motor_work_speed_com_address,
                    "meta_info_duration_ms": meta_info_duration,
                    "temperture_sensor_query_interval_duration_ms": temperture_sensor_query_interval_duration,
                    "pressure_sensor_query_interval_duration_ms": pressure_sensor_query_interval_duration,
                    "default_main_motor_work_speed_duration_ms": default_main_motor_work_speed_duration,
                    "default_rolling_motor_work_speed_duration_ms": default_rolling_motor_work_speed_duration,
                    "default_lifting_motor_work_speed_duration_ms": default_lifting_motor_work_speed_duration

                  }
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

import time
from fastapi import HTTPException, Query
from typing import Optional


def simulate_ejector_operation( serial_number, iteration_count, iteration_interval_in_ms):
    request_ids = []
    durations = []

    async def generate():
        for i in range(iteration_count):
            start_time = time.time()
            request_id = await device_manager.ejector_operation_cmd(serial_number, i, i % 8, [True, True, True, False, False, False, True, False], [i % 1, i % 2, i % 3, i % 4, i % 5, i % 6, i % 7, i % 8], [i % 1, i % 2, i % 3, i % 4, i % 5, i % 6, i % 7, i % 8])
            end_time = time.time()
            duration = (end_time - start_time) * 1000

            request_ids.append(request_id)
            durations.append(duration)

            avg_duration = sum(durations) / len(durations)

            result = {
                "iteration": i + 1,
                "request_id": request_id,
                "duration_ms": duration,
                "max_duration_ms": max(durations),
                "min_duration_ms": min(durations),
                "cumulative_avg_duration_ms": avg_duration
            }

            yield json.dumps(result) + "\n"  # Convert dict to JSON string and add newline

            #time.sleep(iteration_interval_in_ms / 1000.0)  # Sleep for the specified interval

    return generate  # Return the generator function

@router.post("/simulate_ejector_operation_cmd_stream", tags=[tag])
async def simulate_ejector_operation_cmd(
    background_tasks: BackgroundTasks,
    serial_number: Optional[str] = Query(None, description="**Optional** The serial number of the ejector device."),
    iteration_count: int = Query(..., description="The number of iterations for the ejector operation."),
    iteration_interval_in_ms: int = Query(default=1000, description="**Required** Iteration Interval in milliseconds.")
):
    serial_number = check_default_serial_number(serial_number, device_manager)
    generator = simulate_ejector_operation(serial_number, iteration_count, iteration_interval_in_ms)  # Mocking device_manager for this example

    return StreamingResponse(generator(), media_type="text/plain")

@router.post("/simulate_ejector_operation_cmd_complete_return", tags=[tag])
async def simulate_ejector_operation_cmd_complete_return(
    serial_number: Optional[str] = Query(None, description="**Optional** The serial number of the ejector device."),
    iteration_count: int = Query(default=300, description="The number of iterations for the ejector operation."),
):
    serial_number = check_default_serial_number(serial_number, device_manager)
    request_ids = []
    durations = []

    for i in range(iteration_count):
        start_time = time.time()
        request_id = await device_manager.ejector_operation_cmd(serial_number, i, i % 8, [True, True, True, False, False, False, True, False], [i % 1, i % 2, i % 3, i % 4, i % 5, i % 6, i % 7, i % 8], [i % 1, i % 2, i % 3, i % 4, i % 5, i % 6, i % 7, i % 8])
        end_time = time.time()
        duration = (end_time - start_time) * 1000

        request_ids.append(request_id)
        durations.append(duration)

    avg_duration = sum(durations) / len(durations)

    result = {
        "request_ids_len": len(request_ids),
        "max_duration_ms": max(durations),
        "min_duration_ms": min(durations),
        "avg_duration_ms": avg_duration
    }

    return result

@router.post("/round_trip_time_taken_test", tags=[tag])
async def round_trip_time_taken_test(
    serial_number: Optional[str] = Query(None, description="**Optional** The serial number of the ejector device."),
    iteration_count: int = Query(default=300, description="The number of iterations for the ejector operation."),
):
    serial_number = check_default_serial_number(serial_number, device_manager)
    request_ids = []
    durations = []

    for i in range(iteration_count):
        start_time = time.time()
        request_id = await device_manager.ping(serial_number)
        end_time = time.time()
        duration = (end_time - start_time) * 1000

        request_ids.append(request_id)
        durations.append(duration)

    avg_duration = sum(durations) / len(durations)

    result = {
        "request_ids_len": len(request_ids),
        "max_duration_ms": max(durations),
        "min_duration_ms": min(durations),
        "avg_duration_ms": avg_duration
    }

    return result

@router.post("/avg_response_stats_from_tcp_server", tags=[tag])
async def avg_response_stats_from_tcp_server():
    avg_response_time, total_response_count = device_manager.average_response_stats
    result = {"avg_response_time_ms": avg_response_time, "total_response_count": total_response_count}
    return result
@router.post("/round_trip_time_taken_test_read_time_from_client", tags=[tag])
async def round_trip_time_taken_test_read_time_from_client(
    serial_number: Optional[str] = Query(None, description="**Optional** The serial number of the ejector device."),
    iteration_count: int = Query(default=300, description="The number of iterations for the ejector operation."),
):
    serial_number = check_default_serial_number(serial_number, device_manager)
    request_ids = []
    durations = []
    server2client_duration = []
    client2server_duration = []

    for i in range(iteration_count):
        start_time = time.time()*1000
        #logging.info(f"start_time: {start_time}")
        request_id ,unix_time_stamp_resp_value= await device_manager.read_run_time(serial_number)
        end_time = time.time()*1000
        #logging.info(f"end_time: {end_time}")
        duration = (end_time - start_time)
        server2client = unix_time_stamp_resp_value - start_time
        client2server = end_time - unix_time_stamp_resp_value
        #logging.info(f"server2client: {server2client}")
        #logging.info(f"client2server: {client2server}")
        server2client_duration.append(server2client)
        client2server_duration.append(client2server)
        request_ids.append(request_id)
        durations.append(duration)

    avg_duration = sum(durations) / len(durations)
    avg_server2client_duration = sum(server2client_duration) / len(server2client_duration)
    avg_client2server_duration = sum(client2server_duration) / len(client2server_duration)

    result = {"total":{
                        "request_ids_len": len(request_ids),
                        "max_duration_ms": max(durations),
                        "min_duration_ms": min(durations),
                        "avg_duration_ms": avg_duration,
                    },
            "server2client":{
                        "max_duration_ms": max(server2client_duration),
                        "min_duration_ms": min(server2client_duration),
                        "avg_duration_ms": avg_server2client_duration,
                    },
            "client2server":{
                        "max_duration_ms": max(client2server_duration),
                        "min_duration_ms": min(client2server_duration),
                        "avg_duration_ms": avg_client2server_duration,
                    }

    }

    return result