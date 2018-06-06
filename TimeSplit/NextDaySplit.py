import datetime
class NextDaySplit(object):

    def run(self,items):
        endtime = '2020-01-01 00:00:00'
        count = 0
        for item in items:
            if item['log_id'] == 'LoginRole':
                endtime = item['timestamp']
                break
        time = datetime.datetime.strptime(item['timestamp'], "%Y-%m-%d %H:%M:%S")
        return (time+datetime.timedelta(1)).strftime("%Y-%m-%d %H:%M:%S")
