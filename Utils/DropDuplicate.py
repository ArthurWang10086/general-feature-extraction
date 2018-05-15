def DropDuplicate(items):
    tempList=[]
    for item in items:
        #居然可以这么写
        if item not in tempList:
            tempList.append(item)
    return tempList
