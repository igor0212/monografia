from util import Util
from repository import DataBase
from flask import jsonify

class District:
    def get():
        id = Util.get_field('id', 'int')
        query = 'select * from "District" where Id = {} '.format(id)
        data = DataBase.select(query)    
        if(data):
            return jsonify(data[0])
        return {}

    def add():
        name = Util.get_field('name', 'str')
        query = """INSERT INTO public."District"(name)
                VALUES (\'{}\')""".format(name)    
        return DataBase.insert(query)        

    def get_by_name(name):
        query = 'select * from "District" where Name = {} '.format(name)
        data = DataBase.select(query)    
        if(data):
            return jsonify(data[0])
        return {}

    def get_id(name):        
        data = District.get_by_name(name)
        if(len(data) == 0):
            data = District.get_by_name(name)
            if(len(data) == 0):
                return 'District Error: Get district id'

        return data['id']