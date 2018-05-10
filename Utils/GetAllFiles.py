import os
def GetAllFiles(object):
    def getAllFiles(self,dir):
        L=[]
        for root, dirs, files in os.walk(dir):
            for file in files:
                if os.path.splitext(file)[1] == '.json':
                    L.append(os.path.join(root, file))
        return L
