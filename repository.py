import psycopg2
from util import Util

class DataBase:    
    def select(query, args=(), one=False):
        try:         
            conn = psycopg2.connect(host=Util.host, database=Util.database, user=Util.user, password=Util.password)   
            cursor = conn.cursor()
            cursor.execute(query, args)
            r = [dict((cursor.description[i][0], value) \
                    for i, value in enumerate(row)) for row in cursor.fetchall()]
            cursor.connection.close()
            return (r[0] if r else None) if one else r
        except Exception as ex:
            print("DataBase Error: Query select error - {}".format(ex))

    def insert(query):
        try:            
            conn = psycopg2.connect(host=Util.host, database=Util.database, user=Util.user, password=Util.password)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()                        
            cursor.close()            
        except Exception as ex:
            print("DataBase Error: Query insert error - {}".format(ex))
        finally:
            if conn is not None:
                conn.close()       