import datetime
import json
import argparse
from Utils.GetRoleId import GetRoleId
from Utils.GetSerialId import GetSerialId
from Utils.GetAllFiles import GetAllFiles
from Utils.GlobalVariable import GlobalVariable
from Utils.DropDuplicate import DropDuplicate
from Utils.not_None import not_None
from TimeSplit.OneGameSplit import OneGameSplit
from PlayerSplit.H5PlayerSplit import H5PlayerSplit
from PlayerSplit.AppPlayerSplit import AppPlayerSplit
from FeatureDef.uno import *
featurenames=['LoginRole_country']

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'manual to this script')
    parser.add_argument('--dir', type=str, default = '/srv/uno-churn-dataset/uno/new_es/')
    args = parser.parse_args()
    count = 0
    SerialId = None
    itemDatas=[]
    features=[]
    for featurename in featurenames:
        features.append(eval(featurename+'()'))

    filelist = GetAllFiles(args.dir)
    #filelist = ['1.json']
    PlayerSplit = H5PlayerSplit()
    TimeSplit = OneGameSplit()
    dirIndex = list(filter(not_None,str(args.dir).split('/')))[-1]
    resourcename = PlayerSplit.name
    with open('data/'+dirIndex+'_'+resourcename+'_featurename_old_tmp.txt','w') as f2:
        tmp = zip(featurenames,range(0,len(featurenames)))
        f2.write('序号\t名字\t描述\t重要级\tNone值\tDefault建议值\n')
        f2.write('\n'.join(['\t'.join([str(x[1]),x[0],'详见xx','1','-1','0']) for x in tmp]))

    for filename in filelist:
        with open(filename,'r') as f:
            count = count +1
            if count%10000==0:
                print('now:',count)
            data = f.read()
            items = json.loads(data)
            items = DropDuplicate(items)
            role_id = GetRoleId(items)
            GlobalVariable.role_id = role_id
            endtime = TimeSplit.run(items)
            SerialId = GetSerialId(items)
            label = 0
            if PlayerSplit.run(items) :
                for item in items:
                    if datetime.datetime.strptime(item['timestamp'], "%Y-%m-%d %H:%M:%S") < datetime.datetime.strptime(endtime, "%Y-%m-%d %H:%M:%S"):
                        for feature in features:
                            if feature.log == item['log_id']:
                                feature.append(item)
                    else:
                        label = 1
                featureData=[]
                for feature in features:
                    featureData.append(feature.run())
                itemDatas.append([label,role_id,SerialId,featureData[:]])


    with open('data/'+dirIndex+'_'+resourcename+'_result_tmp.txt','w') as f:
        for itemData in itemDatas:
            f.write(str(itemData[0])+'|'+str(itemData[1])+'|'+str(itemData[2])+'|'+'|'.join(itemData[3])+'\n')


