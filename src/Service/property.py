from Repository.property import Property as RepositoryProperty
from util import Util, Log

class Property:
    def get_all():
        try:
            data = RepositoryProperty.get_all()
            if(data):
                return data
            return []    
        except Exception as ex:
            error = "Partner Service - get_all error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)            
    
    def get_all_new_ad():
        try:
            data = RepositoryProperty.get_all_new_ad()
            if(data):
                return data
            return []
        except Exception as ex:
            error = "Partner Service - get_all_new_ad error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def get_by_partner_id(id):
        try:
            data = RepositoryProperty.get_by_partner_id(id)          
            if(data):
                return data[0]
            return {}     
        except Exception as ex:
            error = "Partner Service - get_by_partner_id error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)  

    def get_by_partner_code(code):
        try:
            data = RepositoryProperty.get_by_partner_code(code)          
            if(data):
                return data[0]
            return {}     
        except Exception as ex:
            error = "Partner Service - get_by_partner_code error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)           

    def add(partner_id, partner_code, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number, new_ad):
        try:
            return RepositoryProperty.add(partner_id, partner_code, type_id, district_id, city_id, goal_id, number,  Util.format(street), size, bedroom_number, room_number, bath_number, parking_number, new_ad)          
        except Exception as ex:
            error = "Partner Service - add error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def add_by_query(query):
        try:
            if(query):
                RepositoryProperty.add_by_query(query)          
        except Exception as ex:
            error = "Partner Service - add_by_query error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)