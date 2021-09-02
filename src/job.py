import schedule
import time
from Service.partner import Partner
from util import Log
from datetime import datetime

def routine():
    Log.print("Rotina comecou: {}".format(datetime.now()))
    Partner.routine()
    Log.print("Rotina terminou: {}".format(datetime.now()))                

schedule.every().day.at("01:00").do(routine) 

while True:
    schedule.run_pending()
    time.sleep(1)