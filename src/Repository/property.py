from Repository.Database import DataBase

class Property:
    def get_all():        
        query = 'select * from "Property"'
        return DataBase.select(query)           

    def get_all_new_ad():        
        query = 'select * from "Property" where new_ad = True'
        return DataBase.select(query)        

    def get_by_partner_id(id):
        query = 'select * from "Property" where partner_id = {}'.format(id)
        return DataBase.select(query)                   

    def add(partner_id, partner_code, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number, new_ad=False):
        return """INSERT INTO public."Property"(partner_id, partner_code, type_id, district_id, city_id, goal_id, "number", street, size, bedroom_number, room_number, bath_number, parking_number, new_ad) 
                  VALUES ({}, \'{}\', {}, {}, {}, {}, \'{}\', \'{}\', {}, {}, {}, {}, {}, {}); """.format(partner_id, partner_code, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, 
                                                                                                          room_number, bath_number, parking_number, new_ad)
                                                                                                          
    def add_by_query(query):
        DataBase.insert(query)