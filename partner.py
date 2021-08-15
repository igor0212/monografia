from district import District
from city import City
import requests
from util import Util
from property import Property
from management import Management
from repository import DataBase

class Partner:   

    def get(goal, type, location, name, city, state='mg'):
        url = Util.get_url(goal, type, location, name, city, state)
        response = requests.get(url = url)        
        return response.json()

    def get_by_partner_id(id):
        query = 'select * from "Property" where partner_id = \'{}\' '.format(id)
        data = DataBase.select(query)           
        if(data):
            return data[0]
        return {}

    def add(goal, type, location, name, city, state='mg'):       
        
        url = Util.get_url(goal, type, location, name, city, state)
        response = requests.get(url = url)        

        response_json = response.json()

        properties = response_json['imoveis']        

        if(len(properties) == 0):
            return('No properties added')
        
        for property in properties:
            data = Partner.get_by_partner_id(property['codigo'])
            if(data):
                continue;

            try:
                property_id = Partner.add_property(property)
            except Exception as error:
                return "Partner Error: Add property error - {}".format(error)

            try:
                Partner.add_management(property, property_id)
            except Exception as error:
                return "Partner Error: Add management error - {}".format(error)

        return('ok')
            
    
    def add_property(property):                
        partner_id = property['codigo']
        type_id =  Util.apartment if property['tipo']['nome'] == 'Apartamento' else Util.house                
        district_id = District.get_id(property['bairro']['nome'])                
        city_id = City.get_id(property['bairro']['cidade']['nome'])        
        goal_id =  Util.sell if property['finalidade'] == 'venda' else Util.rent                
        number = property['numero'] if property['numero'] else " "
        street = property['logradouro'] if property['logradouro'] else " "        
        size = property['area']        
        bedroom_number = property['quartos']
        room_number = property['salas']
        bath_number = property['banheiros']        
        parking_number = property['vagas']                
        
        return Property.add(partner_id, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number)

    def add_management(management, property_id):
        price = management['preco']
        tax_rate = management['valor_iptu'] if management['valor_iptu'] else 0
        property_tax = management['valor_condominio'] if management['valor_condominio'] else 0        
        is_available = True
        
        return Management.add(property_id, price, tax_rate, property_tax, is_available)

            



    


        


