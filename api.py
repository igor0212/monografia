import flask
from flask import request, jsonify
from util import JSONEncoder
from repository import DataBase
from management import Management
from city import City
from district import District
from property import Property
from partner import Partner
from util import Util

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
        return jsonify(Property.get_all())
   
    @app.route('/api/property', methods=['GET'])
    def api_property():            
        id = Util.get_field('id', 'int')
        return jsonify(Property.get(id))

    """ 
        Management Control
    """
    @app.route('/api/management/all', methods=['GET'])
    def api_management_all():
        return jsonify(Management.get_all())    

    @app.route('/api/management', methods=['GET'])
    def api_management():    
        id = Util.get_field('id', 'int')
        return jsonify(Management.get(id))

    """ 
        City Control
    """
    @app.route('/api/city/all', methods=['GET'])
    def api_city_all():
        return jsonify(City.get_all())

    @app.route('/api/city', methods=['GET'])
    def api_city():
        id = Util.get_field('id', 'int')
        return jsonify(City.get(id))

    """ 
        District Control
    """
    @app.route('/api/district/all', methods=['GET'])
    def api_district_all():
        return jsonify(District.get_all())

    @app.route('/api/district', methods=['GET'])
    def api_district():    
        id = Util.get_field('id', 'int')
        return jsonify(District.get(id))

    """ 
        Partner Control
    """
    @app.route('/api/partner', methods=['GET'])
    def api_partner():
        code = Util.get_field('code', 'str')             
        return jsonify(Partner.get_by_code(code))

    @app.route('/api/partner/sold', methods=['GET'])
    def api_partner_sold():        
        return Partner.check_sold()

    @app.route('/api/partner/street', methods=['GET', 'POST'])
    def api_partner_street():
        goal = Util.get_field('goal', 'str')
        type = Util.get_field('type', 'str')        
        name = Util.get_field('name', 'str')
        city = Util.get_field('city', 'str')
        location = 'logradouros'
        
        if request.method=='GET':       
            return Partner.get(goal, type, location, name, city)
        elif request.method=='POST':
            return Partner.add(goal, type, location, name, city)   

    @app.route('/api/partner/district', methods=['GET', 'POST'])
    def api_partner_district():
        goal = Util.get_field('goal', 'str')
        type = Util.get_field('type', 'str')        
        name = Util.get_field('name', 'str')
        city = Util.get_field('city', 'str')
        location = 'bairros'

        if request.method=='GET':        
            return Partner.get(goal, type, location, name, city)
        elif request.method=='POST':
            return Partner.add(goal, type, location, name, city)       
        
    app.run()	
    