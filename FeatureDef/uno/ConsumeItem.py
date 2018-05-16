from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature

class ConsumeItem_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'ConsumeItem_freq', 'ConsumeItem')

class ConsumeItem_time(Feature):
    def __init__(self):
        Feature.__init__(self, 'ConsumeItem_time', 'ConsumeItem')

    def __parse__(self, item):
        return item['raw_info']['time']