from Repository.City import City as RepositoryCity
from Util import Log

class City:
    def get_all():
        try:
            data = RepositoryCity.get_all()    
            if(data):
                return data
            return []
        except Exception as ex:            
            error = "City Service - get_all error: {}".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_by_id(id):
        try:
            data = RepositoryCity.get_by_id(id)    
            if(data):
                return data[0]
            return {}
        except Exception as ex:
            error = "City Service - get_by_id error: {}".format(ex)
            Log.print(error, True)
            raise Exception(error)            