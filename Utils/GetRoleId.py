def GetRoleId(items):
    role_id = None
    for item in items:
        if item['log_id'] == 'LoginRole':
            role_id = item['raw_info']['role_id']
            break
    return role_id
