from Feature.FeatureCount import  FeatureCount


# PraisePlayRound_freq - 给他人点赞频度 PraisePlayRound
class PraisePlayRound_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'PraisePlayRound_freq', 'PraisePlayRound')
