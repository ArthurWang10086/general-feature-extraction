from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature
import yaml


# GuideInfo_step -  如果在开局就点击SKIP则步骤为0，完成全部新手引导则记为30,31为选择简易新手引导，1-29为新手引导中的步骤 GuideInfo step
class Tutorial_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'Tutorial_freq', 'Tutorial')

class Tutorial_start_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'Tutorial_start_freq', 'Tutorial')

    def __parse__(self, item):
        if str(item['raw_info']['step_type']) == '0':
            return 1
        else:
            return 0

class Tutorial_finish_freq(FeatureCount):
    def __init__(self):
        FeatureCount.__init__(self, 'Tutorial_finish_freq', 'Tutorial')

    def __parse__(self, item):
        if str(item['raw_info']['step_type']) == '1':
            return 1
        else:
            return 0

class Tutorial_start_plus4(Feature):
    def __init__(self):
        Feature.__init__(self, 'Tutorial_start_plus4', 'Tutorial')

    def __parse__(self, item):
        if str(item['raw_info']['step_type']) == '0' and int(item['raw_info']['tutorial_id'])==4200008:
            return 1
        else:
            return 0

class Tutorial_start_2v2(Feature):
    def __init__(self):
        Feature.__init__(self, 'Tutorial_start_2v2', 'Tutorial')

    def __parse__(self, item):
        if str(item['raw_info']['step_type']) == '0' and int(item['raw_info']['tutorial_id'])==4200010:
            return 1
        else:
            return 0

class Tutorial_start_uno(Feature):
    def __init__(self):
        Feature.__init__(self, 'Tutorial_start_uno', 'Tutorial')

    def __parse__(self, item):
        if str(item['raw_info']['step_type']) == '0' and int(item['raw_info']['tutorial_id'])==4200009:
            return 1
        else:
            return 0

class Tutorial_start_friend(Feature):
    def __init__(self):
        Feature.__init__(self, 'Tutorial_start_friend', 'Tutorial')

    def __parse__(self, item):
        if str(item['raw_info']['step_type']) == '0' and int(item['raw_info']['tutorial_id'])==4200011:
            return 1
        else:
            return 0

class Tutorial_finish_plus4(Feature):
    def __init__(self):
        Feature.__init__(self, 'Tutorial_finish_plus4', 'Tutorial')

    def __parse__(self, item):
        if str(item['raw_info']['step_type']) == '1' and int(item['raw_info']['tutorial_id'])==4200008:
            return 1
        else:
            return 0

class Tutorial_finish_2v2(Feature):
    def __init__(self):
        Feature.__init__(self, 'Tutorial_finish_2v2', 'Tutorial')

    def __parse__(self, item):
        if str(item['raw_info']['step_type']) == '1' and int(item['raw_info']['tutorial_id'])==4200010:
            return 1
        else:
            return 0

class Tutorial_finish_uno(Feature):
    def __init__(self):
        Feature.__init__(self, 'Tutorial_finish_uno', 'Tutorial')

    def __parse__(self, item):
        if str(item['raw_info']['step_type']) == '1' and int(item['raw_info']['tutorial_id'])==4200009:
            return 1
        else:
            return 0

class Tutorial_finish_friend(Feature):
    def __init__(self):
        Feature.__init__(self, 'Tutorial_finish_friend', 'Tutorial')

    def __parse__(self, item):
        if str(item['raw_info']['step_type']) == '1' and int(item['raw_info']['tutorial_id'])==4200011:
            return 1
        else:
            return 0

class Tutorial_usetime_plus4(Feature):
    def __init__(self):
        Feature.__init__(self, 'Tutorial_usetime_plus4', 'Tutorial')

    def __parse__(self, item):
        if str(item['raw_info']['step_type']) == '1' and int(item['raw_info']['tutorial_id'])==4200008:
            return item['raw_info']['use_time']
        else:
            return None

class Tutorial_usetime_2v2(Feature):
    def __init__(self):
        Feature.__init__(self, 'Tutorial_usetime_2v2', 'Tutorial')

    def __parse__(self, item):
        if str(item['raw_info']['step_type']) == '1' and int(item['raw_info']['tutorial_id'])==4200010:
            return item['raw_info']['use_time']
        else:
            return None

class Tutorial_usetime_uno(Feature):
    def __init__(self):
        Feature.__init__(self, 'Tutorial_usetime_uno', 'Tutorial')

    def __parse__(self, item):
        if str(item['raw_info']['step_type']) == '1' and int(item['raw_info']['tutorial_id'])==4200009:
            return item['raw_info']['use_time']
        else:
            return None

class Tutorial_usetime_friend(Feature):
    def __init__(self):
        Feature.__init__(self, 'Tutorial_usetime_friend', 'Tutorial')

    def __parse__(self, item):
        if str(item['raw_info']['step_type']) == '1' and int(item['raw_info']['tutorial_id'])==4200011:
            print(item['raw_info']['use_time'])
            return item['raw_info']['use_time']
        else:
            return None


