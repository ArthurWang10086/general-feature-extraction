from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature

class SendEmotion_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'SendEmotion_freq', 'SendEmotion')


class SendEmotion_type1(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'SendEmotion_type1', 'SendEmotion')

    def __parse__(self, item):
        return 1 if str(item['raw_info']['emotionType']) == '1' else None


class SendEmotion_type2(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'SendEmotion_type2', 'SendEmotion')

    def __parse__(self, item):
        return 1 if str(item['raw_info']['emotionType']) == '2' else None


class SendEmotion_type3(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'SendEmotion_type3', 'SendEmotion')

    def __parse__(self, item):
        return 1 if str(item['raw_info']['emotionType']) == '3' else None


class SendEmotion_type4(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'SendEmotion_type4', 'SendEmotion')

    def __parse__(self, item):
        return 1 if str(item['raw_info']['emotionType']) == '4' else None


class SendEmotion_time(Feature):
    def __init__(self):
        Feature.__init__(self, 'SendEmotion_time', 'SendEmotion')

    def __parse__(self, item):
        return item['raw_info']['time']
