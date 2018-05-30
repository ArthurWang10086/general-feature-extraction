class OneGameSplitById(object):

    def run(self,items):
        endtime = '2020-01-01 00:00:00'
        id = 0
        for item in items:
            if item['log_id'] == 'UnoRoomPlayReviewOneLog':
                if id == 0:
                    id = item['SerialId']
                if item['SerialId']>0 and item['SerialId'] != id:
                    endtime = item['timestamp']
                    break

        count = 0
        for item in items:
            if item['log_id'] == 'MatchInfo':
                count = count + 1
                if count > 1:
                    endtime = min(endtime, item['timestamp'])
                    break
        return endtime
