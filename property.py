from repository import DataBase

class Property:
    def get(id):        
        query = 'select * from "Property" where Id = {} '.format(id)
        data = DataBase.select(query)    
        if(data):
            return data[0]
        return {}

    def add(partner_id, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number):
        query = """INSERT INTO public."Property"(
                    partner_id, type_id, district_id, city_id, goal_id, "number", street, size, bedroom_number, room_number, bath_number, parking_number)
                    VALUES (\'{}\', {}, {}, {}, {}, \'{}\', \'{}\', {}, {}, {}, {}, {})""".format(partner_id, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number)                       
        return DataBase.insert(query)

    def get_all(serialize=False):        
        query = 'select * from "Property"'
        data = DataBase.select(query)
        if(data):
            return data
        return []
