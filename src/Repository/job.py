from Repository.database import DataBase

class Job:
    def add(name, has_error, date_now):            
        query = 'INSERT INTO public."Job"(name, created_on, has_error) VALUES (\'{}\', \'{}\', {});'.format(name, date_now, has_error)
        DataBase.insert(query)
        return query