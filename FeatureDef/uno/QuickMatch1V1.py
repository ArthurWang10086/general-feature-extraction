from Feature.FeatureCount import FeatureCount
import yaml


# QuickMatch1V1_freq - 1V1参与频度  QuickMatch1V1
class QuickMatch1V1_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'QuickMatch1V1_freq', 'QuickMatch1V1')


# QuickMatch1V1_winratio - 1V1胜率（所有场次） QuickMatch1V1 role_id == role_id1 win
class QuickMatch1V1_winratio(FeatureCount):
    def __init__(self, name='QuickMatch1V1_winratio', log='QuickMatch1V1'):
        FeatureCount.__init__(self, name, log)

    def __parse__(self, item):
        from Utils.GlobalVariable import GlobalVariable
        role_id = GlobalVariable.role_id
        if type(item['raw_info']) != str:
            item['raw_info'] = item['raw_info']
        else:
            try:
                item['raw_info'] = yaml.safe_load(item['raw_info'].split('[QuickMatch1V1],')[1])
            except:
                return None
        if role_id == str(item['raw_info']['role_id1']):
            return 1
        else:
            return 0

    def __process__(self):
        L = self.L
        return sum(L) / float(len(L)) if len(L) > 0 else 0.25

    # F1QuickMatch1V1_winratio - 1V1胜率（前1场） QuickMatch1V1 role_id == role_id1 win


class F1QuickMatch1V1_winratio(QuickMatch1V1_winratio):
    def __init__(self):
        QuickMatch1V1_winratio.__init__(self, 'F1QuickMatch1V1_winratio', 'QuickMatch1V1')

    def __process__(self):
        L = self.L
        return sum(L[:1]) / float(len(L[:1])) if len(L) > 0 else 0.25

    # F2QuickMatch1V1_winratio - 1V1胜率（前2场） QuickMatch1V1 role_id == role_id1 win


class F2QuickMatch1V1_winratio(QuickMatch1V1_winratio):
    def __init__(self):
        QuickMatch1V1_winratio.__init__(self, 'F2QuickMatch1V1_winratio', 'QuickMatch1V1')

    def __process__(self):
        L = self.L
        return sum(L[:2]) / float(len(L[:2])) if len(L) > 0 else 0.25

    # F3QuickMatch1V1_winratio - 1V1胜率（前3场） QuickMatch1V1 role_id == role_id1 win


class F3QuickMatch1V1_winratio(QuickMatch1V1_winratio):
    def __init__(self):
        QuickMatch1V1_winratio.__init__(self, 'F3QuickMatch1V1_winratio', 'QuickMatch1V1')

    def __process__(self):
        L = self.L
        return sum(L[:3]) / float(len(L[:3])) if len(L) > 0 else 0.25

    # L1QuickMatch1V1_winratio - 1V1胜率（后1场） QuickMatch1V1 role_id == role_id1 win


class L1QuickMatch1V1_winratio(QuickMatch1V1_winratio):
    def __init__(self):
        QuickMatch1V1_winratio.__init__(self, 'L1QuickMatch1V1_winratio', 'QuickMatch1V1')

    def __process__(self):
        L = self.L
        return sum(L[-1:]) / float(len(L[-1:])) if len(L) > 0 else 0.25

    # L2QuickMatch1V1_winratio - 1V1胜率（后2场） QuickMatch1V1 role_id == role_id1 win


class L2QuickMatch1V1_winratio(QuickMatch1V1_winratio):
    def __init__(self):
        QuickMatch1V1_winratio.__init__(self, 'L2QuickMatch1V1_winratio', 'QuickMatch1V1')

    def __process__(self):
        L = self.L
        return sum(L[-2:]) / float(len(L[-2:])) if len(L) > 0 else 0.25

    # L3QuickMatch1V1_winratio - 1V1胜率（后3场） QuickMatch1V1 role_id == role_id1 win


class L3QuickMatch1V1_winratio(QuickMatch1V1_winratio):
    def __init__(self):
        QuickMatch1V1_winratio.__init__(self, 'L3QuickMatch1V1_winratio', 'QuickMatch1V1')

    def __process__(self):
        L = self.L
        return sum(L[-3:]) / float(len(L[-3:])) if len(L) > 0 else 0.25

    # QuickMatch1V1_rank - 1V1名次（所有场次） QuickMatch1V1 role_id == role_id1 win


class QuickMatch1V1_rank(FeatureCount):
    def __init__(self, name='QuickMatch1V1_rank', log='QuickMatch1V1'):
        FeatureCount.__init__(self, name, log)

    def __parse__(self, item):
        from Utils.GlobalVariable import GlobalVariable
        role_id = GlobalVariable.role_id
        if type(item['raw_info']) != str:
            item['raw_info'] = item['raw_info']
        else:
            try:
                item['raw_info'] = yaml.safe_load(item['raw_info'].split('[QuickMatch1V1],')[1])
            except:
                return None
        if role_id == str(item['raw_info']['role_id1']):
            return 1
        if role_id == str(item['raw_info']['role_id2']):
            return 2
        if role_id == str(item['raw_info']['role_id3']):
            return 3
        if role_id == str(item['raw_info']['role_id4']):
            return 4
        return 0

    def __process__(self):
        L = self.L
        return sum(L) / float(len(L)) if len(L) > 0 else 2.5

    # F1QuickMatch1V1_rank - 1V1名次（前1场） QuickMatch1V1 role_id == role_id1 win


class F1QuickMatch1V1_rank(QuickMatch1V1_rank):
    def __init__(self):
        QuickMatch1V1_rank.__init__(self, 'F1QuickMatch1V1_rank', 'QuickMatch1V1')

    def __process__(self):
        L = self.L
        return sum(L[:1]) / float(len(L[:1])) if len(L) > 0 else 2.5

    # F2QuickMatch1V1_rank - 1V1名次（前2场） QuickMatch1V1 role_id == role_id1 win


class F2QuickMatch1V1_rank(QuickMatch1V1_rank):
    def __init__(self):
        QuickMatch1V1_rank.__init__(self, 'F2QuickMatch1V1_rank', 'QuickMatch1V1')

    def __process__(self):
        L = self.L
        return sum(L[:2]) / float(len(L[:2])) if len(L) > 0 else 2.5

    # F3QuickMatch1V1_rank - 1V1名次（前3场） QuickMatch1V1 role_id == role_id1 win


class F3QuickMatch1V1_rank(QuickMatch1V1_rank):
    def __init__(self):
        QuickMatch1V1_rank.__init__(self, 'F3QuickMatch1V1_rank', 'QuickMatch1V1')

    def __process__(self):
        L = self.L
        return sum(L[:3]) / float(len(L[:3])) if len(L) > 0 else 2.5

    # L1QuickMatch1V1_rank - 1V1名次（后1场） QuickMatch1V1 role_id == role_id1 win


class L1QuickMatch1V1_rank(QuickMatch1V1_rank):
    def __init__(self):
        QuickMatch1V1_rank.__init__(self, 'L1QuickMatch1V1_rank', 'QuickMatch1V1')

    def __process__(self):
        L = self.L
        return sum(L[-1:]) / float(len(L[-1:])) if len(L) > 0 else 2.5

    # L2QuickMatch1V1_rank - 1V1名次（后2场） QuickMatch1V1 role_id == role_id1 win


class L2QuickMatch1V1_rank(QuickMatch1V1_rank):
    def __init__(self):
        QuickMatch1V1_rank.__init__(self, 'L2QuickMatch1V1_rank', 'QuickMatch1V1')

    def __process__(self):
        L = self.L
        return sum(L[-2:]) / float(len(L[-2:])) if len(L) > 0 else 2.5

    # L3QuickMatch1V1_rank - 1V1名次（后3场） QuickMatch1V1 role_id == role_id1 win


class L3QuickMatch1V1_rank(QuickMatch1V1_rank):
    def __init__(self):
        QuickMatch1V1_rank.__init__(self, 'L3QuickMatch1V1_rank', 'QuickMatch1V1')

    def __process__(self):
        L = self.L
        return sum(L[-3:]) / float(len(L[-3:])) if len(L) > 0 else 2.5
