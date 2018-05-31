import pyhs2
import datetime
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

    d = datetime.datetime.strptime('2018-04-01', '%Y-%m-%d')
    for t in range(0,60):
        date = (d+datetime.timedelta(t)).strftime('%Y-%m-%d')
        sql = '''
                    Insert overwrite table qn_guanning.guanninggamewithfeature
                    partition (ds='%s')
                    
                    select min(time),server,iid
                    ,concat_ws(';',collect_set(if(iswin>0,features,NULL))) as win_features
                    ,concat_ws(';',collect_set(if(iswin<0,features,NULL))) as lose_features
                    from (
                    select a.time,a.server,a.iid,a.id,if(b.features is null,'0,0,0,0,0,0,0,0,0,0,0,0,0,0',b.features) as features,iswin
                    from
                    (
                    SELECT time,server,iid,id,iswin
                    from qndb.h_guanning_result
                    where ds='%s'
                    )a
                    
                    left outer join 
                    (select role_id,features from qn_guanning.guanningpersonal where ds='%s')b
                    on a.id=b.role_id
                    )c
                    group by server,iid
                  '''%(date,date,date)
        result = hive_client.action(sql)
        print t
    hive_client.close()





# d = datetime.datetime.strptime('2018-04-01', '%Y-%m-%d')
# for t in range(0,60):
#     date = (d+datetime.timedelta(t)).strftime('%Y-%m-%d')
#     sql = '''
#                     Insert overwrite table qn_guanning.guanninggame
#                     partition (ds='%s')
#                     SELECT min(time),server,iid,concat_ws(',',collect_set(concat_ws(':',cast(id as STRING),cast(iswin as String))))
#                     from qndb.h_guanning_result
#                     where ds='%s'
#                     group by server,iid
#                   '''%(date,date)
#     result = hive_client.action(sql)

# d = datetime.datetime.strptime('2018-04-01', '%Y-%m-%d')
# for t in range(0,60):
#     date = (d+datetime.timedelta(t)).strftime('%Y-%m-%d')
#     sql = '''
#                 Insert overwrite table qn_guanning.guanningpersonal
#                     partition (ds='%s')
#                     select server,id,
#                         concat_ws(',',cast(avg(round(iswin,2)) as string),cast(avg(round(xiulian,2)) as string)
#                         ,cast(avg(round(total_score,2)) as string),cast(avg(round(help_num,2)) as string)
#                         ,cast(avg(round(kill_score,2)) as string),cast(avg(round(flag_score,2)) as string)
#                         ,cast(avg(round(xiuwei,2)) as string),cast(avg(round(equip_score,2)) as string)
#                         ,cast(avg(round(team_score,2)) as string),cast(avg(round(killed_score,2)) as string)
#                         ,cast(avg(round(score_count,2)) as string),cast(avg(round(grade,2)) as string)
#                         ,cast(avg(round(class,2)) as string),cast(round(count(*),2) as string))
#                     from  qndb.h_guanning_result where ds>='%s' and ds<='%s'
#                     group by server,id
#               '''%((d+datetime.timedelta(7+t)).strftime('%Y-%m-%d'),date,(d+datetime.timedelta(6+t)).strftime('%Y-%m-%d'))
#     result = hive_client.action(sql)
#     print t

# d = datetime.datetime.strptime('2018-04-01', '%Y-%m-%d')
# for t in range(0,1):
#     date = (d+datetime.timedelta(t)).strftime('%Y-%m-%d')
#     sql = '''
#                     select * from qn_guanning.guanninggame where ds<='2018-05-29'
#
#                   '''
#     result = hive_client.query(sql)
#     print t
#     f=open('guanninggame.txt','a+')
#     f.write('\n'.join(['\t'.join([str(y) for y in x]) for x in result]))
#     f.write('\n')
#     f.close()