class H5PlayerSplit(object):
    def __self__(self):
        self.name = 'H5'

    def run(self,items):
        flag = False
        for item in items:
            if item['log_id'] == 'LoginRole':
                if item['raw_info']['client_source'] == 'h5':
                    flag = True
        return flag
