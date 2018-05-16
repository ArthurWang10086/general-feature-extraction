from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature
# DailySignReward_freq - 每日签到奖励领取频度 DailySignReward
class DailySignReward_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'DailySignReward_freq', 'DailySignReward')

class DailySignReward_time(Feature):
    def __init__(self):
        Feature.__init__(self, 'DailySignReward_time', 'DailySignReward')

    def __parse__(self, item):
        return item['raw_info']['rewardtime']
