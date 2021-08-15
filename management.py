from util import Util
from repository import DataBase
from datetime import datetime
from flask import jsonify

class Management:
    def add():
        property_id = Util.get_field('property_id', 'int')
        price = Util.get_field('price', 'float')
        tax_rate = Util.get_field('tax_rate', 'float')
        property_tax = Util.get_field('property_tax', 'float')
        is_available = Util.get_field('is_available', 'bool')
        date_now = datetime.now()

        query = """INSERT INTO public."Management"(
                    property_id, price, tax_rate, property_tax, created_on, is_available)
                    VALUES ({}, {}, {}, {}, \'{}\', {}); """.format(property_id, price, tax_rate, property_tax, date_now, is_available)    
        DataBase.insert(query)
        return('ok')

    def get():
        id = Util.get_field('id', 'int')
        query = 'select * from "Management" where Id = {} '.format(id)
        data = DataBase.select(query)    
        if(data):
            return jsonify(data[0])
        return {}