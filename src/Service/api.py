import flask
from flask import jsonify
from management import Management
from city import City
from district import District
from property import Property
from partner import Partner
from liquidity import Liquidity
from region import Region
from util import Util, JSONEncoder

app = flask.Flask(__name__)
app.json_encoder = JSONEncoder

class Api:        
    
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

    @app.route('/api/partner/district/name', methods=['PATCH'])
    def api_partner_district_name():
        name = Util.get_field('name', 'str')
        Partner.search_properties_by_district_name(name)               
        return('ok')

    @app.route('/api/partner/sold/code', methods=['PATCH'])
    def api_partner_sold_code():
        code = Util.get_field('code', 'str')     
        Partner.check_property_sold_by_code(code)
        return('ok')  

    """ 
        Liquidity Controller
    """
    @app.route('/api/liquidity/district', methods=['GET'])
    def api_liquidity_district():        
        name = Util.get_field('name', 'str')
        month = Util.get_field('month', 'int')        
        return jsonify(Liquidity.get_district_liquidity(name, month))

    @app.route('/api/liquidity/district/all', methods=['GET'])
    def api_liquidity_district_all():                
        month = Util.get_field('month', 'int')
        return jsonify(Liquidity.get_by_district_all(month))

    @app.route('/api/liquidity/street', methods=['GET'])
    def api_liquidity_street():        
        name = Util.get_field('name', 'str')
        month = Util.get_field('month', 'int')
        return jsonify(Liquidity.get_street_liquidity(name, month))

    @app.route('/api/liquidity/region', methods=['GET'])
    def api_liquidity_region():        
        name = Util.get_field('name', 'str')
        month = Util.get_field('month', 'int')
        return jsonify(Liquidity.get_region_liquidity(name, month))

    @app.route('/api/liquidity/region/all', methods=['GET'])
    def api_liquidity_region_all():                
        month = Util.get_field('month', 'int')
        return jsonify(Liquidity.get_by_region_all(month))

    @app.route('/api/liquidity/street/all', methods=['GET'])
    def api_liquidity_street_all():                
        month = Util.get_field('month', 'int')
        return jsonify(Liquidity.get_by_street_all(month))   

    """
        Region Controller
    """
    @app.route('/api/region/link', methods=['GET'])
    def api_region():                
        Region.link()
        return jsonify({})
        
    app.run()	
    