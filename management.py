from util import Util
from repository import DataBase
from datetime import datetime
from flask import jsonify

class Management:
    def add(property_id=0, price=0, tax_rate=0, property_tax=0, is_available=False):        
        property_id = property_id if property_id else Util.get_field('property_id', 'int')
        price = price if price else Util.get_field('price', 'float')        
        tax_rate = tax_rate if tax_rate else Util.get_field('tax_rate', 'float')        
        property_tax = property_tax if property_tax else Util.get_field('property_tax', 'float')        
        is_available = is_available if is_available else Util.get_field('is_available', 'bool')               
        date_now = datetime.now()

        query = """INSERT INTO public."Management"(
                    property_id, price, tax_rate, property_tax, created_on, is_available)
                    VALUES ({}, {}, {}, {}, \'{}\', {})""".format(property_id, price, tax_rate, property_tax, date_now, is_available)    
        return DataBase.insert(query)        

    def get():
        id = Util.get_field('id', 'int')
        query = 'select * from "Management" where Id = {} '.format(id)
        data = DataBase.select(query)    
        if(data):
            return jsonify(data[0])
        return {}