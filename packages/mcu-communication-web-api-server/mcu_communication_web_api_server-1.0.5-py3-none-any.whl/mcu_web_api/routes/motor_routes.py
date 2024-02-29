from fastapi import APIRouter, Form, HTTPException
from mcu_tcp_impl.server_api import DeviceManager
from typing import Optional
from datetime import datetime
from fastapi import Query
from mcu_web_api import check_default_serial_number
from mcu_functions import functions
from mcu_protocol import motor_operation

router = APIRouter()
device_manager = DeviceManager()
tag = "Motor Operations"
@router.post("/set-realtime-motor-speed", tags=[tag])
async def set_motor_realtime_speed(serial_number: Optional[str] = None, motor_speed: float = 2000, driver_type: int = 0, com_address: int = 0):
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id ,driver_type, com_address = await device_manager.set_motor_speed(serial_number,functions.function_id.function_id.motor_set_speed_real_time, motor_speed, driver_type, com_address)

        result = {"request_id": request_id,"driver_type":driver_type,"com_address":com_address}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/read-realtime-motor-speed", tags=[tag])
async def read_motor_realtime_speed(serial_number: Optional[str] = None, driver_type: int = 0, com_address: int = 0):
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id,speed, driver_type, com_address = await device_manager.read_motor_speed(serial_number,functions.function_id.function_id.motor_read_speed_real_time, driver_type, com_address)
        result = {"request_id": request_id, "speed": speed,"driver_type":driver_type,"com_address":com_address}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set-work-motor-speed", tags=[tag])
async def set_motor_work_speed(serial_number: Optional[str] = None, motor_speed: float = 2000, driver_type: int = 0, com_address: int = 0):
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id ,driver_type, com_address = await device_manager.set_motor_speed(serial_number,functions.function_id.function_id.motor_set_work_speed, motor_speed, driver_type, com_address)

        result = {"request_id": request_id,"driver_type":driver_type,"com_address":com_address}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/read-work-motor-speed", tags=[tag])
async def read_motor_work_speed(serial_number: Optional[str] = None, driver_type: int = 0, com_address: int = 0):
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id,speed, driver_type, com_address = await device_manager.read_motor_speed(serial_number,functions.function_id.function_id.motor_read_work_speed, driver_type, com_address)
        result = {"request_id": request_id, "speed": speed,"driver_type":driver_type,"com_address":com_address}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set-motor-direction", tags=[tag])
async def set_motor_direction(serial_number: Optional[str] = None, direction: bool = True, driver_type: int = 0, com_address: int = 0):
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id ,driver_type, com_address = await device_manager.set_motor_direction(serial_number,functions.function_id.function_id.motor_set_rotation_direction, direction, driver_type, com_address)

        result = {"request_id": request_id,"driver_type":driver_type,"com_address":com_address}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.post("/read-motor-direction", tags=[tag])
async def read_motor_direction(serial_number: Optional[str] = None, driver_type: int = 0, com_address: int = 0):
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id,direction, driver_type, com_address = await device_manager.read_motor_direction(serial_number,functions.function_id.function_id.motor_read_rotation_direction, driver_type, com_address)
        result = {"request_id": request_id, "direction": direction,"driver_type":driver_type,"com_address":com_address}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set-motor-operation", tags=[tag])
async def set_motor_operation(serial_number: Optional[str] = None, operation:int  = motor_operation.motor_operation.step, driver_type: int = 0, com_address: int = 0):
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id ,driver_type, com_address = await device_manager.set_motor_control_operation(serial_number, operation, driver_type, com_address)

        result = {"request_id": request_id,"driver_type":driver_type,"com_address":com_address}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/read-motor-stats", tags=[tag])
async def read_motor_stats(serial_number: Optional[str] = None, driver_type: int = 0, com_address: int = 0):
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id,driver_type, com_address,avg_load, max_load,read_time_speed = await device_manager.read_motor_stats(serial_number, driver_type, com_address)
        result = {"request_id": request_id,"driver_type":driver_type,"com_address":com_address,"avg_load":avg_load,"max_load":max_load,"read_time_speed":read_time_speed}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))