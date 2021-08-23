import schedule
import time
from Service.Partner import Partner
from Service.Job import Job
from Util import File, Log

def routine():
    Log.print("Rotina comecou")
    has_error = False
    error_description = ""
    try:
        Partner.routine()
    except Exception as ex:
        Log.print("Job - routine error: {}".format(ex), True)
        has_error = True
        error_description = ex
    finally:
        text = Job.add('routine', has_error, error_description)        
        File.record_insert(text, File.routine)
        Log.print("Rotina terminou")

schedule.every().day.at("01:00").do(routine) 

while True:
    schedule.run_pending()
    time.sleep(1)