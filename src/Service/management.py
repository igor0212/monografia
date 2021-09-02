from Repository.management import Management as RepositoryManagement
from datetime import datetime
from util import Log

class Management:
    def get_all():    
        try:            
            data = RepositoryManagement.get_all()    
            if(data):
                return data
            return []
        except Exception as ex:
            error = "Management Service - get_all error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def get_by_partner_id(id):
        try:
            data = RepositoryManagement.get_by_partner_id(id)
            if(data):
                return data[0]
            return {}
        except Exception as ex:
            error = "Management Service - get_by_partner_id error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def add(partner_id, price, tax_rate, property_tax, is_available):
        try:
            date_now = datetime.now()                     
            return RepositoryManagement.add(partner_id, price, tax_rate, property_tax, is_available, date_now)      
        except Exception as ex:
            error = "Management Service - add error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)           