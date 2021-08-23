from Repository.District import District as RepositoryDistrict
from Util import Log

class District:
    def get_all():
        try:
            data = RepositoryDistrict.get_all()    
            if(data):
                return data
        except Exception as ex:
            error = "District Service - get_all error: {}".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def get_by_id(id):    
        try:            
            data = RepositoryDistrict.get_by_id(id)    
            if(data):
                return data[0]
            return {}
        except Exception as ex:            
            error = "District Service - get_by_id error: {}".format(ex)
            Log.print(error, True)
            raise Exception(error)