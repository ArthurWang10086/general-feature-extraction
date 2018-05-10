from Utils.GlobalVariable import GlobalVariable
import sys


class Feature(object):
    def __init__(self, name, log):
        self.name = name
        self.value = None
        self.log = log

    def __parse__(self, item):
        pass

    def append(self, item):
        if self.value is None:
            try:
                self.value = self.__parse__(item)
            except Exception as e:
                print('parse error', GlobalVariable.role_id, self.name, e, item)
                self.value = None

    def __preprocess__(self):
        pass

    def __process__(self):
        return self.value

    def run(self):
        self.__preprocess__()
        try:
            if self.value != None:
                tmp = self.__process__()
                # print(self.name,tmp)
                self.value = None
                return str(tmp) if str(tmp) != 'None' else '-1'
            else:
                return '-1'
        except Exception as e:
            print('process error', GlobalVariable.role_id, self.name, e, self.value)
            return '-1'
