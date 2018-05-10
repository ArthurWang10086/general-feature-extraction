from Feature.FeatureCount import FeatureCount
# DailySignReward_freq - 每日签到奖励领取频度 DailySignReward
class DailySignReward_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'DailySignReward_freq', 'DailySignReward')
