import pandas as pd
import  uno_process_run
if __name__=='__main__':
    log_feature_filename = '/srv/uno-churn-service/uno/wangkai/general-feature-extraction/data/2018-04-12_H5_result.txt'
    log_featurename_filename = '/srv/uno-churn-service/uno/wangkai/general-feature-extraction/data/2018-04-12_H5_featurename.txt'
    hive_feature_filename = ''
    statistic_filename = ''
    df_log=pd.read_table(log_feature_filename, sep='|',names=['label','role_id','SerialId'].extend(uno_process_run.featurenames))
    df_hive=pd.read_table(hive_feature_filename, sep=','
                          ,names=['SerialId','getusetimemin','gettimeaverage'
                                ,'getusetimemax' ,'postusetimemin','posttimeaverage'
                                ,'postusetimemax','unocount'])

    df = df_log.join(df_hive,'SerialId','inner')



