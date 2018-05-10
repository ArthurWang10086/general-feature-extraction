from Feature.FeatureCount import FeatureCount


class DailyReward_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'DailyReward_freq', 'DailyReward')
