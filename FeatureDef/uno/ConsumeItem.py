from Feature.FeatureCount import FeatureCount

class ConsumeItem_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'ConsumeItem_freq', 'ConsumeItem')
