from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature

class RoomModeCreate_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'RoomModeCreate_freq', 'RoomModeCreate')


class RoomModeCreate_mode(Feature):
    def __init__(self):
        Feature.__init__(self, 'RoomModeCreate_mode', 'RoomModeCreate')

    def __parse__(self, item):
        return item['raw_info']['mode']
