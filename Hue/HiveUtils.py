import pyhs2

class HiveClient:
    def __init__(self, db_host, user, password, database, port=10000, authMechanism="PLAIN"):
        """
        create connection to hive server2
        """
        self.conn = pyhs2.connect(host=db_host,
                                  port=port,
                                  authMechanism=authMechanism,
                                  user=user,
                                  password=password,
                                  database=database,
                                  )

    def query(self, sql):

        """
        query
        """

        with self.conn.cursor() as cursor:

            cursor.execute(sql)

            return cursor.fetch()

    def action(self, sql):

        """
        query
        """

        with self.conn.cursor() as cursor:

            cursor.execute(sql)

            return cursor

    def close(self):

        """
        close connection
        """
        self.conn.close()


if __name__ == '__main__':
    hive_client = HiveClient(db_host='59.111.7.43', port=10000, user='hdfs', password='mypass',

                             database='default', authMechanism='PLAIN')


    for t in range(0,8):
        date= '2018-05-'+str(15+t)
        # sql = '''
        #         Insert overwrite table la_shitu_analysis.shitu_churn
        #         select role_id
        #         ,if(tmp<=-7,if(churnDate='',date_add('%s',%d),concat_ws(',',date_add('%s',%d),churnDate)),churnDate)
        #         ,if(tmp<=-7,10000,tmp)
        #         from (
        #         select if(a.role_id is NULL,b.role_id,a.role_id) as role_id
        #         ,if(a.role_id is NULL,'',a.churnDate) as churnDate
        #         ,if(a.role_id is NULL,0,if(b.role_id is NULL,a.tmp-1,0)) as tmp from
        #
        #         la_shitu_analysis.shitu_churn a
        #
        #         full outer join
        #
        #         (select role_id from
        #         ladb.la_bi_login_role
        #         where ds=date_add('%s',%d)
        #         group by role_id)b
        #
        #         on a.role_id=b.role_id
        #         )c
        #     '''%(date,t,date,t,date,t)
        # sql ='''
        #         Insert overwrite table tmp.wangkai_uno_feature_v2 partition(ds='%s')
        #         SELECT serialid,getusetimemin,getusetimesum/getcount as gettimeaverage,getusetimemax
        #         ,postusetimemin,postusetimesum/postcount as posttimeaverage,postusetimemax
        #         ,unocount,getcount,postcount,postovercount,postovercountmagic,postovercountpower
        #         ,arguecount,arguehappencount,arguesuccesscount,roomplaylogcount
        #         from
        #         (
        #         SELECT serialid
        #         ,min(if(typestr='CatchUnoCardResult',get_json_object(infostr,'$.usetime'),0)) as getusetimemin
        #         ,min(if(typestr='PlayUnoCardResult',get_json_object(infostr,'$.usetime'),0)) as postusetimemin
        #         ,max(if(typestr='CatchUnoCardResult',get_json_object(infostr,'$.usetime'),0)) as getusetimemax
        #         ,max(if(typestr='PlayUnoCardResult',get_json_object(infostr,'$.usetime'),0)) as postusetimemax
        #         ,sum(if(typestr='CatchUnoCardResult',get_json_object(infostr,'$.usetime'),0)) as getusetimesum
        #         ,sum(if(typestr='PlayUnoCardResult',get_json_object(infostr,'$.usetime'),0)) as postusetimesum
        #         ,sum(if(typestr='CatchUnoCardResult',1,0)) as getcount
        #         ,sum(if(typestr='PlayUnoCardResult',1,0)) as postcount
        #         ,sum(if(typestr='PlayUnoCardResult',if(get_json_object(infostr,'$.unodeclared')=='true',1,0),0)) as unocount
        #         ,sum(if(typestr='PlayUnoCardResult',if(get_json_object(infostr,'$.usetime')>=10,1,0),0)) as postovercount
        #         ,sum(if(typestr='PlayUnoCardResult',if(get_json_object(infostr,'$.usetime')>=10 and get_json_object(infostr,'$.cardtype') in (1,2),1,0),0)) as postovercountmagic
        #         ,sum(if(typestr='PlayUnoCardResult',if(get_json_object(infostr,'$.usetime')>=10 and get_json_object(infostr,'$.cardtype') in (101,102,103,104,201,202,203,204,301,302,303,304),1,0),0)) as postovercountpower
        #         ,sum(if(typestr='SendChallengeWildFourResult',1,0)) as arguecount
        #         ,sum(if(typestr='SendChallengeWildFourResult' and get_json_object(infostr,'$.ischallenge')='true',1,0)) as arguehappencount
        #         ,sum(if(typestr='SendChallengeWildFourResult' and get_json_object(infostr,'$.result')='true',1,0)) as arguesuccesscount
        #         ,count(*) as roomplaylogcount
        #         ,'%s' as ds
        #         from tmp.unoroomplayreviewonelog
        #         where ds='%s'
        #         group by serialid
        #     )a
        #     '''%(date,date,date)
        sql = '''select * from tmp.wangkai_uno_feature_v2 where ds='%s';'''%(date)

        result = hive_client.query(sql)


        f=open('wangkai_uno_feature_v2.txt','a+')
        f.write('\n'.join(['\t'.join([str(y) for y in x]) for x in result]))
        f.write('\n')
        f.close()

    hive_client.close()
