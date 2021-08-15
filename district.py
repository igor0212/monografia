from util import Util
from repository import DataBase
from flask import jsonify

class District:
    def get(id=0):        
        id = id if id else Util.get_field('id', 'int')
        query = 'select * from "District" where Id = {} '.format(id)
        data = DataBase.select(query)    
        if(data):
            return jsonify(data[0])
        return {}

    def add(name=''):        
        name = name if name else Util.get_field('name', 'str')
        query = """INSERT INTO public."District"(name)
                VALUES (\'{}\')""".format(name)    
        return DataBase.insert(query)        

    def get_by_name(name):
        query = 'select * from "District" where Name = \'{}\' '.format(name)
        data = DataBase.select(query)           
        if(data):
            return data[0]
        return {}

    def get_id(name):        
        data = District.get_by_name(name)                
        if(not data):
            return District.add(name)            
        return data['id']