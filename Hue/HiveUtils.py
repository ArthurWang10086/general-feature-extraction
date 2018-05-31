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
                    Insert overwrite table qn_guanning.guanninggame
                    partition (ds='%s')
                    SELECT min(time),server,iid,concat_ws(',',collect_set(concat_ws(':',cast(id as STRING),cast(iswin as String))))
                    from qndb.h_guanning_result
                    where ds='%s'
                    group by server,iid
                  '''%(date,date)
        result = hive_client.action(sql)
        # f=open('shitu_all.txt','a+')
        # f.write('\n'.join(['\t'.join([str(y) for y in x]) for x in result]))
        # f.write('\n')
        # f.close()
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
#                     concat_ws(',',cast(avg(iswin) as string),cast(avg(xiulian) as string)
#                     ,cast(avg(total_score) as string),cast(avg(help_num) as string)
#                     ,cast(avg(kill_score) as string),cast(avg(flag_score) as string)
#                     ,cast(avg(xiuwei) as string),cast(avg(equip_score) as string)
#                     ,cast(avg(team_score) as string),cast(avg(killed_score) as string)
#                     ,cast(avg(score_count) as string),cast(avg(grade) as string)
#                     ,cast(avg(class) as string),cast(count(*) as string))
#                     from  qndb.h_guanning_result where ds>='%s' and ds<='%s'
#                     group by server,id
#               '''%(date,(d+datetime.timedelta(6+t)).strftime('%Y-%m-%d'),(d+datetime.timedelta(7+t)).strftime('%Y-%m-%d'))
#     result = hive_client.action(sql)
#     print t