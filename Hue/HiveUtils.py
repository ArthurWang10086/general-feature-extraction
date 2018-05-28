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


    for t in range(21,71):
        date= '2018-02-19'
        sql = '''
                Insert overwrite table la_shitu_analysis.shitu_churn
                select role_id
                ,if(tmp<=-7,if(churnDate='',date_add('%s',%d),concat_ws(',',date_add('%s',%d),churnDate)),churnDate)
                ,if(tmp<=-7,10000,tmp)
                from (
                select if(a.role_id is NULL,b.role_id,a.role_id) as role_id
                ,if(a.role_id is NULL,'',a.churnDate) as churnDate
                ,if(a.role_id is NULL,0,if(b.role_id is NULL,a.tmp-1,0)) as tmp from
                
                la_shitu_analysis.shitu_churn a
                
                full outer join
                
                (select role_id from
                ladb.la_bi_login_role
                where ds=date_add('%s',%d)
                group by role_id)b
                
                on a.role_id=b.role_id
                )c
            '''%(date,t,date,t,date,t)

        print t
        #print result

        result = hive_client.action(sql)

        print t
        #print result

    hive_client.close()
