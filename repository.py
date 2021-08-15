import psycopg2

def db(database_name='monografia'):        
        return psycopg2.connect(host='localhost', database=database_name, user='postgres', password='@Eliane9455')

class DataBase():
    def select(query, args=(), one=False):
        try:
            cur = db().cursor()
            cur.execute(query, args)
            r = [dict((cur.description[i][0], value) \
                    for i, value in enumerate(row)) for row in cur.fetchall()]
            cur.connection.close()
            return (r[0] if r else None) if one else r
        except:
            return "Error: Query select error"

    def insert(query):
        try:
            conn = db()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
            conn.close()
        except:
            return "Error: Query insert error"