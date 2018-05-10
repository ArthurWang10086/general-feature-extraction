from Feature.FeatureCount import FeatureCount


# DailyTaskReward_freq - 每日任务奖励领取频度 DailyTaskReward
class DailyTaskReward_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'DailyTaskReward_freq', 'DailyTaskReward')
