from Repository.Database import DataBase
from Util import Log

class City:
    def get_all():
        try:
            query = 'select * from "City"'
            return DataBase.select(query)            
        except Exception as ex:
            Log.print("City Repository - get_all error: {}".format(ex), True)
        

    def get_by_id(id):
        try:
            query = 'select * from "City" where Id = {}'.format(id)
            return DataBase.select(query)           
        except Exception as ex:
            Log.print("City Repository - get_by_id error: {}".format(ex), True)