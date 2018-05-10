from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature

class ShareLog_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'ShareLog_freq', 'ShareLog')
