import datetime
import json
import argparse
from Utils.GetRoleId import GetRoleId
from Utils.GetAllFiles import GetAllFiles
from Utils.GlobalVariable import GlobalVariable
from Utils.not_None import not_None
from TimeSplit.OneGameSplit import OneGameSplit
from PlayerSplit.H5PlayerSplit import H5PlayerSplit
from PlayerSplit.AppPlayerSplit import AppPlayerSplit
from FeatureDef.uno import *
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'manual to this script')
    parser.add_argument('--dir', type=str, default = '/srv/uno-churn-dataset/uno/new_es/')
    args = parser.parse_args()
    count = 0
    featurenames=['LoginRole_freq','LoginRole_rolelevel'
              ,'LogoutRole_onlinetime'
              ,'LogoutRole_expsum','Trade_FFirst_coins_change','Trade_FSecond_coins_change','Trade_FThird_coins_change'
              ,'Trade_LFirst_coins_change','Trade_LSecond_coins_change','Trade_LThird_coins_change','Trade_Final_coins'
              ,'ShareLog_freq','InviteLog_freq','Invite_and_get_into_room','Invite_and_start_game','FollowLog_freq','AdsLog_freq'
              ,'AdsLog_type','AddAchievement_freq','AddExp_freq','Backpack_freq','ConsumeItem_freq'
              ,'DailyReward_freq','DailySign_freq','DailySignReward_freq','DailyTaskFinish_freq','DailyTaskReward_freq','GradeUp_final_grade'
              ,'GradeUp_final_exp','MatchInfo_freq'
              ,'MatchInfo_timeavg','MatchInfo_timemax','MatchInfo_timemin','PraisePlayRound_freq','QuickMatch1V1_freq','QuickMatch1V1_winratio'
              ,'F1QuickMatch1V1_winratio','QuickMatch1V1_rank','F1QuickMatch1V1_rank','QuickMatch2V2_freq','QuickMatch2V2_winratio'
              ,'F1QuickMatch2V2_winratio','ReplaceRole_freq','RewardAchievement_freq'
              ,'RoomModeCreate_freq','RoomModeCreate_mode','SendEmotion_freq','SendEmotion_type1_freq','SendEmotion_type2_freq'
              ,'SendEmotion_type3_freq','SendEmotion_type4_freq','SendGift_freq','SendGift_amount','UnoRoomPlayReviewOneLog_freq'
              ,'UnoRoomPlayReviewOneLog_timeconsume_average','UnoRoomPlayReviewOneLog_timeconsume_min','UnoRoomPlayReviewOneLog_timeconsume_max'
              ,'UnoRoomPlayReviewOneLog_postmagiccard_freq','UnoRoomPlayReviewOneLog_postpowercard_freq','UnoRoomPlayReviewOneLog_getmagiccard_freq'
              ,'UnoRoomPlayReviewOneLog_getpowercard_freq','UnoRoomPlayReviewOneLog_argue_freq'
              ,'UnoRoomPlayReviewOneLog_arguesuccess_freq','UnoRoomPlayReviewOneLog_arguehappen_freq','UnoRoomPlayReviewOneLog_unomay_freq'
              ,'UnoRoomPlayReviewOneLog_uno_freq','UnoRoomPlayReviewOneLog_catchcause_freq','UnoRoomPlayReviewOneLog_catchcause1_freq'
              ,'UnoRoomPlayReviewOneLog_catchcause2_freq','UnoRoomPlayReviewOneLog_catchcause3_freq','UnoRoomPlayReviewOneLog_catchcause4_freq'
              ,'UnoRoomPlayReviewOneLog_catchcause5_freq','UnoRoomPlayReviewOneLog_catchcause6_freq','UnoRoomPlayReviewOneLog_forcerule'
              ,'UnoRoomPlayReviewOneLog_remainnum','UnoRoomPlayReviewOneLog_post_freq','UnoRoomPlayReviewOneLog_get_freq'
              ,'UnoRoomPlayReviewOneLog_timeover_freq'
              ,'Tutorial_freq','Tutorial_start_freq','Tutorial_finish_freq','Tutorial_start_plus4','Tutorial_start_2v2','Tutorial_start_uno'
              ,'Tutorial_start_friend','Tutorial_finish_plus4'
              ,'Tutorial_finish_2v2','Tutorial_finish_uno','Tutorial_finish_friend','Tutorial_usetime_plus4','Tutorial_usetime_2v2'
              ,'Tutorial_usetime_uno','Tutorial_usetime_friend']


    itemDatas=[]
    features=[]
    for featurename in featurenames:
        features.append(eval(featurename+'()'))

    filelist = GetAllFiles(args.dir)
    #filelist = ['1.json','2.json']
    PlayerSplit = H5PlayerSplit()
    TimeSplit = OneGameSplit()
    for filename in filelist:
        with open(filename,'r') as f:
            count = count +1
            if count%10000==0:
                print('now:',count)
            data = f.read()
            items = json.loads(data)
            role_id = GetRoleId(items)
            GlobalVariable.role_id = role_id
            endtime = TimeSplit.run(items)
            resourcename = PlayerSplit.name
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
                itemDatas.append([label,role_id,featureData[:]])

    dirIndex = list(filter(not_None,str(args.dir).split('/')))[-1]
    with open('data/'+dirIndex+'_'+resourcename+'_result.txt','w') as f:
        for itemData in itemDatas:
            f.write(str(itemData[0])+'|'+str(itemData[1])+'|'+'|'.join(itemData[2])+'\n')

    with open('data/'+dirIndex+'_'+resourcename+'_featurename.txt','w') as f2:
        tmp = zip(featurenames,range(0,len(featurenames)))
        f2.write('序号\t名字\t描述\t重要级\tNone值\tDefault建议值\n')
        f2.write('\n'.join(['\t'.join([str(x[1]),x[0],'详见xx','1','-1','0']) for x in tmp]))
