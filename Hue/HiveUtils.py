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
                SELECT min(time),server,iid,concat_ws(',',collect_set(cast(id as STRING))) 
                from qndb.h_guanning_result
                where ds='%s'
                group by server,iid;
              '''%(date,date)
        result = hive_client.action(sql)
        # f=open('shitu_all.txt','a+')
        # f.write('\n'.join(['\t'.join([str(y) for y in x]) for x in result]))
        # f.write('\n')
        # f.close()
    hive_client.close()







