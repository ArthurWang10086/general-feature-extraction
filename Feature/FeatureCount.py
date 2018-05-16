from Utils.not_None import not_None
from Utils.GlobalVariable import GlobalVariable
import sys


class FeatureCount(object):
    def __init__(self, name, log):
        self.name = name
        self.L = []
        self.log = log

    def __parse__(self, item):
        return 1

    def append(self, item):
        try:
            value = self.__parse__(item)
        except Exception as e:
            print('parse error', GlobalVariable.role_id, self.name, e, item)
            value = None
        self.L.append(value)

    def __preprocess__(self):
        self.L = list(filter(not_None, self.L))

    def __process__(self):
        return sum(self.L)

    def run(self):
        self.__preprocess__()
        try:
            if len(self.L) > 0:
                tmp = self.__process__()
                print(self.name,tmp)
                self.L = []
                return str(tmp) if str(tmp) != 'None' else '-1'
            else:
                return '-1' if 'freq' not in self.name else '0'
        except Exception as e:
            print('process error', GlobalVariable.role_id, self.name, e, self.L)
            return '-1' if 'freq' not in self.name else '0'
