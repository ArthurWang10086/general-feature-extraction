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
    sql = ''
    exec_sql_in_impala_handler()