from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature
class LogoutRole_onlinetime(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'LogoutRole_onlinetime', 'LogoutRole')

    def __parse__(self, item):
        return item['raw_info']['online_time']

    def __process__(self):
        L = self.L
        return sum(L) if len(L)>0 else None


class LogoutRole_logouttime(Feature):
    def __init__(self):
        Feature.__init__(self, 'LogoutRole_logouttime', 'LogoutRole')

    def __parse__(self, item):
        return item['raw_info']['logout_time']


class LogoutRole_expsum(Feature):
    def __init__(self):
        Feature.__init__(self, 'LogoutRole_expsum', 'LogoutRole')

    def __parse__(self, item):
        return item['raw_info']['exp_sum']
