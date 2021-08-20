import requests

class Partner:
    def get_properties_by_code(code):
        url = 'https://api.casamineira.com.br/busca-por-codigo?codigo={}'.format(code)        
        response = requests.get(url)        
        return response.json() 

    def get_properties(url):        
        print(url)
        response = requests.get(url)        
        return response.json()        