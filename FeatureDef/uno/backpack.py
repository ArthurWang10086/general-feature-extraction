from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature


# Backpack_freq - 获得道具频度 backpack
class Backpack_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'Backpack_freq', 'backpack')


class Backpack_reason(Feature):
    def __init__(self):
        Feature.__init__(self, 'Backpack_reason', 'backpack')

    def __parse__(self, item):
        return item['raw_info']['item_reason']

class Backpack_time(Feature):
    def __init__(self):
        Feature.__init__(self, 'Backpack_time', 'backpack')

    def __parse__(self, item):
        return item['raw_info']['time']
