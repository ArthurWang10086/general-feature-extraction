class ThreeGameSplit(object):

    def run(self,items):
        endtime = '2020-01-01 00:00:00'
        count = 0
        for item in items:
            if item['log_id'] in ['QuickMatch1V1','QuickMatch2V2']:
                count = count + 1
                if count > 2:
                    endtime = item['timestamp']
                    break
        return endtime
