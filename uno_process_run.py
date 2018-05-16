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
featurenames=['LoginRole_freq','LoginRole_rolelevel'
    ,'LogoutRole_expsum','Trade_FFirst_coins_change'
    ,'Trade_Final_coins'
    ,'AddAchievement_freq','AddExp_freq','Backpack_freq','ConsumeItem_freq'
    ,'DailySign_freq','DailySignReward_freq','DailyTaskFinish_freq','DailyTaskReward_freq','GradeUp_final_grade'
    ,'GradeUp_final_exp','MatchInfo_freq'
    ,'MatchInfo_timeavg','MatchInfo_timemax','MatchInfo_timemin','PraisePlayRound_freq','QuickMatch1V1_freq','QuickMatch1V1_winratio'
    ,'F1QuickMatch1V1_winratio','QuickMatch1V1_rank','F1QuickMatch1V1_rank','QuickMatch2V2_freq','QuickMatch2V2_winratio'
    ,'F1QuickMatch2V2_winratio','ReplaceRole_freq','RewardAchievement_freq'
    ,'RoomModeCreate_freq','RoomModeCreate_mode','SendEmotion_freq','SendEmotion_type1','SendEmotion_type2'
    ,'SendEmotion_type3','SendEmotion_type4','SendGift_freq','SendGift_amount','UnoRoomPlayReviewOneLog_freq'
    ,'UnoRoomPlayReviewOneLog_timeconsume_average','UnoRoomPlayReviewOneLog_timeconsume_min','UnoRoomPlayReviewOneLog_timeconsume_max'
    ,'UnoRoomPlayReviewOneLog_postmagiccard','UnoRoomPlayReviewOneLog_postpowercard'
    ,'UnoRoomPlayReviewOneLog_initmagiccard','UnoRoomPlayReviewOneLog_initpowercard'
    ,'UnoRoomPlayReviewOneLog_getmagiccard','UnoRoomPlayReviewOneLog_getpowercard','UnoRoomPlayReviewOneLog_argue'
    ,'UnoRoomPlayReviewOneLog_arguesuccess','UnoRoomPlayReviewOneLog_arguehappen','UnoRoomPlayReviewOneLog_unomay'
    ,'UnoRoomPlayReviewOneLog_catchcause','UnoRoomPlayReviewOneLog_catchcause1'
    ,'UnoRoomPlayReviewOneLog_catchcause2','UnoRoomPlayReviewOneLog_catchcause3','UnoRoomPlayReviewOneLog_catchcause4'
    ,'UnoRoomPlayReviewOneLog_catchcause5','UnoRoomPlayReviewOneLog_catchcause6','UnoRoomPlayReviewOneLog_forcerule'
    ,'UnoRoomPlayReviewOneLog_remainnum','UnoRoomPlayReviewOneLog_post','UnoRoomPlayReviewOneLog_get','UnoRoomPlayReviewOneLog_get_num','UnoRoomPlayReviewOneLog_init'
    ,'UnoRoomPlayReviewOneLog_timeover'
    ,'Tutorial_freq','Tutorial_start','Tutorial_finish','Tutorial_start_plus4','Tutorial_start_2v2','Tutorial_start_uno'
    ,'Tutorial_start_friend','Tutorial_finish_plus4'
    ,'Tutorial_finish_2v2','Tutorial_finish_uno','Tutorial_finish_friend','Tutorial_usetime_plus4','Tutorial_usetime_2v2'
    ,'Tutorial_usetime_uno','Tutorial_usetime_friend'
    ,'AddAchievement_time'
    ,'Backpack_time'
    ,'ConsumeItem_time'
    ,'DailyReward_time'
    ,'DailySign_time'
    ,'DailySignReward_time'
    ,'DailyTaskFinish_time'
    ,'DailyTaskReward_time'
    ,'MatchInfo_time']

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
    with open('data/'+dirIndex+'_'+resourcename+'_featurename_old.txt','w') as f2:
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


    with open('data/'+dirIndex+'_'+resourcename+'_result.txt','w') as f:
        for itemData in itemDatas:
            f.write(str(itemData[0])+'|'+str(itemData[1])+'|'+str(itemData[2])+'|'+'|'.join(itemData[3])+'\n')


