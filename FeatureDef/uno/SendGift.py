from Feature.FeatureCount import FeatureCount


# SendGift_freq - 发送礼物频度 SendGift
class SendGift_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'SendGift_freq', 'SendGift')


class SendGift_amount(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'SendGift_amount', 'SendGift')

    def __parse__(self, item):
        return item['raw_info']['gift_message']['diamond_use']
