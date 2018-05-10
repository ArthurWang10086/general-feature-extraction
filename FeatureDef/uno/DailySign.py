from Feature.FeatureCount import FeatureCount


# DailySign_freq - 签到频度 DailySign
class DailySign_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'DailySign_freq', 'DailySign')
