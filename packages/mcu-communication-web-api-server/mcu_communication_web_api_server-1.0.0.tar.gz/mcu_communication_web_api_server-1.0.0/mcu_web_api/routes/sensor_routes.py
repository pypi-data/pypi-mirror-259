from fastapi import APIRouter, Form, HTTPException
from mcu_tcp_impl.server_api import DeviceManager
from typing import Optional
from datetime import datetime
from fastapi import Query
from mcu_web_api import check_default_serial_number
from mcu_functions import functions
from mcu_protocol import function_id
from typing import List, Optional

router = APIRouter()
device_manager = DeviceManager()
tag = "Sensor Operations"

@router.post("/read-temperature-sensor", tags=[tag])
async def read_temperature_sensor(
    serial_number: Optional[str] = Query(None, description="**Optional** The serial number of the temperature sensor. (**可选** 温度传感器的序列号。)")
):
    """
    **Read the temperature from a specific sensor.** (从特定传感器读取温度。)

    This endpoint retrieves the current temperature from a specified sensor.
    (此端点从指定的传感器检索当前温度。)

    - **serial_number**: **Optional** serial number of the temperature sensor. If not provided, the first connected device will be used. (**可选** 温度传感器的序列号。如果未提供，将使用第一个连接的设备。)
    - **return**: A JSON object containing the request ID and the temperature of the specified sensor. (**返回**：包含请求ID和指定传感器的温度的JSON对象。如果发生错误，则返回一个json错误对象。)
    """
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id, sensor_value = await device_manager.read_temperature(serial_number)
        result = {"request_id": request_id, "data": sensor_value}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/read-pressure-sensor", tags=[tag])
async def read_pressure_sensor(
    serial_number: Optional[str] = Query(None, description="**Optional** The serial number of the pressure sensor. (**可选** 压力传感器的序列号。)")
):
    """
    **Read the pressure from a specific sensor.** (从特定传感器读取压力。)

    This endpoint retrieves the current pressure from a specified sensor.
    (此端点从指定的传感器检索当前压力。)

    - **serial_number**: **Optional** serial number of the pressure sensor. If not provided, the first connected device will be used. (**可选** 压力传感器的序列号。如果未提供，将使用第一个连接的设备。)
    - **return**: A JSON object containing the request ID and the pressure of the specified sensor. (**返回**：包含请求ID和指定传感器的压力的JSON对象。如果发生错误，则返回一个json错误对象。)
    """
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id, sensor_value = await device_manager.read_pressure(serial_number)
        result = {"request_id": request_id, "data": sensor_value}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set-temperature-query-interval", tags=[tag])
async def set_temperature_query_interval(
    serial_number: Optional[str] = Query(None, description="**Optional** The serial number of the temperature sensor. (**可选** 温度传感器的序列号。)"),
    interval_in_ms: int = Query(..., description="The interval in milliseconds to query the temperature. (以毫秒为单位查询温度的间隔。)")
):
    """
    **Set the interval to query the temperature.** (设置查询温度的间隔。)

    This endpoint sets the interval in milliseconds to query the temperature from a specified sensor.
    (此端点设置以毫秒为单位从指定传感器查询温度的间隔。)

    - **serial_number**: **Optional** serial number of the temperature sensor. If not provided, the first connected device will be used. (**可选** 温度传感器的序列号。如果未提供，将使用第一个连接的设备。)
    - **interval_in_ms**: The interval in milliseconds to query the temperature. (以毫秒为单位查询温度的间隔。)
    - **return**: A JSON object containing the request ID of the set temperature query interval action. (**返回**：包含设置温度查询间隔操作的请求ID的JSON对象。如果发生错误，则返回一个json错误对象。)
    """
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id = await device_manager.set_temperature_query_interval(serial_number, interval_in_ms)
        result = {"request_id": request_id}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set-pressure-query-interval", tags=[tag])
async def set_pressure_query_interval(
    serial_number: Optional[str] = Query(None, description="**Optional** The serial number of the pressure sensor. (**可选** 压力传感器的序列号。)"),
    interval_in_ms: int = Query(..., description="The interval in milliseconds to query the pressure. (以毫秒为单位查询压力的间隔。)")
):
    """
    **Set the interval to query the pressure.** (设置查询压力的间隔。)

    This endpoint sets the interval in milliseconds to query the pressure from a specified sensor.
    (此端点设置以毫秒为单位从指定传感器查询压力的间隔。)

    - **serial_number**: **Optional** serial number of the pressure sensor. If not provided, the first connected device will be used. (**可选** 压力传感器的序列号。如果未提供，将使用第一个连接的设备。)
    - **interval_in_ms**: The interval in milliseconds to query the pressure. (以毫秒为单位查询压力的间隔。)
    - **return**: A JSON object containing the request ID of the set pressure query interval action. (**返回**：包含设置压力查询间隔操作的请求ID的JSON对象。如果发生错误，则返回一个json错误对象。)
    """
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id = await device_manager.set_pressure_query_interval(serial_number, interval_in_ms)
        result = {"request_id": request_id}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))