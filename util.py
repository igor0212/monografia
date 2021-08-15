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
                return "Error: Type {} not implemented.".format(type)
        except:
            return "Error: No {} field provided. Please specify an {}.".format(name, name)
        return field
    