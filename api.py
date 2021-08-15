import flask
from flask import request, jsonify
import psycopg2
import decimal
from datetime import datetime

class MyJSONEncoder(flask.json.JSONEncoder):
    
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return str(obj)
        return super(MyJSONEncoder, self).default(obj)

app = flask.Flask(__name__)
app.json_encoder = MyJSONEncoder

def db(database_name='monografia'):
    return psycopg2.connect(host='localhost', database=database_name, user='postgres', password='@Eliane9455')

def query_select(query, args=(), one=False):
    try:
        cur = db().cursor()
        cur.execute(query, args)
        r = [dict((cur.description[i][0], value) \
                for i, value in enumerate(row)) for row in cur.fetchall()]
        cur.connection.close()
        return (r[0] if r else None) if one else r
    except:
        return "Error: Query select error"

def query_insert(query):
    try:
        conn = db()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        return "Error: Query insert error"

def get_field(name, type):
    try:
        if (type == 'int'):
            field = int(request.args[name])
        elif (type == 'float'):
            field = float(request.args[name])
        elif (type == 'bool'):
            field = bool(request.args[name])
        else:
            return "Error: Type {} not implemented.".format(type)
    except:
        return "Error: No {} field provided. Please specify an {}.".format(name, name)
    return field

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/management/all', methods=['GET'])
def api_management_all():
    query = 'select * from "Management"'
    my_query = query_select(query)
    return jsonify(my_query)   

def get_management():
    id = get_field('id', 'int')
    query = 'select * from "Management" where Id = {} '.format(id)
    data = query_select(query)
    result = {}
    if(data):
        result = jsonify(data[0])
    return result

def add_management():
    property_id = get_field('property_id', 'int')
    price = get_field('price', 'float')
    tax_rate = get_field('tax_rate', 'float')
    property_tax = get_field('property_tax', 'float')
    is_available = get_field('is_available', 'bool')
    date_now = datetime.now()

    query = """INSERT INTO public."Management"(
            	property_id, price, tax_rate, property_tax, created_on, is_available)
	            VALUES ({}, {}, {}, {}, \'{}\', {}); """.format(property_id, price, tax_rate, property_tax, date_now, is_available)    
    query_insert(query)
    return('ok')

@app.route('/api/management', methods=['GET', 'POST'])
def api_management():    
    if request.method=='GET':        
        return get_management()
    elif request.method=='POST':
        return add_management()

app.run()	