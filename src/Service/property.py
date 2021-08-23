from Repository.Property import Property as RepositoryProperty
from Util import Util, Log

class Property:
    def get_all():
        try:
            data = RepositoryProperty.get_all()
            if(data):
                return data
            return []    
        except Exception as ex:
            error = "Partner Service - get_all error: {}".format(ex)
            Log.print(error, True)
            raise Exception(error)            
    
    def get_all_new_ad_and_not_sold():
        try:
            data = RepositoryProperty.get_all_new_ad_and_not_sold()
            if(data):
                return data
            return []
        except Exception as ex:
            error = "Partner Service - get_all_new_ad_and_not_sold error: {}".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def get_by_partner_id(id):
        try:
            data = RepositoryProperty.get_by_partner_id(id)          
            if(data):
                return data[0]
            return {}     
        except Exception as ex:
            error = "Partner Service - get_by_partner_id error: {}".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def add(partner_id, partner_code, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number, new_ad):
        try:
            return RepositoryProperty.add(partner_id, partner_code, type_id, district_id, city_id, goal_id, number,  Util.format(street), size, bedroom_number, room_number, bath_number, parking_number, new_ad)          
        except Exception as ex:
            error = "Partner Service - add error: {}".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def add_by_query(query):
        try:
            if(query):
                RepositoryProperty.add_by_query(query)          
        except Exception as ex:
            error = "Partner Service - add_by_query error: {}".format(ex)
            Log.print(error, True)
            raise Exception(error)