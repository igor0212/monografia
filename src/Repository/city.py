from Repository.Database import DataBase
from Util import Log

class City:
    def get_all():
        try:
            query = 'select * from "City"'
            return DataBase.select(query)            
        except Exception as ex:
            error = "City Repository - get_all error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)
        

    def get_by_id(id):
        try:
            query = 'select * from "City" where Id = {}'.format(id)
            return DataBase.select(query)           
        except Exception as ex:
            error = "City Repository - get_by_id error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)