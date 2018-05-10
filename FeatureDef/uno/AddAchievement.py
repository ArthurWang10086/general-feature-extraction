from Feature.FeatureCount import FeatureCount


# AddAchievement_freq - 成就增加频度 AddAchievement
class AddAchievement_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'AddAchievement_freq', 'AddAchievement')
