from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature
import datetime
import time
# DailySign_freq - 签到频度 DailySign
class DailySign_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'DailySign_freq', 'DailySign')

class DailySign_time(Feature):
    def __init__(self):
        Feature.__init__(self, 'DailySign_time', 'DailySign')

    def datetime_timestamp(self,dt):
        time.strptime(dt,'%Y-%m-%d %H:%M:%S')
        s = time.mktime(time.strptime(dt,'%Y-%m-%d %H:%M:%S'))
        return s

    def __parse__(self, item):
        return int(self.datetime_timestamp(item['timestamp']))
