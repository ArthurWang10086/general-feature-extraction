from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature

class DailyReward_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'DailyReward_freq', 'DailyReward')

class DailyReward_time(Feature):
    def __init__(self):
        Feature.__init__(self, 'DailyReward_time', 'DailyReward')

    def __parse__(self, item):
        return item['raw_info']['rewardtime']