import flask
from flask import request, jsonify
from util import JSONEncoder, Util
from repository import DataBase
from datetime import datetime

app = flask.Flask(__name__)
app.json_encoder = JSONEncoder

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

""" 
    Management Control
"""

@app.route('/api/management/all', methods=['GET'])
def api_management_all():
    query = 'select * from "Management"'
    my_query = DataBase.select(query)
    return jsonify(my_query)   

def get_management():
    id = Util.get_field('id', 'int')
    query = 'select * from "Management" where Id = {} '.format(id)
    data = DataBase.select(query)
    result = {}
    if(data):
        result = jsonify(data[0])
    return result

def add_management():
    property_id = Util.get_field('property_id', 'int')
    price = Util.get_field('price', 'float')
    tax_rate = Util.get_field('tax_rate', 'float')
    property_tax = Util.get_field('property_tax', 'float')
    is_available = Util.get_field('is_available', 'bool')
    date_now = datetime.now()

    query = """INSERT INTO public."Management"(
            	property_id, price, tax_rate, property_tax, created_on, is_available)
	            VALUES ({}, {}, {}, {}, \'{}\', {}); """.format(property_id, price, tax_rate, property_tax, date_now, is_available)    
    DataBase.insert(query)
    return('ok')

@app.route('/api/management', methods=['GET', 'POST'])
def api_management():    
    if request.method=='GET':        
        return get_management()
    elif request.method=='POST':
        return add_management()

app.run()	