from Repository.management import Management as RepositoryManagement
from datetime import datetime

class Management:
    def get_all():                
        data = RepositoryManagement.get_all()    
        if(data):
            return data
        return []

    def get_by_partner_id(id):
        data = RepositoryManagement.get_by_partner_id(id)
        if(data):
            return data[0]
        return {}

    def add(partner_id, price, tax_rate, property_tax, is_available):   
        date_now = datetime.now()                     
        return RepositoryManagement.add(partner_id, price, tax_rate, property_tax, is_available, date_now)      