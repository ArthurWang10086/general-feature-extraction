import json
def GetSerialId(items):
    serial_id = None
    for item in items:
        if item['log_id'] == 'UnoRoomPlayReviewOneLog':
            serial_id = item['raw_info']['SerialId']
            return serial_id
    for item in items:
        if item['log_id'] == 'MatchInfo':
            serial_id = item['raw_info']['SerialId']
            return serial_id
    return '-1'
