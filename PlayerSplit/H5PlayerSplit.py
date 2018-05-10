class H5PlayerSplit(object):
    @staticmethod
    def run(items):
        flag = False
        for item in items:
            if item['log_id'] == 'LoginRole':
                if item['raw_info']['client_source'] == 'h5':
                    flag = True
        return flag
