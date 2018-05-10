from Utils.not_None import not_None


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
        except:
            print('parse error',self.name,item)
            value = None
        self.L.append(value)

    def __preprocess__(self):
        self.L = list(filter(not_None, self.L))

    def __process__(self):
        return sum(self.L)

    def run(self):
        self.__preprocess__()
        try:
            tmp = self.__process__()
            # print(self.name,tmp)
            self.L = []
            return tmp
        except:
            print('process error',self.name,self.L)
            return None

