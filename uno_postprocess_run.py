import pandas as pd
import numpy as np
import  uno_process_run
if __name__=='__main__':
    name = '/srv/uno-churn-service/uno/wangkai/general-feature-extraction/data/'
    log_feature_filename = name+'2018-04-12_H5_result.txt'
    log_featurename_filename = name+'2018-04-12_H5_featurename.txt'
    hive_feature_filename = name+'2018-04-12_Hive_result.txt'
    output_filename = name+'2018-04-12_H5_allfeature.txt'

    log_featurenames = ['label','role_id','SerialId']+uno_process_run.featurenames
    df_log=pd.read_table(log_feature_filename,sep='|',names=log_featurenames)
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
        names = ['label','role_id','SerialId']+uno_process_run.featurenames + hive_featurenames[1:-1]
        print(names)
        tmp = zip(names,range(0,len(names)))
        f2.write('序号\t名字\t描述\t重要级\tNone值\tDefault建议值\n')
        f2.write('\n'.join(['\t'.join([str(x[1]),x[0],'详见xx','1','-1','0']) for x in tmp]))



