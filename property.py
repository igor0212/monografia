from util import Util
from repository import DataBase
from flask import jsonify

class Property:
    def get():
        id = Util.get_field('id', 'int')
        query = 'select * from "Property" where Id = {} '.format(id)
        data = DataBase.select(query)    
        if(data):
            return jsonify(data[0])
        return {}

    def add():
        partner_id = Util.get_field('partner_id', 'int')
        type_id = Util.get_field('type_id', 'int')
        district_id = Util.get_field('district_id', 'int')
        city_id = Util.get_field('city_id', 'int')
        goal_id = Util.get_field('goal_id', 'int')
        number = Util.get_field('number', 'str')
        street = Util.get_field('street', 'str')
        size = Util.get_field('size', 'int')
        bedroom_number = Util.get_field('bedroom_number', 'int')
        room_number = Util.get_field('room_number', 'int')
        bath_number = Util.get_field('bath_number', 'int')
        parking_number = Util.get_field('parking_number', 'int')    

        query = """INSERT INTO public."Property"(
                    partner_id, type_id, district_id, city_id, goal_id, "number", street, size, bedroom_number, room_number, bath_number, parking_number)
                    VALUES ({}, {}, {}, {}, {}, \'{}\', \'{}\', {}, {}, {}, {}, {}); """.format(partner_id, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number)        
        DataBase.insert(query)
        return('ok')
