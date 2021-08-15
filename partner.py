import requests
from util import Util

class Partner:
    def get(goal, type, location, name, city, state='mg'):
        #url = 'https://api.casamineira.com.br/busca/imoveis?finalidade=venda&tipos[]=apartamento&logradouros[]=logradouro_avenida-dos-engenheiros_belo-horizonte_mg'
        #url = 'https://api.casamineira.com.br/busca/imoveis?finalidade=venda&tipos[]=apartamento&bairros[]=centro_belo-horizonte_mg'
        #url = 'https://api.casamineira.com.br/busca/imoveis?finalidade=venda&tipos[]=casa&bairros[]=santa-monica_belo-horizonte_mg'

        #https://api.casamineira.com.br/busca/imoveis?finalidade=venda&tipos[]=apartamento&logradouros[]=logradouro_avenida-dos-engenheiros_belo-horizonte_mg
        #https://api.casamineira.com.br/busca/imoveis?finalidade=venda&tipos[]=apartamento&logradouros[]=logradouros_avenida-dos-engenheiros_belo-horizonte_mg
        
        if(location == 'logradouros'):
            search = 'logradouro_{}_{}_{}'.format(name, city, state)
        elif(location == 'bairros'):
            search = '{}_{}_{}'.format(name, city, state)
        else:
            return 'Error: Location not implemented'

        url = 'https://api.casamineira.com.br/busca/imoveis?finalidade={}&tipos[]={}&{}[]={}'.format(Util.format_search(goal), Util.format_search(type), Util.format_search(location), Util.format_search(search))        

        response = requests.get(url = url)        
        return response.json()


