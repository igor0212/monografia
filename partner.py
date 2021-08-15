from district import District
from city import City
import requests
from util import Util
from property import Property
from management import Management

class Partner:   

    def get(goal, type, location, name, city, state='mg'):
        #url = 'https://api.casamineira.com.br/busca/imoveis?finalidade=venda&tipos[]=apartamento&logradouros[]=logradouro_avenida-dos-engenheiros_belo-horizonte_mg'
        #url = 'https://api.casamineira.com.br/busca/imoveis?finalidade=venda&tipos[]=apartamento&bairros[]=centro_belo-horizonte_mg'
        #url = 'https://api.casamineira.com.br/busca/imoveis?finalidade=venda&tipos[]=casa&bairros[]=santa-monica_belo-horizonte_mg'

        #https://api.casamineira.com.br/busca/imoveis?finalidade=venda&tipos[]=apartamento&logradouros[]=logradouro_avenida-dos-engenheiros_belo-horizonte_mg
        #https://api.casamineira.com.br/busca/imoveis?finalidade=venda&tipos[]=apartamento&logradouros[]=logradouros_avenida-dos-engenheiros_belo-horizonte_mg

        url = Util.get_url(goal, type, location, name, city, state)        

        response = requests.get(url = url)        
        return response.json()

    def add(goal, type, location, name, city, state='mg'):       
        
        url = Util.get_url(goal, type, location, name, city, state)
        response = requests.get(url = url)        

        response_json = response.json()

        properties = response_json['imoveis']

        if(len(properties) == 0):
            return('No properties added')
        
        for property in properties:
            try:
                property_id = Partner.add_property(property)
            except:
                return "Partner Error: Add property error"

            try:
                Partner.add_management(property_id, property)
            except:
                return "Partner Error: Add management error"

        return ('ok')
            
    
    def add_property(property):
        partner_id = property['id']            
        type_id =  Util.apartment if property['tipo']['nome'] == 'Apartamento' else Util.house
        district_id = District.get_id(property['bairro']['nome'])
        city_id = City.get_id(property['bairro']['cidade']['nome'])
        goal_id =  Util.sell if property['finalidade'] == 'venda' else Util.rent
        number = property['numero']
        street = property['logradouro']
        size = property['area']
        bedroom_number = property['quartos']
        room_number = property['salas']
        bath_number = property['banheiros']
        parking_number = property['vagas']
        
        Property.add(partner_id, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number)

    def add_management(management, property_id):        
        price = management['preco']
        tax_rate = management['valor_iptu']
        property_tax = management['valor_condominio']
        is_available = True
        
        Management.add(property_id, price, tax_rate, property_tax, is_available)

            



    


        


