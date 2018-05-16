from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature

# AddAchievement_freq - 成就增加频度 AddAchievement
class AddAchievement_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'AddAchievement_freq', 'AddAchievement')

class AddAchievement_time(Feature):
    def __init__(self):
        Feature.__init__(self, 'AddAchievement_time', 'AddAchievement')

    def __parse__(self, item):
        return item['raw_info']['time']
