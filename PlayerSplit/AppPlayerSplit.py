class AppPlayerSplit(object):
    def __init__(self):
        self.name = 'app'

    def run(self,items):
        flag = False
        for item in items:
            if item['log_id'] == 'LoginRole':
                if item['raw_info']['client_source'] == 'app':
                    flag = True
        return flag
