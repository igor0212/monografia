from Repository.Database import DataBase
from Util import Log

class Management:
    def get_all():  
        try:      
            query = 'select * from "Management"'
            return DataBase.select(query)
        except Exception as ex:
            Log.print("Management Repository - get_all error: {}".format(ex), True)

    def get_by_partner_id(id):
        try:
            query = 'select * from "Management" where partner_id = {} order by created_on desc'.format(id)
            return DataBase.select(query)            
        except Exception as ex:
            Log.print("Management Repository - get_by_partner_id error: {}".format(ex), True)

    def add(partner_id, price, tax_rate, property_tax, is_available, date_now):   
        try:                     
            return 'INSERT INTO public."Management"(partner_id, price, tax_rate, property_tax, created_on, is_available) VALUES (\'{}\', {}, {}, {}, \'{}\', {}); \n'.format(partner_id, price, tax_rate, property_tax, date_now, is_available)
        except Exception as ex:
            Log.print("Management Repository - add error: {}".format(ex), True)
    