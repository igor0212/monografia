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

    def add(partner_id=0, type_id=0, district_id=0, city_id=0, goal_id=0, number='', street='', size=0, bedroom_number=0, room_number=0, bath_number=0, parking_number=0):
        partner_id = partner_id if partner_id else Util.get_field('partner_id', 'int')
        type_id = type_id if type_id else Util.get_field('type_id', 'int')
        district_id = district_id if district_id else Util.get_field('district_id', 'int')
        city_id = city_id if city_id else Util.get_field('city_id', 'int')
        goal_id = goal_id if goal_id else Util.get_field('goal_id', 'int')
        number = number if number else Util.get_field('number', 'str')
        street = street if street else Util.get_field('street', 'str')
        size = size if size else Util.get_field('size', 'int')
        bedroom_number = bedroom_number if bedroom_number else Util.get_field('bedroom_number', 'int')
        room_number = room_number if room_number else Util.get_field('room_number', 'int')
        bath_number = bath_number if bath_number else Util.get_field('bath_number', 'int')
        parking_number = parking_number if parking_number else Util.get_field('parking_number', 'int')    

        query = """INSERT INTO public."Property"(
                    partner_id, type_id, district_id, city_id, goal_id, "number", street, size, bedroom_number, room_number, bath_number, parking_number)
                    VALUES ({}, {}, {}, {}, {}, \'{}\', \'{}\', {}, {}, {}, {}, {})""".format(partner_id, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number)                
        return DataBase.insert(query)
