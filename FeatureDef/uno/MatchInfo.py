from Feature.FeatureCount import FeatureCount


# MatchInfo_freq - 匹配频度（一共参与匹配游戏的次数频度）  MatchInfo
class MatchInfo_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'MatchInfo_freq', 'MatchInfo')


# MatchInfo_timeavg - 平均匹配耗时    MatchInfo  end_match_time-start_match_time
class MatchInfo_timeavg(FeatureCount):
    def __init__(self, name='MatchInfo_timeavg', log='MatchInfo'):
        FeatureCount.__init__(self, name, log)

    def __parse__(self, item):
        return item['raw_info']['end_match_time'] - item['raw_info']['start_match_time']

    def __process__(self):
        L = self.L
        return sum(L) / float(len(L))


# MatchInfo_timemax - 最大匹配耗时
class MatchInfo_timemax(MatchInfo_timeavg):
    def __init__(self):
        MatchInfo_timeavg.__init__(self, 'MatchInfo_timemax', 'MatchInfo')

    def __process__(self):
        return max(self.L)


# MatchInfo_timemin - 最小匹配耗时
class MatchInfo_timemin(MatchInfo_timeavg):
    def __init__(self):
        MatchInfo_timeavg.__init__(self, 'MatchInfo_timemin', 'MatchInfo')

    def __process__(self):
        return min(self.L)
