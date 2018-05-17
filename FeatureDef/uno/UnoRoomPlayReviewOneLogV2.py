from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature
import json


class UnoRoomPlayReviewOneLog_userremainnum(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_userremainnum', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'StartUnoPlayOne':
            return ['StartUnoPlayOne', json.loads(item['raw_info']['InfoStr'])['CardList']]
        elif item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            return ['PlayUnoCardResult', json.loads(item['raw_info']['InfoStr'])['CardType']]
        elif item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return ['CatchUnoCardResult', json.loads(item['raw_info']['InfoStr'])['CardsList']]

    def __process__(self):
        L = self.L
        start = []
        tmp = None
        for x in L:
            if x[0] == 'StartUnoPlayOne':
                tmp = x[:]
                break
        L.remove(tmp)
        start = tmp[1]
        if len(start) > 0:
            for x in L:
                if x[0] == 'CatchUnoCardResult':
                    for (index, card) in dict(x[1]).items():
                        start.append(card)
            for x in L:
                if x[0] == 'PlayUnoCardResult':
                    if x[1] in start:
                        start.remove(x[1])
            return len(start)
        else:
            return None


class UnoRoomPlayReviewOneLog_userremainpowernum(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_userremainpowernum', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'StartUnoPlayOne':
            return ['StartUnoPlayOne', json.loads(item['raw_info']['InfoStr'])['CardList']]
        elif item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            return ['PlayUnoCardResult', json.loads(item['raw_info']['InfoStr'])['CardType']]
        elif item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return ['CatchUnoCardResult', json.loads(item['raw_info']['InfoStr'])['CardsList']]

    def __process__(self):
        L = self.L
        start = []
        tmp = None
        for x in L:
            if x[0] == 'StartUnoPlayOne':
                tmp = x[:]
                break
        L.remove(tmp)
        start = tmp[1]
        if len(start) > 0:
            for x in L:
                if x[0] == 'CatchUnoCardResult':
                    for (index, card) in dict(x[1]).items():
                        start.append(card)
            for x in L:
                if x[0] == 'PlayUnoCardResult':
                    if x[1] in start:
                        start.remove(x[1])
            return sum([1 if str(x)[-2:] in ['01', '02', '03', '04'] else 0 for x in start])
        else:
            return None


class UnoRoomPlayReviewOneLog_userremainmagicnum(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'UnoRoomPlayReviewOneLog_userremainmagicnum', 'UnoRoomPlayReviewOneLog')

    def __parse__(self, item):
        if item['raw_info']['TypeStr'] == 'StartUnoPlayOne':
            return ['StartUnoPlayOne', json.loads(item['raw_info']['InfoStr'])['CardList']]
        elif item['raw_info']['TypeStr'] == 'PlayUnoCardResult':
            return ['PlayUnoCardResult', json.loads(item['raw_info']['InfoStr'])['CardType']]
        elif item['raw_info']['TypeStr'] == 'CatchUnoCardResult':
            return ['CatchUnoCardResult', json.loads(item['raw_info']['InfoStr'])['CardsList']]

    def __process__(self):
        L = self.L
        start = []
        tmp = None
        for x in L:
            if x[0] == 'StartUnoPlayOne':
                tmp = x[:]
                break
        L.remove(tmp)
        start = tmp[1]
        if len(start) > 0:
            for x in L:
                if x[0] == 'CatchUnoCardResult':
                    for (index, card) in dict(x[1]).items():
                        start.append(card)
            for x in L:
                if x[0] == 'PlayUnoCardResult':
                    if x[1] in start:
                        start.remove(x[1])
            return sum([1 if str(x) in ['1', '2'] else 0 for x in start])
        else:
            return None
