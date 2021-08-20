from Repository.database import DataBase

class City:
    def get_all():        
        query = 'select * from "City"'
        return DataBase.select(query)            

    def get_by_id(id):                
        query = 'select * from "City" where Id = {}'.format(id)
        return DataBase.select(query)           