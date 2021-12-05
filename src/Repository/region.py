from Repository.database import DataBase
from util import Util, Log

class Region:
    def get_by_name(name):
        try:
            query = 'select id from "Region" where name = \'{}\' '.format(name)
            response = DataBase.select(query)
            if(response):
                return response[0]['id']
            return 0
        except Exception as ex:
            error = "Region Repository - get_by_name error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_district_by_name(name):
        try:
            name_fmt = name.replace("'", "''")            
            query = 'select id from "District" where name = \'{}\' and region_id is null'.format(name_fmt)
            print(query)
            response = DataBase.select(query)
            if(response):
                return response[0]['id']
            return 0
        except Exception as ex:
            error = "Region Repository - get_district_by_name error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)
  
    def link(region_id, district_id):
        try:
            query = 'update "District" set region_id = {} where id = {}'.format(region_id, district_id)
            DataBase.update(query)
        except Exception as ex:
            error = "Region Repository - link error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)