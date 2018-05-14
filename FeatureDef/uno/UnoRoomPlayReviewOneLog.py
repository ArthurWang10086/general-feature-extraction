from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature
import json


class UnoRoomPlayReviewOneLog_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_freq', 'UnoRoomPlayReviewOneLog')


class UnoRoomPlayReviewOneLog_post_freq(FeatureCount):
    def __init__(self, name='UnoRoomPlayReviewOneLog_post_freq', log='UnoRoomPlayReviewOneLog'):
        FeatureCount.__init__(self, name, log)

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            return 1
        else:
            return None


class UnoRoomPlayReviewOneLog_get_freq(FeatureCount):
    def __init__(self, name='UnoRoomPlayReviewOneLog_get_freq', log='UnoRoomPlayReviewOneLog'):
        FeatureCount.__init__(self, name, log)

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1
        else:
            return None


class UnoRoomPlayReviewOneLog_timeover_freq(FeatureCount):
    def __init__(self, name='UnoRoomPlayReviewOneLog_timeover_freq', log='UnoRoomPlayReviewOneLog'):
        FeatureCount.__init__(self, name, log)

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            return 1 if int(json.loads(item['raw_info']['InfoStr'])['UseTime']) >= 10 else 0
        else:
            return None

    def __process__(self):
        return sum(self.L)


class UnoRoomPlayReviewOneLog_timeconsume_average(FeatureCount):
    def __init__(self, name='UnoRoomPlayReviewOneLog_timeconsume_average', log='UnoRoomPlayReviewOneLog'):
        FeatureCount.__init__(self, name, log)

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            return json.loads(item['raw_info']['InfoStr'])['UseTime']
        else:
            return None

    def __process__(self):
        return sum(self.L) / len(self.L)


class UnoRoomPlayReviewOneLog_timeconsume_min(UnoRoomPlayReviewOneLog_timeconsume_average):
    def __init__(self):
        UnoRoomPlayReviewOneLog_timeconsume_average.__init__(self, 'UnoRoomPlayReviewOneLog_timeconsume_min',
                                                             'UnoRoomPlayReviewOneLog')

    def __process__(self):
        return min(self.L)


class UnoRoomPlayReviewOneLog_timeconsume_max(UnoRoomPlayReviewOneLog_timeconsume_average):
    def __init__(self):
        UnoRoomPlayReviewOneLog_timeconsume_average.__init__(self, 'UnoRoomPlayReviewOneLog_timeconsume_max',
                                                             'UnoRoomPlayReviewOneLog')

    def __process__(self):
        return max(self.L)


class UnoRoomPlayReviewOneLog_postmagiccard_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_postmagiccard_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            if str(json.loads(item['raw_info']['InfoStr'])['CardType']) in ['1', '2']:
                return 1
        return None


class UnoRoomPlayReviewOneLog_postpowercard_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_postpowercard_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            if str(json.loads(item['raw_info']['InfoStr'])['CardType'])[-2:] in ['01', '02', '03', '04']:
                return 1
        return None


class UnoRoomPlayReviewOneLog_getmagiccard_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_getmagiccard_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        count = 0
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            D = json.loads(item['raw_info']['InfoStr'])['CardsList']
            for (index, card) in D.items():
                if str(card) in ('1', '2'):
                    count = count + 1
        return count


class UnoRoomPlayReviewOneLog_getpowercard_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_getpowercard_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        count = 0
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            D = json.loads(item['raw_info']['InfoStr'])['CardsList']
            for (index, card) in D.items():
                if str(card)[-2:] in ('01', '02', '03', '04'):
                    count = count + 1
        return count


class UnoRoomPlayReviewOneLog_argue_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_argue_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'SendChallengeWildFourResult':
            return 1
        else:
            return None


class UnoRoomPlayReviewOneLog_arguesuccess_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_arguesuccess_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'SendChallengeWildFourResult':
            return 1 if json.loads(item['raw_info']['InfoStr'])['Result'] else 0
        else:
            return None


class UnoRoomPlayReviewOneLog_arguehappen_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_arguehappen_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'SendChallengeWildFourResult':
            return 1 if json.loads(item['raw_info']['InfoStr'])['IsChallenge'] else 0
        else:
            return None


class UnoRoomPlayReviewOneLog_unomay_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_unomay_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            return 1
        else:
            return None


class UnoRoomPlayReviewOneLog_uno_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_uno_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            return 1 if json.loads(item['raw_info']['InfoStr'])['UnoDeclared'] else 0
        else:
            return None


class UnoRoomPlayReviewOneLog_catchcause_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1
        else:
            return None


class UnoRoomPlayReviewOneLog_catchcause1_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause1_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1 if json.loads(item['raw_info']['InfoStr'])['Cause'] == 1 else 0
        else:
            return None


class UnoRoomPlayReviewOneLog_catchcause2_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause2_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1 if json.loads(item['raw_info']['InfoStr'])['Cause'] == 2 else 0
        else:
            return None


class UnoRoomPlayReviewOneLog_catchcause3_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause3_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1 if json.loads(item['raw_info']['InfoStr'])['Cause'] == 3 else 0
        else:
            return None


class UnoRoomPlayReviewOneLog_catchcause4_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause4_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1 if json.loads(item['raw_info']['InfoStr'])['Cause'] == 4 else 0
        else:
            return None


class UnoRoomPlayReviewOneLog_catchcause5_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause5_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1 if json.loads(item['raw_info']['InfoStr'])['Cause'] == 5 else 0
        else:
            return None


class UnoRoomPlayReviewOneLog_catchcause6_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause6_freq', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1 if json.loads(item['raw_info']['InfoStr'])['Cause'] == 6 else 0
        else:
            return None


class UnoRoomPlayReviewOneLog_forcerule(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_forcerule', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 0 if json.loads(item['raw_info']['InfoStr'])['IsForcePlay'] == 'false' else 1
        else:
            return None


class UnoRoomPlayReviewOneLog_remainnum(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_remainnum', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return json.loads(item['raw_info']['InfoStr'])['RemainNum']
        else:
            return None

    def __process__(self):
        L = self.L
        return L[-1] if len(L) > 0 else None
