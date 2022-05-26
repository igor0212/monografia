import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from flask import request
from unidecode import unidecode
from datetime import datetime
import flask
import decimal
import dateutil.relativedelta

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

    def format2(search):
        return unidecode(str(search).lower().replace("'", "''")) 

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
    def record_insert(query):    
        date_now = datetime.now()
        text = "\n\n -------------------------------------------------------- Script shot in {} ------------------------------------------------------------------------------------------ \n\n {} \n\n".format(date_now, query)
        try:
            path = "log/{}.sql".format(datetime.now().date())
            File.record(text, path)
        except:
            path = "../log/{}.sql".format(datetime.now().date())
            File.record(text, path)            

    def record_log(log, is_error):
        date_now = datetime.now()
        type = "Erro" if is_error else "Log"
        text = "Date: {}\n{}: {} \n\n".format(date_now, type, log)     
        try:
            path = "log/{}.txt".format(datetime.now().date())            
            File.record(text, path)
        except:
            path = "../log/{}.txt".format(datetime.now().date())            
            File.record(text, path)

    def record(text, path):
        with open(path, 'a') as file:
            file.write(text)
            file.close()

class Cache:    
    def record_district(name, liq, month):
        name_fmt = unidecode(name.replace(" ", "-"))
        text = "{} {}\n".format(name_fmt, liq)
        try:            
            file_name = "cache/all/district{}.txt".format(month)
            File.record(text, file_name)        
        except:
            file_name = "../cache/all/district{}.txt".format(month)
            File.record(text, file_name)        

    def record_region(name, liq, month):
        name_fmt = unidecode(name.replace(" ", "-"))
        text = "{} {}\n".format(name_fmt, liq)
        try:                    
            file_name = "cache/all/region{}.txt".format(month)
            File.record(text, file_name)
        except:
            file_name = "../cache/all/region{}.txt".format(month)
            File.record(text, file_name)
    
    def record_street(name, liq, month):
        name_fmt = unidecode(name.replace(" ", "-"))
        text = "{} {}\n".format(name_fmt, liq)
        try:            
            file_name = "cache/all/street{}.txt".format(month)
            File.record(text, file_name)            
        except:
            file_name = "../cache/all/street{}.txt".format(month)
            File.record(text, file_name)          

    def file_to_dic(path):        
        try:
            dictionary = {}
            file = open(path, 'r')        
            for line in file:
                key, value = line.split()
                dictionary[key] = value
            file.close()
            return dictionary
        except:
            file = open(path, 'a')
            file.close()
            return {}

    def get_cache_district(month):
        try:
            file_name = "cache/all/district{}.txt".format(month)        
            return Cache.file_to_dic(file_name)
        except:
            file_name = "../cache/all/district{}.txt".format(month)        
            return Cache.file_to_dic(file_name)
    
    def get_cache_region(month):
        try:
            file_name = "cache/all/region{}.txt".format(month)        
            return Cache.file_to_dic(file_name)
        except:
            file_name = "../cache/all/region{}.txt".format(month)        
            return Cache.file_to_dic(file_name)
    
    def get_cache_street(month):
        try:
            file_name = "cache/all/street{}.txt".format(month)        
            return Cache.file_to_dic(file_name)
        except:
            file_name = "../cache/all/street{}.txt".format(month)        
            return Cache.file_to_dic(file_name)

    def get_cache_district_name(name, month):
        name_fmt = unidecode(name.replace(" ", "-"))
        try:            
            file_name = "cache/district/{}_{}.txt".format(name_fmt, month)            
            file = open(file_name, "r")        
            liquidity = file.read()
            file.close()
            return liquidity
        except:
            try:
                file_name = "../cache/district/{}_{}.txt".format(name_fmt, month)            
                file = open(file_name, "r")        
                liquidity = file.read()
                file.close()
                return liquidity
            except:
                return 0

    def set_cache_district_name(name, month, liq):
        name_fmt = unidecode(name.replace(" ", "-"))
        try:            
            file_name = "cache/district/{}_{}.txt".format(name_fmt, month)
            File.record(str(liq), file_name)
        except:
            file_name = "../cache/district/{}_{}.txt".format(name_fmt, month)
            File.record(str(liq), file_name)

    def get_cache_street_name(name, month):
        name_fmt = unidecode(name.replace(" ", "-"))
        try:            
            file_name = "cache/street/{}_{}.txt".format(name_fmt, month)           
            file = open(file_name, "r")        
            liquidity = file.read()
            file.close()
            return liquidity
        except:
            try:                
                file_name = "../cache/street/{}_{}.txt".format(name_fmt, month)           
                file = open(file_name, "r")        
                liquidity = file.read()
                file.close()
                return liquidity
            except:
                return 0

    def set_cache_street_name(name, month, liq):
        name_fmt = unidecode(name.replace(" ", "-"))
        try:            
            file_name = "cache/street/{}_{}.txt".format(name_fmt, month)
            File.record(str(liq), file_name)
        except:
            file_name = "../cache/street/{}_{}.txt".format(name_fmt, month)
            File.record(str(liq), file_name)

    def get_cache_region_name(name, month):
        name_fmt = unidecode(name.replace(" ", "-"))
        try:            
            file_name = "cache/region/{}_{}.txt".format(name_fmt, month)            
            file = open(file_name, "r")            
            liquidity = file.read()
            file.close()
            return liquidity
        except:
            try:
                file_name = "../cache/region/{}_{}.txt".format(name_fmt, month)            
                file = open(file_name, "r")            
                liquidity = file.read()
                file.close()
                return liquidity
            except:
                return 0

    def set_cache_region_name(name, month, liq):
        name_fmt = unidecode(name.replace(" ", "-"))
        try:
            file_name = "cache/region/{}_{}.txt".format(name_fmt, month)
            File.record(str(liq), file_name)
        except:
            file_name = "../cache/region/{}_{}.txt".format(name_fmt, month)
            File.record(str(liq), file_name)

class Enum:
    type = {'Apartamento': 1, 'Casa': 2 }
    goal = {'venda': 1, 'aluguel': 2 }   
    city = {'Belo Horizonte': 1}

class Log:
    def print(text, is_error=False, show_screen=True):
        File.record_log(text, is_error)
        if(show_screen):
            print(text)

class Date:
    def get_mininum_date(month):
        date_now = datetime.now()
        date = date_now - dateutil.relativedelta.relativedelta(months=month)
        return date.date()

    def sum_date_by_month(date, month):           
        response = date + dateutil.relativedelta.relativedelta(months=month)        
        return response
