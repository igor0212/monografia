import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from Repository.job import Job as RepositoryJob
from datetime import datetime
from util import Log

class Job:
    def add(name, has_error=False, error_description=""):
        try:
            date_now = datetime.now()    
            return RepositoryJob.add(name, has_error, date_now, error_description)  
        except Exception as ex:            
            error = "Job Service - add error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)