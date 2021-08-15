import flask
from flask import request, jsonify
from util import JSONEncoder
from repository import DataBase
from management import Management
from city import City
from district import District
from property import Property

class Api:
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
   
    @app.route('/api/property', methods=['GET', 'POST'])
    def api_property():    
        if request.method=='GET':        
            return Property.get()
        elif request.method=='POST':
            return Property.add()

    """ 
        Management Control
    """
    @app.route('/api/management/all', methods=['GET'])
    def api_management_all():
        query = 'select * from "Management"'
        data = DataBase.select(query)
        return jsonify(data)      

    @app.route('/api/management', methods=['GET', 'POST'])
    def api_management():    
        if request.method=='GET':        
            return Management.get()
        elif request.method=='POST':
            return Management.add()

    """ 
        City Control
    """
    @app.route('/api/city/all', methods=['GET'])
    def api_city_all():
        query = 'select * from "City"'
        data = DataBase.select(query)
        return jsonify(data)      

    @app.route('/api/city', methods=['GET', 'POST'])
    def api_city():    
        if request.method=='GET':        
            return City.get()
        elif request.method=='POST':
            return City.add()

    """ 
        District Control
    """
    @app.route('/api/district/all', methods=['GET'])
    def api_district_all():
        query = 'select * from "District"'
        data = DataBase.select(query)
        return jsonify(data)  

    @app.route('/api/district', methods=['GET', 'POST'])
    def api_district():    
        if request.method=='GET':        
            return District.get()
        elif request.method=='POST':
            return District.add()

    app.run()	