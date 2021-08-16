from repository import DataBase
from datetime import datetime

class Management:
    def add(partner_id, price, tax_rate, property_tax, is_available):                
        date_now = datetime.now()
        query = """INSERT INTO public."Management"(
                    partner_id, price, tax_rate, property_tax, created_on, is_available)
                    VALUES (\'{}\', {}, {}, {}, \'{}\', {}); """.format(partner_id, price, tax_rate, property_tax, date_now, is_available)    
        return query

    def get(id):        
        query = 'select * from "Management" where Id = {} '.format(id)
        data = DataBase.select(query)    
        if(data):
            return data[0]
        return {}

    def get_all():        
        query = 'select * from "Management"'
        data = DataBase.select(query)    
        if(data):
            return data
        return []

    def get_by_partner_id(id):        
        query = 'select * from "Management" where partner_id = {} order by created_on desc'.format(id)
        data = DataBase.select(query)    
        if(data):
            return data[0]
        return {}