from Repository.Management import Management as RepositoryManagement
from datetime import datetime
from Util import Log

class Management:
    def get_all():    
        try:            
            data = RepositoryManagement.get_all()    
            if(data):
                return data
            return []
        except Exception as ex:
            Log.print("Management Service - get_all error: {}".format(ex), True)

    def get_by_partner_id(id):
        try:
            data = RepositoryManagement.get_by_partner_id(id)
            if(data):
                return data[0]
            return {}
        except Exception as ex:
            Log.print("Management Service - get_by_partner_id error: {}".format(ex), True)

    def add(partner_id, price, tax_rate, property_tax, is_available):
        try:
            date_now = datetime.now()                     
            return RepositoryManagement.add(partner_id, price, tax_rate, property_tax, is_available, date_now)      
        except Exception as ex:
            Log.print("Management Service - add error: {}".format(ex), True)