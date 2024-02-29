from fastapi import APIRouter, Form, HTTPException
from mcu_tcp_impl.server_api import DeviceManager
from typing import Optional
from datetime import datetime
from fastapi import Query
from mcu_web_api import check_default_serial_number
from mcu_functions import functions
from typing import List, Optional

router = APIRouter()
device_manager = DeviceManager()
tag = "IO Operations"

@router.post("/set-io-status", tags=[tag])
async def set_io_status(
    serial_number: Optional[str] = Query(None, description="**Optional** The serial number of the IO device. (**可选** IO设备的序列号。)"),
    port: int = Query(..., description="The port number to set the status for. (设置状态的端口号。)"),
    status: bool = Query(..., description="The status to set for the specified port. (为指定端口设置的状态。)"),
    delay_in_ms: int = Query(-1, description="Delay before setting the status, in milliseconds. (-1 for disable) (设置状态前的延迟，以毫秒为单位。(-1表示禁用))"),
    lasting_time_in_ms: int = Query(-1, description="How long the status should last, in milliseconds. (-1 for disable) (状态应持续的时间，以毫秒为单位。(-1表示禁用))"),
    repeat: int = Query(-1, description="How many times the action should be repeated. (-1 for disable) (操作应重复的次数。(-1表示禁用))")
):
    """
    **Set the status of a specific IO port.** (设置特定IO端口的状态。)

    This endpoint sets the status (on/off) for a specified port on the IO device. Additional parameters allow for configuring a delay before the action, how long the status should last, and how many times the action should be repeated.
    (此端点为IO设备上的指定端口设置状态（开/关）。额外的参数允许配置操作前的延迟，状态应持续的时间以及操作应重复的次数。)

    - **serial_number**: **Optional** serial number of the IO device. If not provided, the first connected device will be used. (**可选** IO设备的序列号。如果未提供，将使用第一个连接的设备。)
    - **port**: The port number to set the status for. (设置状态的端口号。)
    - **status**: The status to set for the specified port. (为指定端口设置的状态。)
    - **delay_in_ms**: Delay before setting the status, in milliseconds. (-1 for disable) (设置状态前的延迟，以毫秒为单位。(-1表示禁用))
    - **lasting_time_in_ms**: How long the status should last, in milliseconds. (-1 for disable) (状态应持续的时间，以毫秒为单位。(-1表示禁用))
    - **repeat**: How many times the action should be repeated. (-1 for disable) (操作应重复的次数。(-1表示禁用))
    - **return**: A JSON object containing the request ID of the set status action. (**返回**：包含设置状态操作的请求ID的JSON对象。如果发生错误，则返回一个json错误对象。)
    """
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id = await device_manager.set_io_status(serial_number, port, status, delay_in_ms, lasting_time_in_ms, repeat)
        result = {"request_id": request_id}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/read-io-status", tags=[tag])
async def read_io_status(
    serial_number: Optional[str] = Query(None, description="**Optional** The serial number of the IO device. (**可选** IO设备的序列号。)"),
    port: int = Query(..., description="The port number to read the status from. (从中读取状态的端口号。)")
):
    """
    **Read the status of a specific IO port.** (读取特定IO端口的状态。)

    This endpoint retrieves the current status (on/off) of a specified port on the IO device.
    (此端点检索IO设备上指定端口的当前状态（开/关）。)

    - **serial_number**: **Optional** serial number of the IO device. If not provided, the first connected device will be used. (**可选** IO设备的序列号。如果未提供，将使用第一个连接的设备。)
    - **port**: The port number to read the status from. (从中读取状态的端口号。)
    - **return**: A JSON object containing the request ID and the status of the specified port. (**返回**：包含请求ID和指定端口状态的JSON对象。如果发生错误，则返回一个json错误对象。)
    """
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id, status = await device_manager.read_io_status(serial_number, port)
        result = {"request_id": request_id, "status": status}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set-io-batch-status", tags=[tag])
async def set_io_batch_status(
    serial_number: Optional[str] = None,
    io_address_list: List[int] = Query(default=[1, 2, 3]),  # Default list of IO addresses
    io_status_list: List[bool] = Query(default=[True, False, True]),  # Default list of IO statuses
    delay_in_ms_list:  List[int] = Query(default=[1, 2, 3]),
    lasting_time_in_ms_list: List[int] = Query(default=[1, 2, 3]),
    repeat_list: List[int] = Query(default=[1, 2, 3])
):
    """
    **Set the status of multiple IO ports. when used in batch, this api only allow same delay, lasting time and repeat for all ports ** (设置多个IO端口的状态。批量设置的时候，此接口仅提供同样的延迟，持续时间和重复次数。)
    - **serial_number**: **Optional** serial number of the IO device. If not provided, the first connected device will be used. (**可选** IO设备的序列号。如果未提供，将使用第一个连接的设备。)
    - **io_address_list**: A list of IO port addresses to set the status for. (设置状态的IO端口地址列表。)
    - **io_status_list**: A list of status values to set for the specified ports. (为指定端口设置的状态值列表。)
    - **delay_in_ms**: Delay before setting the status, in milliseconds. (-1 for disable) (设置状态前的延迟，以毫秒为单位。(-1表示禁用))
    - **lasting_time_in_ms**: How long the status should last, in milliseconds. (-1 for disable) (状态应持续的时间，以毫秒为单位。(-1表示禁用))
    - **repeat**: How many times the action should be repeated. (-1 for disable) (操作应重复的次数。(-1表示禁用))
    - **return**: A JSON object containing the request ID of the set status action. (**返回**：包含设置状态操作的请求ID的JSON对象。如果发生错误，则返回一个json错误对象。)
    """
    serial_number = check_default_serial_number(serial_number, device_manager)
    if len(io_address_list) != len(io_status_list):
        raise HTTPException(status_code=400, detail="The length of the IO address list and the IO status list must be the same. (IO地址列表和IO状态列表的长度必须相同。)")
    try:
        request_id = await device_manager.set_io_batch_status(serial_number,io_address_list,io_status_list,delay_in_ms_list,lasting_time_in_ms_list,repeat_list )# serial_number,io_address_list,io_status_list,delay_in_ms=-1,lasting_time_in_ms=-1,repeat=-1
        result = {"request_id": request_id}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/read-io-batch-status", tags=[tag])
async def read_io_batch_status(serial_number: Optional[str] = None, io_address_list: List[int] = Query(default=[1, 2, 3])):
    """
    **Read the status of multiple IO ports.** (读取多个IO端口的状态。)
    - **serial_number**: **Optional** serial number of the IO device. If not provided, the first connected device will be used. (**可选** IO设备的序列号。如果未提供，将使用第一个连接的设备。)
    - **io_address_list**: A list of IO port addresses to read the status from. (从中读取状态的IO端口地址列表。)
    - **return**: A JSON object containing the request ID and the status of the specified ports. (**返回**：包含请求ID和指定端口状态的JSON对象。如果发生错误，则返回一个json错误对象。)
    """
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id,status_list = await device_manager.read_io_batch_status(serial_number,io_address_list)
        result = {"request_id": request_id, "status_list": status_list}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))