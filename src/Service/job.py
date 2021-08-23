from Repository.Job import Job as RepositoryJob
from datetime import datetime
from Util import Log

class Job:
    def add(name, has_error=False, error_description=""):
        try:
            date_now = datetime.now()    
            return RepositoryJob.add(name, has_error, date_now, error_description)  
        except Exception as ex:            
            error = "Job Service - add error: {}".format(ex)
            Log.print(error, True)
            raise Exception(error)