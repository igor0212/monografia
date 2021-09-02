import requests
from util import Log

class Partner:
    def get_properties_by_code(code):
        try:
            url = 'https://api.casamineira.com.br/busca-por-codigo?codigo={}'.format(code)        
            response = requests.get(url)        
            return response.json() 
        except Exception as ex:
            error = "Partner Repository - get_properties_by_code error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def get_properties(url):
        try:
            Log.print(url, show_screen=False)
            response = requests.get(url)        
            return response.json()        
        except Exception as ex:            
            error = "Partner Repository - get_properties error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)