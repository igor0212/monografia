import schedule
import time
from partner import Partner
from repository import DataBase
from datetime import datetime

location = 'bairros'
goal = 'venda'
city = 'belo horizonte'  

def add(name, has_error=False):
    date_now = datetime.now()
    query = """INSERT INTO public."Job"(
                name, created_on, has_error)
                VALUES (\'{}\', \'{}\', {}); """.format(name, date_now, has_error)

    DataBase.insert(query)
    return query

def check_sold():
    has_error = False
    try:
        Partner.check_sold()
    except:
        has_error = True
    finally:
        add('check_sold', has_error)

def get_house():
    has_error = False
    try:
        Partner.add(goal, 'casa', location, city)
    except:
        has_error = True
    finally:
        add('get_house', has_error)

def get_apartment():
    has_error = False
    try:
        Partner.add(goal, 'apartamento', location, city)
    except:
        has_error = True
    finally:
        add('get_apartment', has_error)

def get_house():     
    Partner.add(goal, 'casa', location, city)

def get_apartment():    
    Partner.add(goal, 'apartamento', location, city)

schedule.every().day.at("08:00").do(get_house)
schedule.every().day.at("17:00").do(get_apartment)
schedule.every().day.at("23:00").do(check_sold)

while True:
    schedule.run_pending()
    time.sleep(1)