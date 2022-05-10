import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
import Repository.city as RepositoryCity
class City:
    def get_all():
        try:
            data = RepositoryCity.get_all()    
            if(data):
                return data
            return []
        except Exception as ex:            
            error = "City Service - get_all error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_by_id(id):
        try:
            data = RepositoryCity.get_by_id(id)    
            if(data):
                return data[0]
            return {}
        except Exception as ex:
            error = "City Service - get_by_id error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)            