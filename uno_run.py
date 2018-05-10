import datetime
import json
from Utils.GetRoleId import GetRoleId
from Utils.GlobalVariable import GlobalVariable
from TimeSplit.OneGameSplit import OneGameSplit
from FeatureDef.uno import *
if __name__ == '__main__':


    featurenames=['LoginRole_freq','LoginRole_country','LoginRole_osname','LoginRole_appchannel','LoginRole_rolelevel'
              ,'LoginRole_logintime','LoginRole_clientsource','LoginRole_clienttype','LogoutRole_onlinetime','LogoutRole_logouttime'
              ,'LogoutRole_expsum','Trade_reason','Trade_FFirst_coins_change','Trade_FSecond_coins_change','Trade_FThird_coins_change'
              ,'Trade_LFirst_coins_change','Trade_LSecond_coins_change','Trade_LThird_coins_change','Trade_Final_coins'
              ,'ShareLog_freq','InviteLog_freq','Invite_and_get_into_room','Invite_and_start_game','FollowLog_freq','AdsLog_freq'
              ,'AdsLog_type','AdsLog_addtime','AddAchievement_freq','AddExp_freq','Backpack_freq','Backpack_reason','ConsumeItem_freq'
              ,'DailyReward_freq','DailySign_freq','DailySignReward_freq','DailyTaskFinish_freq','DailyTaskReward_freq','GradeUp_final_grade'
              ,'GradeUp_final_exp','GuideInfo_step','GuideInfo_time','Is_Guide_Skipped','Is_Guide_Finished','MatchInfo_freq'
              ,'MatchInfo_timeavg','MatchInfo_timemax','MatchInfo_timemin','PraisePlayRound_freq','QuickMatch1V1_freq','QuickMatch1V1_winratio'
              ,'F1QuickMatch1V1_winratio','F2QuickMatch1V1_winratio','F3QuickMatch1V1_winratio','L1QuickMatch1V1_winratio','L2QuickMatch1V1_winratio'
              ,'L3QuickMatch1V1_winratio','QuickMatch1V1_rank','F1QuickMatch1V1_rank','F2QuickMatch1V1_rank','F3QuickMatch1V1_rank'
              ,'L1QuickMatch1V1_rank','L2QuickMatch1V1_rank','L3QuickMatch1V1_rank','QuickMatch2V2_freq','QuickMatch2V2_winratio'
              ,'F1QuickMatch2V2_winratio','F2QuickMatch2V2_winratio','F3QuickMatch2V2_winratio','L1QuickMatch2V2_winratio'
              ,'L2QuickMatch2V2_winratio','L3QuickMatch2V2_winratio','ReplaceRole_freq','ReplaceRole_time','RewardAchievement_freq'
              ,'RoomModeCreate_freq','RoomModeCreate_mode','SendEmotion_freq','SendEmotion_type1_freq','SendEmotion_type2_freq'
              ,'SendEmotion_type3_freq','SendEmotion_type4_freq','SendEmotion_time','SendGift_freq','SendGift_amount','UnoRoomPlayReviewOneLog_freq'
              ,'UnoRoomPlayReviewOneLog_timeconsume_average','UnoRoomPlayReviewOneLog_timeconsume_min','UnoRoomPlayReviewOneLog_timeconsume_max'
              ,'UnoRoomPlayReviewOneLog_postmagiccard_freq','UnoRoomPlayReviewOneLog_postpowercard_freq','UnoRoomPlayReviewOneLog_getmagiccard_freq'
              ,'UnoRoomPlayReviewOneLog_getpowercard_freq','UnoRoomPlayReviewOneLog_argue_freq'
              ,'UnoRoomPlayReviewOneLog_arguesuccess_freq','UnoRoomPlayReviewOneLog_arguehappen_freq','UnoRoomPlayReviewOneLog_unomay_freq'
              ,'UnoRoomPlayReviewOneLog_uno_freq','UnoRoomPlayReviewOneLog_catchcause_freq','UnoRoomPlayReviewOneLog_catchcause1_freq'
              ,'UnoRoomPlayReviewOneLog_catchcause2_freq','UnoRoomPlayReviewOneLog_catchcause3_freq','UnoRoomPlayReviewOneLog_catchcause4_freq'
              ,'UnoRoomPlayReviewOneLog_catchcause5_freq','UnoRoomPlayReviewOneLog_catchcause6_freq','UnoRoomPlayReviewOneLog_forcerule'
              ,'UnoRoomPlayReviewOneLog_remainnum','UnoRoomPlayReviewOneLog_userremainnum','UnoRoomPlayReviewOneLog_post_freq','UnoRoomPlayReviewOneLog_get_freq'
              ,'UnoRoomPlayReviewOneLog_timeover_freq'
              ,'Tutorial_freq','Tutorial_start_freq','Tutorial_finish_freq','Tutorial_start_plus4','Tutorial_start_2v2','Tutorial_start_uno'
              ,'Tutorial_start_friend','Tutorial_finish_plus4'
              ,'Tutorial_finish_2v2','Tutorial_finish_uno','Tutorial_finish_friend','Tutorial_usetime_plus4','Tutorial_usetime_2v2'
              ,'Tutorial_usetime_uno','Tutorial_usetime_friend']

    itemData=[]
    features=[]
    for featurename in featurenames:
        features.append(eval(featurename+'()'))
    for filename in ['11.json',]*1:
        with open(filename,'r') as f:
            data = f.read()
            items = json.loads(data)
            role_id = GetRoleId(items)
            GlobalVariable.role_id = role_id
            endtime = OneGameSplit.run(items)
            for item in items:
                label = 0
                if datetime.datetime.strptime(item['timestamp'], "%Y-%m-%d %H:%M:%S") < datetime.datetime.strptime(endtime, "%Y-%m-%d %H:%M:%S"):
                    for feature in features:
                        if feature.log == item['log_id']:
                            feature.append(item)
                else:
                    label = 1

            featureData=[]
            for feature in features:
                featureData.append(feature.run())
            itemData.append(featureData[:])
            itemData.append(label)
            print(itemData)
            print('success')
    # with open('result.txt','w') as f:
    #     f.write(itemData)
