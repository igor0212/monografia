from flask import request
from unidecode import unidecode
from datetime import datetime
import flask
import decimal

class JSONEncoder(flask.json.JSONEncoder):    
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return str(obj)
        return super(JSONEncoder, self).default(obj)

class Util:   
    def get_field(name, type):
        try:
            if (type == 'int'):
                field = int(request.args.get(name, 0))
            elif (type == 'float'):
                field = float(request.args.get(name, 0))
            elif (type == 'bool'):                
                field = request.args.get(name, '').lower() in ('true', 'True')                
            elif (type == 'str'):
                field = str(request.args.get(name, ''))
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

    def validate_number(number):        
        return number if number else 0
    
    def validate_string(string):        
        return string if string else ""         

class File:
    check_property_sold = "../db/scripts/inserts_check_property_sold.sql"
    search_properties_by_district = "../db/scripts/inserts_properties.sql"
    routine = "../db/scripts/inserts_job.sql"    

    def record_insert(query, path):        
        date_now = datetime.now()
        text = "\n\n -------------------------------------------------------- Script shot in {} ------------------------------------------------------------------------------------------ \n\n {} \n\n".format(date_now, query)
        File.record(text, path)

    def record_log(log):
        path = "../log/log.txt"   
        date_now = datetime.now()
        text = "Date: {}\nLog: {} \n\n".format(date_now, log)     
        File.record(text, path)

    def record(text, path):
        with open(path, 'a') as file:
            file.write(text)
            file.close()

class Enum:
    type = {'Apartamento': 1, 'Casa': 2 }
    goal = {'venda': 1, 'aluguel': 2 }   
    city = {'Belo Horizonte': 1}

class Log:
    def print(text, show_screen=True):
        File.record_log(text)
        if(show_screen):
            print(text)