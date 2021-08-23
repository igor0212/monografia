from Repository.Database import DataBase
from Util import Log

class Property:
    def get_all():
        try:
            query = 'select * from "Property"'
            return DataBase.select(query)           
        except Exception as ex:
            Log.print("Property Repository - get_all error: {}".format(ex), True)

    def get_all_new_ad_and_not_sold():
        try:
            query = 'select * from "Property" where new_ad = True and True = (select is_available from "Management" where partner_id = "Property".partner_id order by created_on desc limit 1)'
            return DataBase.select(query)        
        except Exception as ex:
            Log.print("Property Repository - get_all_new_ad_and_not_sold error: {}".format(ex), True)

    def get_by_partner_id(id):
        try:
            query = 'select * from "Property" where partner_id = {}'.format(id)
            return DataBase.select(query)                   
        except Exception as ex:
            Log.print("Property Repository - get_by_partner_id error: {}".format(ex), True)

    def add(partner_id, partner_code, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number, new_ad=False):
        try:
            return """INSERT INTO public."Property"(partner_id, partner_code, type_id, district_id, city_id, goal_id, "number", street, size, bedroom_number, room_number, bath_number, parking_number, new_ad) 
                      VALUES ({}, \'{}\', {}, {}, {}, {}, \'{}\', \'{}\', {}, {}, {}, {}, {}, {}); """.format(partner_id, partner_code, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, 
                                                                                                              room_number, bath_number, parking_number, new_ad)
        except Exception as ex:
            Log.print("Property Repository - add error: {}".format(ex), True)
                                                                                                          
    def add_by_query(query):
        try:
            DataBase.insert(query)
        except Exception as ex:
            Log.print("Property Repository - add_by_query error: {}".format(ex), True)