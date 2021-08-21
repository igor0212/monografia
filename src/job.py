import schedule
import time
from Service.partner import Partner
from Service.job import Job
from util import File, Log

def routine():
    Log.print("Rotina comecou")
    has_error = False
    try:
        Partner.routine()
    except:
        has_error = True
    finally:
        text = Job.add('routine', has_error)        
        File.record_insert(text, File.routine)
        Log.print("Rotina terminou")

schedule.every().day.at("01:00").do(routine)

while True:
    schedule.run_pending()
    time.sleep(1)