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
tag = "Trigger Operations"

# trigger_start_count = 30
# trigger_stop_reset_count = 31
# trigger_simulate = 32
# trigger_read_trigger_count = 33

@router.post("/trigger-start-count", tags=[tag])
async def trigger_start_count(serial_number: Optional[str] = None):
    """
    **Trigger the start of the count.** (触发计数的开始。)
    - **serial_number**: **Optional** serial number of the MCU device. If not provided, the first connected device will be used. (**可选** MCU设备的序列号。如果未提供，将使用第一个连接的设备。)
    - **return**: A JSON object containing the request ID of the trigger start count action. (**返回**：包含触发开始计数操作的请求ID的JSON对象。如果发生错误，则返回一个json错误对象。)
    """
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id = await device_manager.set_trigger_start_count(serial_number)
        result = {"request_id": request_id}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/trigger-stop-reset-count", tags=[tag])
async def trigger_stop_reset_count(serial_number: Optional[str] = None):
    """
    **Trigger the stop and reset of the count.** (触发计数的停止和重置。)
    - **serial_number**: **Optional** serial number of the MCU device. If not provided, the first connected device will be used. (**可选** MCU设备的序列号。如果未提供，将使用第一个连接的设备。)
    - **return**: A JSON object containing the request ID of the trigger stop and reset count action. (**返回**：包含触发停止和重置计数操作的请求ID的JSON对象。如果发生错误，则返回一个json错误对象。)
    """
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id = await device_manager.set_trigger_stop_reset_count(serial_number)
        result = {"request_id": request_id}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/trigger-simulate", tags=[tag])
async def trigger_simulate(serial_number: Optional[str] = None, simulation_count: Optional[int] = 1):
    """
    **Start the simulation mode of the trigger**, under this mode, MCU should automatically simulate the physicial sensor to give the signals. when real trigger signal comes or when stop/reset method is called, it should switch off the simulation mode and resume to normal mode   (启动触发器的模拟模式，在此模式下，MCU应自动模拟物理传感器发出信号。当真实触发信号到来或调用停止/重置方法时，它应切换到模拟模式并恢复到正常模式)
    - **serial_number**: **Optional** serial number of the MCU device. If not provided, the first connected device will be used. (**可选** MCU设备的序列号。如果未提供，将使用第一个连接的设备。)
    - **simulation_count**: **Optional** The count of the simulation. (**可选** 模拟的计数。当给0的时候，则表示一直模拟，直到真实触发信号到来或者调用停止/重置方法。)
    - **return**: A JSON object containing the request ID of the trigger simulate action. (**返回**：包含触发模拟操作的请求ID的JSON对象。如果发生错误，则返回一个json错误对象。)
    """
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id = await device_manager.set_trigger_simulate(serial_number,simulation_count)
        result = {"request_id": request_id}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/trigger-read-trigger-count", tags=[tag])
async def trigger_read_trigger_count(serial_number: Optional[str] = None):
    """
    **Read the current count.** (读取当前计数。)
    - **serial_number**: **Optional** serial number of the MCU device. If not provided, the first connected device will be used. (**可选** MCU设备的序列号。如果未提供，将使用第一个连接的设备。)
    - **return**: A JSON object containing the request ID and the count. (**返回**：包含请求ID和计数的JSON对象。如果发生错误，则返回一个json错误对象。)
    """
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id,trigger_count = await device_manager.read_trigger_count(serial_number) #request_id, trigger_count
        result = {"request_id": request_id,"trigger_count":trigger_count}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))