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
            except:
                print('parse error',GlobalVariable.role_id,self.name,sys.exc_info()[0],item)
                self.value = None

    def __preprocess__(self):
        pass

    def __process__(self):
        return self.value

    def run(self):
        self.__preprocess__()
        try:
            tmp = self.__process__()
            #print(self.name,tmp)
            self.value = []
            return str(tmp) if str(tmp)!='None' else '-1'
        except:
            print('process error',GlobalVariable.role_id,self.name,sys.exc_info()[0],self.value)
            return '-1'

