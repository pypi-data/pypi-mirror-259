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
tag = "Ejector Operations"

# def ejector_operation_cmd(self, serial_number, trigger_id,group_id,open_status_list,delay_time_list,last_time_list):
@router.post("/ejector-operation-cmd", tags=[tag])
async def ejector_operation_cmd(
    serial_number: Optional[str] = Query(None, description="**Optional** The serial number of the ejector device. (**可选** 射针设备的序列号。)"),
    trigger_id: int = Query(..., description="The trigger ID for the ejector operation. (射针操作的触发器ID。)"),
    group_id: int = Query(..., description="The group ID for the ejector operation. (射针操作的组ID。)"),
    open_status_list: List[bool] = Query(default=[True, True, True, False, False, False, True, False],
                                         description="The list of open status for each ejector. (每个射针的开启状态列表。)"),
    delay_time_list: List[int] = Query(default=[10, 10, 10, 10, 15, 15, 15, 15],
                                       description="The list of delay time for each ejector, in milliseconds. (每个射针的延迟时间列表，以毫秒为单位。)"),
    lasting_time_list: List[int] = Query(default=[10, 10, 10, 10, 15, 15, 15, 15],
                                      description="The list of lasting time for each ejector, in milliseconds. (每个射针的持续时间列表，以毫秒为单位。)")
):
    """
    **Send the ejector operation command to the MCU.** (向MCU发送射针操作命令。)

    This endpoint sends the ejector operation command to the MCU. The command includes the trigger ID, group ID, open status for each ejector, delay time for each ejector, and lasting time for each ejector.
    (此端点向MCU发送射针操作命令。命令包括触发器ID，组ID，每个射针的开启状态，每个射针的延迟时间和每个射针的持续时间。)

    - **serial_number**: **Optional** serial number of the ejector device. If not provided, the first connected device will be used. (**可选** 射针设备的序列号。如果未提供，将使用第一个连接的设备。)
    - **trigger_id**: The trigger ID for the ejector operation. (射针操作的触发器ID。)
    - **group_id**: The group ID for the ejector operation. (射针操作的组ID。)
    - **open_status_list**: The list of open status for each ejector. (每个射针的开启状态列表。)
    - **delay_time_list**: The list of delay time for each ejector, in milliseconds. (每个射针的延迟时间列表，以毫秒为单位。)
    - **last_time_list**: The list of lasting time for each ejector, in milliseconds. (每个射针的持续时间列表，以毫秒为单位。)
    - **return**: A JSON object containing the request ID of the ejector operation command. (**返回**：包含射针操作命令的请求ID的JSON对象。如果发生错误，则返回一个json错误对象。)
    """
    serial_number = check_default_serial_number(serial_number, device_manager)
    try:
        request_id = await device_manager.ejector_operation_cmd(serial_number, trigger_id, group_id, open_status_list, delay_time_list, lasting_time_list)
        result = {"request_id": request_id}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
