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
                print('parse error',self.name,item)
                self.value = None

    def __preprocess__(self):
        pass

    def __process__(self):
        return self.value

    def run(self):
        self.__preprocess__()
        try:
            tmp = self.__process__()
            # print(self.name,tmp)
            self.value = []
            return tmp
        except:
            print('process error',self.name,self.value)
            return None

