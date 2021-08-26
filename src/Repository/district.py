from Repository.Database import DataBase
from Util import Log

class District:    
    def get_all():
        try:
            query = 'select * from "District"'
            return DataBase.select(query)    
        except Exception as ex:            
            error = "District Repository - get_all error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def get_by_id(id):
        try:
            query = 'select * from "District" where Id = {} '.format(id)
            return DataBase.select(query)    
        except Exception as ex:
            error = "District Repository - get_by_id error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_by_name(name):
        try:
            query = 'select * from "District" where name =  \'{}\' '.format(name)
            return DataBase.select(query)    
        except Exception as ex:
            error = "District Repository - get_by_name error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)