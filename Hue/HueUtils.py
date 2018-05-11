from impala import dbapi


class DataSource(object):
    def __init__(self, host,port):
        super(DataSource,self).__init__()
        self.host = host
        self.port = port

    def get_imp_conn(self):
        try:
            imp_connection = dbapi.connect(self.host,self.port,timeout = 10)
            return imp_connection
        except Exception as e:
            print('error:Can not get impala connection')
            print(e)

    def exec_sql_in_impala_handler(self,sql=None,param_list=None):
        cursor = None
        conn = None
        try:
            conn = self.get_imp_conn()
            cursor = conn.cursor()
            cursor.execute(sql,param_list)
            fields = [x[0] for x in cursor.description]
            res = [dict(zip(fields, row)) for row in cursor]
            return res
        except Exception as e:
            print(e)
        finally:
            if(cursor):
                cursor.close()
            if(conn):
                conn.close()

class DataSource2(object):
    def __init__(self, host,port):
        # super(DataSource,self).__init__()
        self.host = host
        self.port = port

    def get_imp_conn(self):
        try:
            imp_connection = dbapi.connect(self.host,self.port,timeout = 10)
            return imp_connection
        except Exception as e:
            print('error:Can not get impala connection')
            print(e)

    def exec_sql_in_impala_handler(self,sql=None,param_list=None):
        cursor = None
        conn = None
        try:
            conn = self.get_imp_conn()
            cursor = conn.cursor()
            cursor.execute(sql,param_list)
            fields = [x[0] for x in cursor.description]
            res = [dict(zip(fields, row)) for row in cursor]
            return res
        except Exception as e:
            print(e)
        finally:
            if(cursor):
                cursor.close()
            if(conn):
                conn.close()

if __name__ == '__main__':
    sql = '''SELECT * from tmp.wangkai_uno_feature_v1 where ds='2018-04-12' limit 100 '''
    handler = DataSource('59.111.128.6',21051)
    result = handler.exec_sql_in_impala_handler(sql)
    print(result)