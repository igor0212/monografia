from Repository.database import DataBase
from util import Log

class Property:
    def get_all():
        try:
            query = 'select * from "Property"'
            return DataBase.select(query)           
        except Exception as ex:            
            error = "Property Repository - get_all error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_all_new_ad():
        try:
            query = 'select * from "Property" where new_ad = True'
            return DataBase.select(query)        
        except Exception as ex:
            error = "Property Repository - get_all_new_ad error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def get_by_partner_id(id):
        try:
            query = 'select * from "Property" where partner_id = {}'.format(id)
            return DataBase.select(query)                   
        except Exception as ex:
            error = "Property Repository - get_by_partner_id error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)
    
    def get_by_partner_code(code):
        try:
            query = 'select * from "Property" where partner_code = \'{}\''.format(code)
            return DataBase.select(query)                   
        except Exception as ex:
            error = "Property Repository - get_by_partner_code error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def add(partner_id, partner_code, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number, new_ad=False):
        try:
            return """INSERT INTO public."Property"(partner_id, partner_code, type_id, district_id, city_id, goal_id, "number", street, size, bedroom_number, room_number, bath_number, parking_number, new_ad) 
                      VALUES ({}, \'{}\', {}, {}, {}, {}, \'{}\', \'{}\', {}, {}, {}, {}, {}, {}); """.format(partner_id, partner_code, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, 
                                                                                                              room_number, bath_number, parking_number, new_ad)
        except Exception as ex:            
            error = "Property Repository - add error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)
                                                                                                          
    def add_by_query(query):
        try:
            DataBase.insert(query)
        except Exception as ex:
            error = "Property Repository - add_by_query error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)          