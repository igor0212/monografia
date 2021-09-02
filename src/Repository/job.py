from Repository.database import DataBase
from util import Log

class Job:
    def add(name, has_error, date_now, error_description):            
        try:
            query = 'INSERT INTO public."Job"(name, created_on, has_error, error_description) VALUES (\'{}\', \'{}\', {}, \'{}\');'.format(name, date_now, has_error, error_description)
            DataBase.insert(query)
            return query
        except Exception as ex:            
            error = "Job Repository - add error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)