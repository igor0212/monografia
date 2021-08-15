from repository import DataBase
from datetime import datetime
from flask import jsonify

class Management:
    def add(property_id, price, tax_rate, property_tax, is_available):                
        date_now = datetime.now()
        query = """INSERT INTO public."Management"(
                    property_id, price, tax_rate, property_tax, created_on, is_available)
                    VALUES ({}, {}, {}, {}, \'{}\', {})""".format(property_id, price, tax_rate, property_tax, date_now, is_available)    
        return DataBase.insert(query)        

    def get(id):        
        query = 'select * from "Management" where Id = {} '.format(id)
        data = DataBase.select(query)    
        if(data):
            return jsonify(data[0])
        return {}