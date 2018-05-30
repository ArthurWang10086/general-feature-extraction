class OneGameSplitById(object):

    def run(self,items):
        endtime = '2020-01-01 00:00:00'
        id = 0
        for item in items:
            if item['log_id'] == 'UnoRoomPlayReviewOneLog':
                serialid = int(item['raw_info']['SerialId'])
                if id == 0:
                    id = serialid
                if serialid>0 and serialid != id:
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
