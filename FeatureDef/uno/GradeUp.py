from Feature.Feature import Feature
import yaml


# Final_GradeUp_grade - 最后等级 GradeUp grade_after
class GradeUp_final_grade(Feature):
    def __init__(self):
        Feature.__init__(self, 'GradeUp_final_grade', 'GradeUp')

    def __parse__(self, item):
        if type(item['raw_info']) != str:
            item['raw_info'] = item['raw_info']
        else:
            try:
                item['raw_info'] = yaml.safe_load(item['raw_info'].split('[GradeUp],')[1])
            except:
                return None
        return item['raw_info']['grade_after']


# Final_GradeUp_exp - 最后经验值  GradeUp exp_after
class GradeUp_final_exp(Feature):
    def __init__(self):
        Feature.__init__(self, 'GradeUp_final_exp', 'GradeUp')

    def __parse__(self, item):
        if type(item['raw_info']) != str:
            item['raw_info'] = item['raw_info']
        else:
            try:
                item['raw_info'] = yaml.safe_load(item['raw_info'].split('[GradeUp],')[1])
            except:
                return None
        return item['raw_info']['exp_after']
