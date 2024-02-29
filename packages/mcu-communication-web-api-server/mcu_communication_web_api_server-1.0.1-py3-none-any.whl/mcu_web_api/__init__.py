def check_default_serial_number(serial_number,device_manager):
    if len(device_manager.devices) > 0:
        if serial_number is None:
            serial_number = list(device_manager.devices.keys())[0]
    else:
        raise Exception("No device connected")
    return serial_number