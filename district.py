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
                VALUES (\'{}\'); """.format(name)    
        DataBase.insert(query)
        return('ok')