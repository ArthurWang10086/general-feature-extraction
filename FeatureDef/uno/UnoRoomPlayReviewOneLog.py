from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature
import json


class UnoRoomPlayReviewOneLog_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_freq', 'UnoRoomPlayReviewOneLog')

class UnoRoomPlayReviewOneLog_init(Feature):
    def __init__(self):
        Feature.__init__(self, 'UnoRoomPlayReviewOneLog_init', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'StartUnoPlayOne':
            return len(json.loads(item['raw_info']['Info'])['CardList'])
        else:
            return None

class UnoRoomPlayReviewOneLog_post(FeatureCount):
    def __init__(self, name='UnoRoomPlayReviewOneLog_post', log='UnoRoomPlayReviewOneLog'):
        FeatureCount.__init__(self, name, log)

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            return 1
        else:
            return 0


class UnoRoomPlayReviewOneLog_get(FeatureCount):
    def __init__(self, name='UnoRoomPlayReviewOneLog_get', log='UnoRoomPlayReviewOneLog'):
        FeatureCount.__init__(self, name, log)

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1
        else:
            return 0

class UnoRoomPlayReviewOneLog_get_num(FeatureCount):
    def __init__(self, name='UnoRoomPlayReviewOneLog_get_num', log='UnoRoomPlayReviewOneLog'):
        FeatureCount.__init__(self, name, log)

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return len(json.loads(item['raw_info']['Info'])['CardsList'])
        else:
            return 0

class UnoRoomPlayReviewOneLog_timeover(FeatureCount):
    def __init__(self, name='UnoRoomPlayReviewOneLog_timeover', log='UnoRoomPlayReviewOneLog'):
        FeatureCount.__init__(self, name, log)

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            return 1 if int(json.loads(item['raw_info']['Info'])['UseTime']) >= 10 else 0
        else:
            return None

    def __process__(self):
        return sum(self.L)


class UnoRoomPlayReviewOneLog_timeconsume_average(FeatureCount):
    def __init__(self, name='UnoRoomPlayReviewOneLog_timeconsume_average', log='UnoRoomPlayReviewOneLog'):
        FeatureCount.__init__(self, name, log)

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            return json.loads(item['raw_info']['Info'])['UseTime']
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


class UnoRoomPlayReviewOneLog_postmagiccardovertime(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_postmagiccardovertime', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            if str(json.loads(item['raw_info']['Info'])['CardType']) in ['1', '2'] and int(json.loads(item['raw_info']['Info'])['UseTime']) >= 10:
                return 1
        return 0


class UnoRoomPlayReviewOneLog_postpowercardovertime(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_postpowercardovertime', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            if str(json.loads(item['raw_info']['Info'])['CardType'])[-2:] in ['01', '02', '03', '04'] and int(json.loads(item['raw_info']['Info'])['UseTime']) >= 10:
                return 1
        return 0



class UnoRoomPlayReviewOneLog_postmagiccard(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_postmagiccard', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            if str(json.loads(item['raw_info']['Info'])['CardType']) in ['1', '2']:
                return 1
        return 0


class UnoRoomPlayReviewOneLog_postpowercard(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_postpowercard', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            if str(json.loads(item['raw_info']['Info'])['CardType'])[-2:] in ['01', '02', '03', '04']:
                return 1
        return 0

class UnoRoomPlayReviewOneLog_initmagiccard(Feature):
    def __init__(self):
        Feature.__init__(self, 'UnoRoomPlayReviewOneLog_initmagiccard', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        count = 0
        if item['raw_info']['TypeStr'] == 'StartUnoPlayOne':
            D = json.loads(item['raw_info']['Info'])['CardList']
            for card in D:
                if str(card) in ('1', '2'):
                    count = count + 1
            return count
        else:
            return None

class UnoRoomPlayReviewOneLog_getmagiccard(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_getmagiccard', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        count = 0
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            D = json.loads(item['raw_info']['Info'])['CardsList']
            for (index, card) in D.items():
                if str(card) in ('1', '2'):
                    count = count + 1
        return count

class UnoRoomPlayReviewOneLog_initpowercard(Feature):
    def __init__(self):
        Feature.__init__(self, 'UnoRoomPlayReviewOneLog_initpowercard', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        count = 0
        if item['raw_info']['TypeStr'] == 'StartUnoPlayOne':
            D = json.loads(item['raw_info']['Info'])['CardList']
            for card in D:
                if str(card)[-2:] in ('01', '02', '03', '04'):
                    count = count + 1
            return count
        else:
            return None

class UnoRoomPlayReviewOneLog_getpowercard(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_getpowercard', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        count = 0
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            D = json.loads(item['raw_info']['Info'])['CardsList']
            for (index, card) in D.items():
                if str(card)[-2:] in ('01', '02', '03', '04'):
                    count = count + 1
        return count


class UnoRoomPlayReviewOneLog_argue(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_argue', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'SendChallengeWildFourResult':
            return 1
        else:
            return 0


class UnoRoomPlayReviewOneLog_arguesuccess(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_arguesuccess', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'SendChallengeWildFourResult':
            return 1 if json.loads(item['raw_info']['Info'])['Result'] else 0
        else:
            return 0


class UnoRoomPlayReviewOneLog_arguehappen(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_arguehappen', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'SendChallengeWildFourResult':
            return 1 if json.loads(item['raw_info']['Info'])['IsChallenge'] else 0
        else:
            return 0


class UnoRoomPlayReviewOneLog_unomay(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_unomay', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            return 1 if json.loads(item['raw_info']['Info'])['UnoDeclared'] else 0
        else:
            return 0

class UnoRoomPlayReviewOneLog_unohappen(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_unohappen', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'OtherDeclareUnoStatus':
            return 1
        else:
            return 0

class UnoRoomPlayReviewOneLog_catchcause(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1
        else:
            return 0


class UnoRoomPlayReviewOneLog_catchcause1(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause1', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1 if json.loads(item['raw_info']['Info'])['Cause'] == 1 else 0
        else:
            return 0


class UnoRoomPlayReviewOneLog_catchcause2(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause2', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1 if json.loads(item['raw_info']['Info'])['Cause'] == 2 else 0
        else:
            return 0


class UnoRoomPlayReviewOneLog_catchcause3(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause3', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1 if json.loads(item['raw_info']['Info'])['Cause'] == 3 else 0
        else:
            return 0
class UnoRoomPlayReviewOneLog_catchcause4(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause4', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1 if json.loads(item['raw_info']['Info'])['Cause'] == 4 else 0
        else:
            return 0

class UnoRoomPlayReviewOneLog_catchcause4_4(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause4_4', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1 if json.loads(item['raw_info']['Info'])['Cause'] == 4 and len(json.loads(item['raw_info']['Info'])['CardsList'])<5 else 0
        else:
            return 0

class UnoRoomPlayReviewOneLog_catchcause4_6(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause4_6', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1 if json.loads(item['raw_info']['Info'])['Cause'] == 4 and len(json.loads(item['raw_info']['Info'])['CardsList'])>5 else 0
        else:
            return 0


class UnoRoomPlayReviewOneLog_catchcause5(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause5', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1 if json.loads(item['raw_info']['Info'])['Cause'] == 5 else 0
        else:
            return 0


class UnoRoomPlayReviewOneLog_catchcause6(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_catchcause6', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 1 if json.loads(item['raw_info']['Info'])['Cause'] == 6 else 0
        else:
            return 0


class UnoRoomPlayReviewOneLog_forcerule(Feature):
    def __init__(self):
        Feature.__init__(self, 'UnoRoomPlayReviewOneLog_forcerule', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return 0 if json.loads(item['raw_info']['Info'])['IsForcePlay'] == 'false' else 1
        else:
            return None


class UnoRoomPlayReviewOneLog_remainnum(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_remainnum', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return json.loads(item['raw_info']['Info'])['RemainNum']
        else:
            return None

    def __process__(self):
        L = self.L
        return L[-1] if len(L) > 0 else None
