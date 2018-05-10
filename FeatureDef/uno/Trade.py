from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature
import yaml

class Trade_reason(Feature):
    def __init__(self):
        Feature.__init__(self, 'Trade_reason', 'Trade')

    def __parse__(self, item):
        return item['raw_info']['reason']


# FFirst_Trade_coins_change-Trade gain_count 1v1 reason 1015
class Trade_FFirst_coins_change(FeatureCount):
    def __init__(self, name='Trade_FFirst_coins_change', log='Trade'):
        FeatureCount.__init__(self, name, log)

    def __parse__(self, item):
        if type(item['raw_info']) != str:
            item['raw_info'] = item['raw_info']
        else:
            try:
                item['raw_info'] = yaml.safe_load(item['raw_info'].split('[Trade],')[1])
            except:
                return None
        # 1v1
        if item['raw_info']['reason'] == 1015:
            return item['raw_info']['gain_count']
        else:
            return None

    def __process__(self):
        L=self.L
        return L[0] if len(L) > 0 else None


# FSecond_Trade_coins_change - Trade gain_count 1v1 reason 1015
class Trade_FSecond_coins_change(Trade_FFirst_coins_change):
    def __init__(self):
        Trade_FFirst_coins_change.__init__(self, 'Trade_FSecond_coins_change', 'Trade')

    def __process__(self):
        L=self.L
        return L[1] if len(L) > 1 else None


# FThird_Trade_coins_change - Trade gain_count 1v1 reason 1015
class Trade_FThird_coins_change(Trade_FFirst_coins_change):
    def __init__(self):
        Trade_FFirst_coins_change.__init__(self, 'Trade_FThird_coins_change', 'Trade')

    def __process__(self):
        L=self.L
        return L[2] if len(L) > 2 else None


# LFirst_Trade_coins_change - Trade gain_count 1v1 reason 1015
class Trade_LFirst_coins_change(Trade_FFirst_coins_change):
    def __init__(self):
        Trade_FFirst_coins_change.__init__(self, 'Trade_LFirst_coins_change', 'Trade')

    def __process__(self):
        L=self.L
        return L[-1] if len(L) > 0 else None


# LSecond_Trade_coins_change - Trade gain_count 1v1 reason 1015
class Trade_LSecond_coins_change(Trade_FFirst_coins_change):
    def __init__(self):
        Trade_FFirst_coins_change.__init__(self, 'Trade_LSecond_coins_change', 'Trade')

    def __process__(self):
        L=self.L
        return L[-2] if len(L) > 1 else None


# LThird_Trade_coins_change - Trade gain_count 1v1 reason 1015
class Trade_LThird_coins_change(Trade_FFirst_coins_change):
    def __init__(self):
        Trade_FFirst_coins_change.__init__(self, 'Trade_LThird_coins_change', 'Trade')

    def __process__(self):
        L=self.L
        return L[-3] if len(L) > 2 else None
    # Final_Trade_coins - 最后交易剩余的金币数  Trade CurrentCions


class Trade_Final_coins(Feature):
    def __init__(self):
        Feature.__init__(self, 'Trade_Final_coins', 'Trade')

    def __parse__(self, item):
        if type(item['raw_info']) != str:
            item['raw_info'] = item['raw_info']
        else:
            try:
                item['raw_info'] = yaml.safe_load(item['raw_info'].split('[Trade],')[1])
            except:
                return None
        return item['raw_info']['CurrentCions']
