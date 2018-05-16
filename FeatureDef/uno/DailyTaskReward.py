from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature

# DailyTaskReward_freq - 每日任务奖励领取频度 DailyTaskReward
class DailyTaskReward_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'DailyTaskReward_freq', 'DailyTaskReward')

class DailyTaskReward_time(Feature):
    def __init__(self):
        Feature.__init__(self, 'DailyTaskReward_time', 'DailyTaskReward')

    def __parse__(self, item):
        return item['raw_info']['rewardtime']
