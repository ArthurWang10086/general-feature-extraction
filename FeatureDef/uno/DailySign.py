from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature

# DailySign_freq - 签到频度 DailySign
class DailySign_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'DailySign_freq', 'DailySign')

class DailySign_time(Feature):
    def __init__(self):
        Feature.__init__(self, 'DailySign_time', 'DailySign')

    def __parse__(self, item):
        return item['timestamp']
