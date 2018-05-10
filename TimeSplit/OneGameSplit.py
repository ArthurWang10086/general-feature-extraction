class OneGameSplit(object):
    @staticmethod
    def run(items):
        endtime = '2020-01-01 00:00:00'
        count = 0
        for item in items:
            if item['log_id'] == 'MatchInfo':
                count = count + 1
                if count > 1:
                    endtime = item['timestamp']
                    break
        return endtime
