from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature


class AdsLog_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'AdsLog_freq', 'AdsLog')


class AdsLog_type(Feature):
    def __init__(self):
        Feature.__init__(self, 'AdsLog_type', 'AdsLog')

    def __parse__(self, item):
        return item['raw_info']['type']


class AdsLog_addtime(Feature):
    def __init__(self):
        Feature.__init__(self, 'AdsLog_addtime', 'AdsLog')

    def __parse__(self, item):
        return item['raw_info']['addtime']
