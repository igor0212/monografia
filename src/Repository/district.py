from Repository.Database import DataBase

class District:    
    def get_all():        
        query = 'select * from "District"'
        return DataBase.select(query)    

    def get_by_id(id):                
        query = 'select * from "District" where Id = {} '.format(id)
        return DataBase.select(query)    