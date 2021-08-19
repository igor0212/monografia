from repository import DataBase
from util import Util

class Property:
    def get(id):        
        query = 'select * from "Property" where Id = {} '.format(id)
        data = DataBase.select(query)    
        if(data):
            return data[0]
        return {}

    def add(partner_id, partner_code, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number, new_ad=False):
        query = """INSERT INTO public."Property"(partner_id, partner_code, type_id, district_id, city_id, goal_id, "number", street, size, bedroom_number, room_number, bath_number, parking_number, new_ad) VALUES ({}, \'{}\', {}, {}, {}, {}, \'{}\', \'{}\', {}, {}, {}, {}, {}, {}); """.format(partner_id, partner_code, type_id, district_id, city_id, goal_id, number, Util.format(street), size, bedroom_number, room_number, bath_number, parking_number, new_ad)
        return query

    def get_all():        
        query = 'select * from "Property"'
        data = DataBase.select(query)
        if(data):
            return data
        return []

    def get_valid_property(properties_partner, id):
        response = {}
        for property_partner in properties_partner:
            if(property_partner['id'] == id):
                response = property_partner
                break
        return response

    def get_by_partner_id(id):
        query = 'select * from "Property" where partner_id = {}'.format(id)
        data = DataBase.select(query)           
        if(data):
            return data[0]
        return {} 

    def get_all_new_ad():        
        query = 'select * from "Property" where new_ad = True'
        data = DataBase.select(query)
        if(data):
            return data
        return []
