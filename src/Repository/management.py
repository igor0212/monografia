from Repository.Database import DataBase

class Management:
    def get_all():        
        query = 'select * from "Management"'
        return DataBase.select(query)

    def get_by_partner_id(id):        
        query = 'select * from "Management" where partner_id = {} order by created_on desc'.format(id)
        return DataBase.select(query)            

    def add(partner_id, price, tax_rate, property_tax, is_available, date_now):                        
        return 'INSERT INTO public."Management"(partner_id, price, tax_rate, property_tax, created_on, is_available) VALUES (\'{}\', {}, {}, {}, \'{}\', {}); \n'.format(partner_id, price, tax_rate, property_tax, date_now, is_available)
    