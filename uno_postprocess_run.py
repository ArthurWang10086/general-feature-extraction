import pandas as pd
import numpy as np
import  uno_process_run
if __name__=='__main__':
    name = '/srv/uno-churn-service/uno/wangkai/general-feature-extraction/data/'
    date='2018-04-12'
    log_feature_filename = name+date+'_H5_result.txt'
    log_featurename_filename = name+date+'_H5_featurename.txt'
    hive_feature_filename = name+'wangkai_uno_feature_v1.txt'
    output_filename = name+date+'_H5_allfeature.txt'

    log_featurenames = ['label','role_id','SerialId']+uno_process_run.featurenames
    df_log=pd.read_table(log_feature_filename,sep='|',names=log_featurenames)
    df_log=df_log[df_log['MatchInfo_freq']>0]
    df_log=df_log[df_log['RoomModeCreate_freq']<1]
    df_log['UnoRoomPlayReviewOneLog_postmagiccard_ratio']=df_log['UnoRoomPlayReviewOneLog_postmagiccard']/(df_log['UnoRoomPlayReviewOneLog_getmagiccard']+df_log['UnoRoomPlayReviewOneLog_initmagiccard'])
    df_log['UnoRoomPlayReviewOneLog_postmagiccard_ratio'][df_log['UnoRoomPlayReviewOneLog_getmagiccard']+df_log['UnoRoomPlayReviewOneLog_initmagiccard']<1]=-1
    df_log['UnoRoomPlayReviewOneLog_postpowercard_ratio']=df_log['UnoRoomPlayReviewOneLog_postpowercard']/(df_log['UnoRoomPlayReviewOneLog_getpowercard']+df_log['UnoRoomPlayReviewOneLog_initpowercard'])
    df_log['UnoRoomPlayReviewOneLog_postpowercard_ratio'][df_log['UnoRoomPlayReviewOneLog_getpowercard']+df_log['UnoRoomPlayReviewOneLog_initpowercard']<1]=-1
    #df_log['UnoRoomPlayReviewOneLog_uno_ratio']=df_log['UnoRoomPlayReviewOneLog_unomay']/df_log['UnoRoomPlayReviewOneLog_unohappen']
    df_log['UnoRoomPlayReviewOneLog_post_ratio']= df_log['UnoRoomPlayReviewOneLog_post']/df_log['UnoRoomPlayReviewOneLog_get_num']
    df_log['UnoRoomPlayReviewOneLog_post_ratio'][df_log['UnoRoomPlayReviewOneLog_get_num']<1]=-1
    df_log['UnoRoomPlayReviewOneLog_postovertime_ratio']= df_log['UnoRoomPlayReviewOneLog_timeover']/df_log['UnoRoomPlayReviewOneLog_post']
    df_log['UnoRoomPlayReviewOneLog_postovertime_ratio'][df_log['UnoRoomPlayReviewOneLog_post']<1]=-1
    df_log['RewardAchievement_ratio']= df_log['RewardAchievement_freq']/df_log['AddAchievement_freq']
    df_log['RewardAchievement_ratio'][df_log['AddAchievement_freq']<1]=-1
    df_log['DailySignReward_ratio']= df_log['DailySignReward_freq']/df_log['DailySign_freq']
    df_log['DailySignReward_ratio'][df_log['DailySign_freq']<1]=-1
    #df_log['DailyTaskReward_ratio']= df_log['DailyTaskReward_freq']/df_log['DailyTaskFinish_freq']
    df_log['DailySignReward_timediff']= df_log['DailySignReward_time']-df_log['LoginRole_logintime']
    df_log['DailySignReward_timediff'][df_log['DailySignReward_time']<0]=-1
    df_log['DailyTaskFinish_timediff']=df_log['DailyTaskFinish_time']-df_log['LoginRole_logintime']
    df_log['DailyTaskFinish_timediff'][df_log['DailyTaskFinish_time']<0]=-1
    df_log['MatchInfo_timediff']=df_log['MatchInfo_time']-df_log['LoginRole_logintime']
    df_log['MatchInfo_timediff'][df_log['MatchInfo_time']<0]=-1
    df_log['DailySign_timediff']=df_log['DailySign_time']-df_log['LoginRole_logintime']
    df_log['DailySign_timediff'][df_log['DailySign_time']<0]=-1
    df_log['DailyReward_timediff']=df_log['DailyReward_time']-df_log['LoginRole_logintime']
    df_log['DailyReward_timediff'][df_log['DailyReward_time']<0]=-1
    df_log['ConsumeItem_timediff']=df_log['ConsumeItem_time']-df_log['LoginRole_logintime']
    df_log['ConsumeItem_timediff'][df_log['ConsumeItem_time']<0]=-1
    df_log['Backpack_timediff']=df_log['Backpack_time']-df_log['LoginRole_logintime']
    df_log['Backpack_timediff'][df_log['Backpack_time']<0]=-1
    df_log['AddAchievement_timediff']=df_log['AddAchievement_time']-df_log['LoginRole_logintime']
    df_log['AddAchievement_timediff'][df_log['AddAchievement_time']<0]=-1
    add_featurenames=['UnoRoomPlayReviewOneLog_postmagiccard_ratio','UnoRoomPlayReviewOneLog_postpowercard_ratio'
                      ,'UnoRoomPlayReviewOneLog_post_ratio','UnoRoomPlayReviewOneLog_postovertime_ratio'
                      ,'RewardAchievement_ratio','DailySignReward_ratio','DailySignReward_timediff'
                      ,'DailyTaskFinish_timediff','MatchInfo_timediff','DailySign_timediff','DailyReward_timediff'
                      ,'ConsumeItem_timediff','Backpack_timediff','AddAchievement_timediff']

    remove_featurenames=['LoginRole_logintime','AddAchievement_time'
        ,'Backpack_time'
        ,'ConsumeItem_time'
        ,'DailyReward_time'
        ,'DailySign_time'
        ,'DailySignReward_time'
        ,'DailyTaskFinish_time'
        ,'MatchInfo_time']
    for x in remove_featurenames:
        log_featurenames.remove(x)
    log_featurenames=log_featurenames+add_featurenames
    print(log_featurenames)
    df_log=df_log[log_featurenames]
    df_log.to_csv(log_feature_filename+'.2', sep='|',index=False,header=False)


    hive_featurenames = ['SerialId','getusetimemin','gettimeaverage'
        ,'getusetimemax' ,'postusetimemin','posttimeaverage'
        ,'postusetimemax','unocount','date']
    df_hive=pd.read_table(hive_feature_filename
                          ,sep='\t'
                          ,names=hive_featurenames
                          ,usecols=hive_featurenames[:-1])
    #df_hive = df_hive.fillna(value=0, inplace=True)

    df = df_log.merge(df_hive,how = 'inner')
    df.fillna(value=0, inplace=True)
    df.to_csv(output_filename, sep='|',index=False,header=False)


    with open(log_featurename_filename,'w') as f2:
        names = log_featurenames+hive_featurenames[1:-1]
        print(names)
        tmp = zip(names,range(0,len(names)))
        f2.write('序号\t名字\t描述\t重要级\tNone值\tDefault建议值\n')
        f2.write('\n'.join(['\t'.join([str(x[1]),x[0],'详见xx','1','-1','0']) for x in tmp]))



