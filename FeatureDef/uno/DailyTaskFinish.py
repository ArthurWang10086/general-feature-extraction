from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature

# DailyTaskFinish_freq - 任务完成频度 DailyTaskFinish
class DailyTaskFinish_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'DailyTaskFinish_freq', 'DailyTaskFinish')

class DailyTaskFinish_time(Feature):
    def __init__(self):
        Feature.__init__(self, 'DailyTaskFinish_time', 'DailyTaskFinish')

    def __parse__(self, item):
        return item['raw_info']['finishtime']
