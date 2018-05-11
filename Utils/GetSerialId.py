def GetSerialId(items):
    serial_id = None
    for item in items:
        if item['log_id'] == 'UnoRoomPlayReviewOneLog':
            serial_id = item['raw_info']['SerialId']
            break
    return serial_id
