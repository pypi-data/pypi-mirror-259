from fastapi import APIRouter, Form, HTTPException
from mcu_tcp_impl.server_api import DeviceManager
from typing import Optional
from datetime import datetime
from fastapi import Query
from mcu_web_api import check_default_serial_number

router = APIRouter()
device_manager = DeviceManager()

@router.get("/available-serial-numbers", tags=["MCU Operations"])
def get_available_serial_numbers():
    # Assuming device_manager.devices is a dict mapping serial numbers to device instances
    available_serial_numbers = list(device_manager.devices.keys())
    return {"available_serial_numbers": available_serial_numbers}

@router.post("/ping", tags=["MCU Operations"])
async def ping(serial_number: Optional[str] = Query(None, description="**Optional** The serial number of the MCU device to ping. (**非必需**MCU设备的序列号。)")):
    """
    Ping an MCU device to check its connectivity. (检查MCU设备的连接性。)

    This endpoint sends a ping request to the specified MCU device and returns a response indicating successful communication. If no serial number is provided, the system will attempt to ping the first device it finds.
    (此端点向指定的MCU设备发送ping请求，并返回指示成功通信的响应。如果未提供序列号，系统将尝试ping找到的第一个设备。)

    - **serial_number**: **Optional** serial number of the MCU device to ping. (**非必填**MCU设备的序列号。如果不填写，将使用连接的第一个设备（通常情况下，我们只会连接一个MCU设备，因此默认缺省的时候，就是给这个设备发送），如果没有连接的设备，将返回错误。)
    - **return**: A JSON object containing the request ID of the ping request (**返回**：包含ping请求的请求ID的JSON对象。.如果发生错误，则返回一个json错误对象)
    """
    try:
        serial_number = check_default_serial_number(serial_number,device_manager)
        response = await device_manager.ping(serial_number)
        result = {"request_id": response}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set-meta-info", tags=["MCU Operations"])
async def set_meta_info(
    serial_number: Optional[str] = None,
    row: int = Form(8),
    column: int = Form(16),
    ejection_delay: str = Form("15,15,15,15,15,15,15,15"),  # Received as comma-separated string
    ejection_lasting: str = Form("15,15,15,15,15,15,15,15"),  # Received as comma-separated string
    port_drive_mapping: str = Form("1,2,3,4,5,6,7,8")  # Received as comma-separated string
):
    serial_number = check_default_serial_number(serial_number,device_manager)
    try:
        # Convert comma-separated strings to lists of integers
        ejection_delay_list = [int(x) for x in ejection_delay.split(',')]
        ejection_lasting_list = [int(x) for x in ejection_lasting.split(',')]
        port_drive_mapping_list = [int(x) for x in port_drive_mapping.split(',')]



        # Pass the parameters to your device_manager method
        response = await device_manager.set_meta_info(serial_number, row, column, ejection_delay_list, ejection_lasting_list, port_drive_mapping_list)
        result = {"request_id": response}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/read-meta-info", tags=["MCU Operations"])
async def read_meta_info(serial_number: Optional[str] = None):
    serial_number = check_default_serial_number(serial_number,device_manager)
    try:
        request_id,row, column, ejection_delay, ejection_lasting, port_drive_mapping = await device_manager.read_meta_info(serial_number)
        result = {
            "request_id": request_id,
            "row": row,
            "column": column,
            "ejection_delay": ejection_delay,
            "ejection_lasting": ejection_lasting,
            "port_drive_mapping": port_drive_mapping
        }
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.post("/set_authorization_date", tags=["MCU Operations"])
async def set_authorization_date(serial_number: Optional[str] = None,authorization_date: str = Form("2021-05-01")):
    serial_number = check_default_serial_number(serial_number,device_manager)
    try:
        # Parse the date string into a datetime object
        date_obj = datetime.strptime(authorization_date, "%Y-%m-%d")
        # Convert the datetime object to a Unix timestamp (in seconds)
        timestamp_seconds = datetime.timestamp(date_obj)
        # Convert the timestamp to milliseconds
        timestamp_milliseconds = int(timestamp_seconds * 1000)
        response = await device_manager.set_authorization_date(serial_number, timestamp_milliseconds)
        result = {"request_id": response}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.post("/read_authorization_date", tags=["MCU Operations"])
async def read_authorization_date(serial_number: Optional[str] = None):
    serial_number = check_default_serial_number(serial_number,device_manager)
    try:

        request_id,timestamp  = await device_manager.read_authorization_date(serial_number)
        result = {"request_id": request_id, "timestamp": timestamp}

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_last_usage_time", tags=["MCU Operations"])
async def set_last_usage_time(serial_number: Optional[str] = None,last_usage_time: str = Form("2021-05-01")):
    serial_number = check_default_serial_number(serial_number,device_manager)
    try:
        # Parse the date string into a datetime object
        date_obj = datetime.strptime(last_usage_time, "%Y-%m-%d")
        # Convert the datetime object to a Unix timestamp (in seconds)
        timestamp_seconds = datetime.timestamp(date_obj)
        # Convert the timestamp to milliseconds
        timestamp_milliseconds = int(timestamp_seconds * 1000)
        response = await device_manager.set_last_usage_time(serial_number, timestamp_milliseconds)
        result = {"request_id": response}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/read_last_usage_time", tags=["MCU Operations"])
async def read_last_usage_time(serial_number: Optional[str] = None):
    serial_number = check_default_serial_number(serial_number,device_manager)
    try:
        request_id,timestamp  = await device_manager.read_last_usage_time(serial_number)
        result = {"request_id": request_id,"timestamp":timestamp}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/read_run_time", tags=["MCU Operations"])
async def read_run_time(serial_number: Optional[str] = None):
    serial_number = check_default_serial_number(serial_number,device_manager)
    try:
        request_id,timestamp = await device_manager.read_run_time(serial_number)
        result = {"request_id": request_id,"timestamp":timestamp}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))