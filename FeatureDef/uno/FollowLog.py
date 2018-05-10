from Feature.FeatureCount import FeatureCount


# FollowLog_freq - 添加关注好友频度 FollowLog
class FollowLog_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'FollowLog_freq', 'FollowLog')
