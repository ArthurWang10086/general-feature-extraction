from Feature.FeatureCount import FeatureCount
from Feature.Feature import Feature
import yaml


# GuideInfo_step -  如果在开局就点击SKIP则步骤为0，完成全部新手引导则记为30,31为选择简易新手引导，1-29为新手引导中的步骤 GuideInfo step
class GuideInfo_step(Feature):
    def __init__(self):
        Feature.__init__(self, 'GuideInfo_step', 'GuideInfo')

    def __parse__(self, item):
        if type(item['raw_info']) != str:
            item['raw_info'] = item['raw_info']
        else:
            try:
                item['raw_info'] = yaml.safe_load(item['raw_info'].split('[GuideInfo],')[1])
            except:
                return None
        if 'step' not in item['raw_info']:
            GuideInfo_step = 0
        else:
            if item['raw_info']['step'] < 30:
                GuideInfo_step = item['raw_info']['step']
                if 'start_time' in item['raw_info']:
                    GuideInfo_time = item['raw_info']['skip_time'] - item['raw_info']['start_time']
                else:
                    return None
                Is_Guide_Skipped = 0
                Is_Guide_Finished = 0
            else:
                GuideInfo_step = item['raw_info']['step']
                if 'start_time' in item['raw_info']:
                    GuideInfo_time = item['raw_info']['skip_time'] - item['raw_info']['start_time']
                else:
                    return None
                Is_Guide_Skipped = 0
                Is_Guide_Finished = 1
        return GuideInfo_step


# GuideInfo_time - 玩家结束新手引导时间-玩家开始新手引导时间 GuideInfo skip_time-start_time
class GuideInfo_time(Feature):
    def __init__(self):
        Feature.__init__(self, 'GuideInfo_time', 'GuideInfo')

    def __parse__(self, item):
        if type(item['raw_info']) != str:
            item['raw_info'] = item['raw_info']
        else:
            try:
                item['raw_info'] = yaml.safe_load(item['raw_info'].split('[GuideInfo],')[1])
            except:
                return None
        if 'step' not in item['raw_info']:
            GuideInfo_step = 0
            GuideInfo_time = 0
            Is_Guide_Skipped = 1
            Is_Guide_Finished = 0
        else:
            if item['raw_info']['step'] < 30:
                GuideInfo_step = item['raw_info']['step']
                if 'start_time' in item['raw_info']:
                    GuideInfo_time = item['raw_info']['skip_time'] - item['raw_info']['start_time']
                else:
                    return None
                Is_Guide_Skipped = 0
                Is_Guide_Finished = 0
            else:
                GuideInfo_step = item['raw_info']['step']
                if 'start_time' in item['raw_info']:
                    GuideInfo_time = item['raw_info']['skip_time'] - item['raw_info']['start_time']
                else:
                    return None
                Is_Guide_Skipped = 0
                Is_Guide_Finished = 1
        return GuideInfo_time


# Is_Guide_Skipped - 是否跳过新手引导
class Is_Guide_Skipped(Feature):
    def __init__(self):
        Feature.__init__(self, 'Is_Guide_Skipped', 'GuideInfo')

    def __parse__(self, item):
        if type(item['raw_info']) != str:
            item['raw_info'] = item['raw_info']
        else:
            try:
                item['raw_info'] = yaml.safe_load(item['raw_info'].split('[GuideInfo],')[1])
            except:
                return None
        if 'step' not in item['raw_info']:
            GuideInfo_step = 0
            GuideInfo_time = 0
            Is_Guide_Skipped = 1
            Is_Guide_Finished = 0
        else:
            if item['raw_info']['step'] < 30:
                GuideInfo_step = item['raw_info']['step']
                if 'start_time' in item['raw_info']:
                    GuideInfo_time = item['raw_info']['skip_time'] - item['raw_info']['start_time']
                else:
                    return None
                Is_Guide_Skipped = 0
                Is_Guide_Finished = 0
            else:
                GuideInfo_step = item['raw_info']['step']
                if 'start_time' in item['raw_info']:
                    GuideInfo_time = item['raw_info']['skip_time'] - item['raw_info']['start_time']
                else:
                    return None
                Is_Guide_Skipped = 0
                Is_Guide_Finished = 1
        return Is_Guide_Skipped


# Is_Guide_Finished - 是否完成新手引导 step >= 30
class Is_Guide_Finished(Feature):
    def __init__(self):
        Feature.__init__(self, 'Is_Guide_Finished', 'GuideInfo')

    def __parse__(self, item):
        if type(item['raw_info']) != str:
            item['raw_info'] = item['raw_info']
        else:
            try:
                item['raw_info'] = yaml.safe_load(item['raw_info'].split('[GuideInfo],')[1])
            except:
                return None
        if 'step' not in item['raw_info']:
            GuideInfo_step = 0
            GuideInfo_time = 0
            Is_Guide_Skipped = 1
            Is_Guide_Finished = 0
        else:
            if item['raw_info']['step'] < 30:
                GuideInfo_step = item['raw_info']['step']
                if 'start_time' in item['raw_info']:
                    GuideInfo_time = item['raw_info']['skip_time'] - item['raw_info']['start_time']
                else:
                    return None
                Is_Guide_Skipped = 0
                Is_Guide_Finished = 0
            else:
                GuideInfo_step = item['raw_info']['step']
                if 'start_time' in item['raw_info']:
                    GuideInfo_time = item['raw_info']['skip_time'] - item['raw_info']['start_time']
                else:
                    return None
                Is_Guide_Skipped = 0
                Is_Guide_Finished = 1
        return Is_Guide_Finished
