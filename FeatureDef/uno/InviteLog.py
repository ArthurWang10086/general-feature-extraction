from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature

class InviteLog_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'InviteLog_freq', 'InviteLog')

    def __parse__(self, item):
        if item['raw_info']['type'] == "1":
            return 1
        else:
            return 0


# Invite_and_get_into_room - 邀请者发起邀请，且被邀请者通过邀请者的邀请进入房间（比率） InviteLog type == 2 / type==1
class Invite_and_get_into_room(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'Invite_and_get_into_room', 'InviteLog')

    def __parse__(self, item):
        if item['raw_info']['type'] == "2":
            return 1
        else:
            return 0


# Invite_and_start_game - 邀请者发起邀请频度，且邀请者和被邀请者同时开始游戏（比率）InviteLog type == 3 / type==1
class Invite_and_start_game(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'Invite_and_start_game', 'InviteLog')

    def __parse__(self, item):
        if item['raw_info']['type'] == "3":
            return 1
        else:
            return 0
