import flask
import decimal
from flask import request
from unidecode import unidecode

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

    type = {'Apartamento': 1, 'Casa': 2 }

    goal = {'venda': 1, 'aluguel': 2 }    

    city = {'Belo Horizonte': 1}

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
            field = ""
        return field

    def format_search(search):        
        return unidecode(str(search).lower().replace(" ", "-"))

    def format(search):        
        return unidecode(str(search).replace("'", "''"))

    def get_url(goal, type, location, name, city, state, page):
        if(location == 'logradouros'):
            search = 'logradouro_{}_{}_{}'.format(name, city, state)
        elif(location == 'bairros'):
            search = '{}_{}_{}'.format(name, city, state)
        else:
            return 'Util Error: Location not implemented'

        complement = 'pagina={}'.format(page)

        return 'https://api.casamineira.com.br/busca/imoveis?finalidade={}&tipos[]={}&{}[]={}&{}'.format(Util.format_search(goal), Util.format_search(type), Util.format_search(location), Util.format_search(search), complement)          
    