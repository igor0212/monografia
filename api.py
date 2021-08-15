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
    Property Control
"""
@app.route('/api/property/all', methods=['GET'])
def api_property_all():
    query = 'select * from "Property"'
    data = DataBase.select(query)
    return jsonify(data)   

def get_property():
    id = Util.get_field('id', 'int')
    query = 'select * from "Property" where Id = {} '.format(id)
    data = DataBase.select(query)    
    if(data):
        return jsonify(data[0])
    return {}

def add_property():
    partner_id = Util.get_field('partner_id', 'int')
    type_id = Util.get_field('type_id', 'int')
    district_id = Util.get_field('district_id', 'int')
    city_id = Util.get_field('city_id', 'int')
    goal_id = Util.get_field('goal_id', 'int')
    number = Util.get_field('number', 'str')
    street = Util.get_field('street', 'str')
    size = Util.get_field('size', 'int')
    bedroom_number = Util.get_field('bedroom_number', 'int')
    room_number = Util.get_field('room_number', 'int')
    bath_number = Util.get_field('bath_number', 'int')
    parking_number = Util.get_field('parking_number', 'int')    

    query = """INSERT INTO public."Property"(
            	partner_id, type_id, district_id, city_id, goal_id, "number", street, size, bedroom_number, room_number, bath_number, parking_number)
	            VALUES ({}, {}, {}, {}, {}, \'{}\', \'{}\', {}, {}, {}, {}, {}); """.format(partner_id, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number)    
    print(query)
    DataBase.insert(query)
    return('ok')

@app.route('/api/property', methods=['GET', 'POST'])
def api_property():    
    if request.method=='GET':        
        return get_property()
    elif request.method=='POST':
        return add_property()


""" 
    Management Control
"""
@app.route('/api/management/all', methods=['GET'])
def api_management_all():
    query = 'select * from "Management"'
    data = DataBase.select(query)
    return jsonify(data)   

def get_management():
    id = Util.get_field('id', 'int')
    query = 'select * from "Management" where Id = {} '.format(id)
    data = DataBase.select(query)    
    if(data):
        return jsonify(data[0])
    return {}

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