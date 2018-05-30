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


    for t in range(0,1):
        date= '2018-05-'+str(15+t)
        sql = ''' select 
                    a.server,a.role_id,a.d_role_id,a.seq
                    ,b.churndate,c.chatinfo,d.chatinfo,e.tradeinfo,f.tradeinfo,g.pveinfo
                  from la_shitu_analysis.shitu_seq a
                  left outer join
                    la_shitu_analysis.shitu_churn b 
                  on a.role_id=b.role_id
                  left outer join
                    la_shitu_analysis.shitu_chat_pair c
                  on a.role_id=c.role_id and a.d_role_id=c.d_role_id
                  left outer join
                    la_shitu_analysis.shitu_chat_pair_reversed d
                  on a.role_id=d.role_id and a.d_role_id=d.d_role_id
                  left outer join
                    la_shitu_analysis.shitu_trade_pair e
                  on a.role_id=e.role_id and a.d_role_id=e.d_role_id
                  left outer join
                    la_shitu_analysis.shitu_trade_pair_reversed f
                  on a.role_id=f.role_id and a.d_role_id=f.d_role_id
                  left outer join
                    la_shitu_analysis.shitu_pve_pair g
                  on a.role_id=g.role_id and a.d_role_id=g.d_role_id 
              '''
        result = hive_client.query(sql)
        f=open('shitu_all.txt','a+')
        f.write('\n'.join(['\t'.join([str(y) for y in x]) for x in result]))
        f.write('\n')
        f.close()
    hive_client.close()
