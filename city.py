from repository import DataBase

class City:
    def get(id):        
        query = 'select * from "City" where Id = {} '.format(id)
        data = DataBase.select(query)    
        if(data):
            return data[0]
        return {}

    def add(name):        
        query = """INSERT INTO public."City"(name)
                VALUES (\'{}\')""".format(name)        
        return DataBase.insert(query)        

    def get_by_name(name):
        query = 'select * from "City" where Name = \'{}\' '.format(name)        
        data = DataBase.select(query)    
        if(data):
            return data[0]
        return {}

    def get_id(name):        
        data = City.get_by_name(name)        
        if(not data):
            return City.add(name)            
        return data['id']

    def get_all():        
        query = 'select * from "City"'
        data = DataBase.select(query)    
        if(data):
            return data
        return []