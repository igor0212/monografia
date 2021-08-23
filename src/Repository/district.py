from Repository.Database import DataBase
from Util import Log

class District:    
    def get_all():
        try:
            query = 'select * from "District"'
            return DataBase.select(query)    
        except Exception as ex:
            Log.print("District Repository - get_all error: {}".format(ex), True)

    def get_by_id(id):
        try:
            query = 'select * from "District" where Id = {} '.format(id)
            return DataBase.select(query)    
        except Exception as ex:
            Log.print("District Repository - get_by_id error: {}".format(ex), True)