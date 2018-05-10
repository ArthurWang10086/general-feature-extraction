from Feature.FeatureCount import FeatureCount


# DailyTaskFinish_freq - 任务完成频度 DailyTaskFinish
class DailyTaskFinish_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'DailyTaskFinish_freq', 'DailyTaskFinish')
