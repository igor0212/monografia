import flask
import decimal
from flask import request

class JSONEncoder(flask.json.JSONEncoder):    
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return str(obj)
        return super(JSONEncoder, self).default(obj)

class Util:
    host = 'localhost'
    database = 'monografia'
    user = 'postgres'
    password = '@Eliane9455'

    apartment = 1
    house = 2
    condo = 3

    sell = 1
    rent = 2    

    def get_field(name, type):
        try:
            if (type == 'int'):
                field = int(request.args[name])
            elif (type == 'float'):
                field = float(request.args[name])
            elif (type == 'bool'):                
                field = request.args[name].lower() in ('true', 'True')                
            elif (type == 'str'):
                field = str(request.args[name])
            else:
                return "Util Error: Type {} not implemented.".format(type)
        except:
            return "Util Error: No {} field provided. Please specify an {}.".format(name, name)
        return field

    def format_search(search):        
        return str(search).lower().replace(" ", "-")

    def get_url(goal, type, location, name, city, state):
        if(location == 'logradouros'):
            search = 'logradouro_{}_{}_{}'.format(name, city, state)
        elif(location == 'bairros'):
            search = '{}_{}_{}'.format(name, city, state)
        else:
            return 'Util Error: Location not implemented'

        return 'https://api.casamineira.com.br/busca/imoveis?finalidade={}&tipos[]={}&{}[]={}'.format(Util.format_search(goal), Util.format_search(type), Util.format_search(location), Util.format_search(search))          
    