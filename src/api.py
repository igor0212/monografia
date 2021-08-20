import flask
from flask import jsonify
from Service.management import Management
from Service.city import City
from Service.district import District
from Service.property import Property
from Service.partner import Partner
from util import File, Util, JSONEncoder

class Api:
    app = flask.Flask(__name__)
    app.json_encoder = JSONEncoder

    @app.errorhandler(404)
    def page_not_found(e):
        return "<h1>404</h1><p>The resource could not be found.</p>", 404

    """ 
        District Controller
    """
    @app.route('/api/district/all', methods=['GET'])
    def api_district_all():
        return jsonify(District.get_all())

    @app.route('/api/district', methods=['GET'])
    def api_district():    
        id = Util.get_field('id', 'int')
        return jsonify(District.get_by_id(id))
    
    """ 
        City Controller
    """
    @app.route('/api/city/all', methods=['GET'])
    def api_city_all():
        return jsonify(City.get_all())

    @app.route('/api/city', methods=['GET'])
    def api_city():
        id = Util.get_field('id', 'int')
        return jsonify(City.get_by_id(id))

    """ 
        Property Controller
    """
    @app.route('/api/property/all', methods=['GET'])
    def api_property_all():        
        return jsonify(Property.get_all())
   
    @app.route('/api/property', methods=['GET'])
    def api_property():            
        id = Util.get_field('partner_id', 'int')
        return jsonify(Property.get_by_partner_id(id))

    """ 
        Management Controller
    """
    @app.route('/api/management/all', methods=['GET'])
    def api_management_all():
        return jsonify(Management.get_all())    

    @app.route('/api/management', methods=['GET'])
    def api_management():    
        id = Util.get_field('partner_id', 'int')
        return jsonify(Management.get_by_partner_id(id))

    """ 
        Partner Controller
    """
    @app.route('/api/partner', methods=['GET'])
    def api_partner():
        code = Util.get_field('code', 'str')             
        return jsonify(Partner.get_properties_by_code(code))

    @app.route('/api/partner/sold', methods=['PATCH'])
    def api_partner_sold():        
        Partner.check_property_sold()
        return('ok')    

    @app.route('/api/partner/district', methods=['POST'])
    def api_partner_district():
        Partner.search_properties_by_district()               
        return('ok')
        
    app.run()	
    