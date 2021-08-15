from util import Util
from repository import DataBase
from flask import jsonify

class City:
    def get():
        id = Util.get_field('id', 'int')
        query = 'select * from "City" where Id = {} '.format(id)
        data = DataBase.select(query)    
        if(data):
            return jsonify(data[0])
        return {}

    def add():
        name = Util.get_field('name', 'str')
        query = """INSERT INTO public."City"(name)
                VALUES (\'{}\')""".format(name)        
        return DataBase.insert(query)        

    def get_by_name(name):
        query = 'select * from "City" where Name = {} '.format(name)
        data = DataBase.select(query)    
        if(data):
            return jsonify(data[0])
        return {}

    def get_id(name):        
        data = City.get_by_name(name)
        if(len(data) == 0):
            data = City.get_by_name(name)
            if(len(data) == 0):
                return 'City Error: Get city id'

        return data['id']