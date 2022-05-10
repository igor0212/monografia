import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from Repository.district import District as RepositoryDistrict
from util import Log

class District:
    def get_all():
        try:
            data = RepositoryDistrict.get_all()    
            if(data):
                return data
        except Exception as ex:
            error = "District Service - get_all error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def get_by_id(id):    
        try:            
            data = RepositoryDistrict.get_by_id(id)    
            if(data):
                return data[0]
            return {}
        except Exception as ex:            
            error = "District Service - get_by_id error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_by_name(name):    
        try:            
            data = RepositoryDistrict.get_by_name(name)    
            if(data):
                return data[0]
            return {}
        except Exception as ex:            
            error = "District Service - get_by_name error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)