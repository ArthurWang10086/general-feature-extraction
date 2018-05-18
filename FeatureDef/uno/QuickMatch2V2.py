from Feature.FeatureCount import  FeatureCount
from Feature.Feature import Feature
import yaml

# QuickMatch2V2_freq - 2V2参与频度  QuickMatch2V2
class QuickMatch2V2_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'QuickMatch2V2_freq', 'QuickMatch2V2')

class QuickMatch2V2_playtime(Feature):
    def __init__(self):
        Feature.__init__(self, 'QuickMatch2V2_playtime', 'QuickMatch2V2')

    def __parse__(self, item):
        return item['raw_info']['end_time']-item['raw_info']['start_time']

# QuickMatch2V2_winratio - 2V2胜率（所有场次）QuickMatch2V2 role_id == role_id1 or role_id == role_id2 win
class QuickMatch2V2_winratio(FeatureCount):
    def __init__(self, name='QuickMatch2V2_winratio', log='QuickMatch2V2'):
        FeatureCount.__init__(self, name, log)

    def __parse__(self, item):
        from Utils.GlobalVariable import GlobalVariable
        role_id = GlobalVariable.role_id
        if type(item['raw_info']) != str:
            item['raw_info'] = item['raw_info']
        else:
            try:
                item['raw_info'] = yaml.safe_load(item['raw_info'].split('[QuickMatch2V2],')[1])
            except:
                return None
        if role_id == str(item['raw_info']['role_id1']) or role_id == str(item['raw_info']['role_id2']):
            return 1
        else:
            return 0

    def __process__(self):
        L = self.L
        return sum(L[-3:]) / float(len(L[-3:])) if len(L) > 0 else None


# F1QuickMatch2V2_winratio - 2V2胜率（前1场）
class F1QuickMatch2V2_winratio(QuickMatch2V2_winratio):
    def __init__(self):
        QuickMatch2V2_winratio.__init__(self, 'F1QuickMatch2V2_winratio', 'QuickMatch2V2')

    def __process__(self):
        L = self.L
        return sum(L[:1]) / float(len(L[:1])) if len(L) > 0 else None
    # F2QuickMatch2V2_winratio - 2V2胜率（前2场）


class F2QuickMatch2V2_winratio(QuickMatch2V2_winratio):
    def __init__(self):
        QuickMatch2V2_winratio.__init__(self, 'F2QuickMatch2V2_winratio', 'QuickMatch2V2')

    def __process__(self):
        L = self.L
        return sum(L[:2]) / float(len(L[:2])) if len(L) > 0 else None
    # F3QuickMatch2V2_winratio - 2V2胜率（前3场）


class F3QuickMatch2V2_winratio(QuickMatch2V2_winratio):
    def __init__(self):
        QuickMatch2V2_winratio.__init__(self, 'F3QuickMatch2V2_winratio', 'QuickMatch2V2')

    def __process__(self):
        L = self.L
        return sum(L[:3]) / float(len(L[:3])) if len(L) > 0 else None
    # L1QuickMatch2V2_winratio - 2V2胜率（后1场）


class L1QuickMatch2V2_winratio(QuickMatch2V2_winratio):
    def __init__(self):
        QuickMatch2V2_winratio.__init__(self, 'L1QuickMatch2V2_winratio', 'QuickMatch2V2')

    def __process__(self):
        L = self.L
        return sum(L[-1:]) / float(len(L[-1:])) if len(L) > 0 else None
    # L2QuickMatch2V2_winratio - 2V2胜率（后2场）


class L2QuickMatch2V2_winratio(QuickMatch2V2_winratio):
    def __init__(self):
        QuickMatch2V2_winratio.__init__(self, 'L2QuickMatch2V2_winratio', 'QuickMatch2V2')

    def __process__(self):
        L = self.L
        return sum(L[-2:]) / float(len(L[-2:])) if len(L) > 0 else None
    # L3QuickMatch2V2_winratio - 2V2胜率（后3场）


class L3QuickMatch2V2_winratio(QuickMatch2V2_winratio):
    def __init__(self):
        QuickMatch2V2_winratio.__init__(self, 'L3QuickMatch2V2_winratio', 'QuickMatch2V2')

    def __process__(self):
        L = self.L
        return sum(L[-3:]) / float(len(L[-3:])) if len(L) > 0 else None
