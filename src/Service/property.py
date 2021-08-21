from Repository.Property import Property as RepositoryProperty
from Util import Util

class Property:
    def get_all():
        data = RepositoryProperty.get_all()
        if(data):
            return data
        return []    
    
    def get_all_new_ad():
        data = RepositoryProperty.get_all_new_ad()
        if(data):
            return data
        return []

    def get_by_partner_id(id):
        data = RepositoryProperty.get_by_partner_id(id)          
        if(data):
            return data[0]
        return {}     

    def add(partner_id, partner_code, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number, new_ad):
        return RepositoryProperty.add(partner_id, partner_code, type_id, district_id, city_id, goal_id, number,  Util.format(street), size, bedroom_number, room_number, bath_number, parking_number, new_ad)          

    def add_by_query(query):
        if(query):
            RepositoryProperty.add_by_query(query)          