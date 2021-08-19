import schedule
import time
from partner import Partner
from repository import DataBase
from datetime import datetime
from util import Util

def add(name, has_error=False):
    date_now = datetime.now()
    query = """INSERT INTO public."Job"(name, created_on, has_error) VALUES (\'{}\', \'{}\', {});""".format(name, date_now, has_error)
    path = "scripts/inserts_job.sql"
    Util.save_query_file(query, path)
    DataBase.insert(query)

def routine():
    print("Buscando novas casas/apartamentos e verificando se alguma propriedade foi vendida ou teve preco alterado")
    has_error = False
    try:
        Partner.routine()
    except:
        has_error = True
    finally:
        add('routine', has_error)

schedule.every().day.at("01:00").do(routine)

while True:
    schedule.run_pending()
    time.sleep(1)