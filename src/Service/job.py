from Repository.Job import Job as RepositoryJob
from datetime import datetime

class Job:
    def add(name, has_error=False):
        date_now = datetime.now()    
        return RepositoryJob.add(name, has_error, date_now)  