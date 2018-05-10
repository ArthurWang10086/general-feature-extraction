from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature

# ReplaceRole_freq -  顶号频度  ReplaceRole
class ReplaceRole_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'ReplaceRole_freq', 'ReplaceRole')


class ReplaceRole_time(Feature):
    def __init__(self):
        Feature.__init__(self, 'ReplaceRole_time', 'ReplaceRole')

    def __parse__(self, item):
        return item['raw_info']['login_time']
