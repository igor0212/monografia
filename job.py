import schedule
import time
from partner import Partner
from repository import DataBase
from datetime import datetime
from util import Util

location = 'bairros'
goal = 'venda'
city = 'belo horizonte'  

def add(name, has_error=False):
    date_now = datetime.now()
    query = """INSERT INTO public."Job"(
                name, created_on, has_error)
                VALUES (\'{}\', \'{}\', {}); """.format(name, date_now, has_error)

    path = "scripts/inserts_job.sql"
    Util.save_query_file(query, path)
    DataBase.insert(query)

def routine():
    print("Buscando novas casas/apartamento e verificando se alguma foi vendidada ou teve preco alterado")
    has_error = False
    try:
        Partner.routine(goal, location, city)
    except:
        has_error = True
    finally:
        add('routine', has_error)

schedule.every().day.at("01:00").do(routine)

while True:
    schedule.run_pending()
    time.sleep(1)