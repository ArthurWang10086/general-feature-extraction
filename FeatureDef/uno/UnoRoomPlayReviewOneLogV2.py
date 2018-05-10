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
                tmp = x
                break
        L.remove(tmp)
        start = tmp[1]
        if len(start)>0:
            for x in L:
                if x[0] == 'CatchUnoCardResult':
                    for card in x[1]:
                        start.append(card[1])
                elif x[0] == 'StartUnoPlayOne':
                    break
            for x in L:
                if x[0] == 'PlayUnoCardResult':
                    start.remove(x[1])
                elif x[0] == 'StartUnoPlayOne':
                    break
            return len(start)
        else:
            return None
