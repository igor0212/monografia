from district import District
import requests
from util import Util
from property import Property
from management import Management
from repository import DataBase

class Partner:   

    def get(goal, type, location, name, city, state='mg', page=1):
        url = Util.get_url(goal, type, location, name, city, state, page)        
        response = requests.get(url = url)        
        return response.json()

    def get_by_code(code):
        url = 'https://api.casamineira.com.br/busca-por-codigo?codigo={}'.format(code)        
        response = requests.get(url = url)        
        return response.json()

    def check_sold():        
        properties = Property.get_all_new_ad()
        query = ""
        for property in properties:            
            response = Partner.get_by_code(property['partner_code'])             
            management = Management.get_by_partner_id(property['partner_id'])
            partner_property = Property.get_valid_property(response['imoveis'], property['partner_id'])            

            #Check if property has been sold
            if(not partner_property):
                print("{} vendido".format(property['partner_code']))
                query += Management.add(property['partner_id'], management['price'], management['tax_rate'], management['property_tax'], False)
            #Check if property value has changed            
            elif partner_property['preco'] != management['price']:                
                print("{} com preco de venda alterado. Preco antigo: {} Preco Novo: {}".format(property['partner_code'], management['price'], partner_property['preco']))
                price = partner_property['preco']
                tax_rate = partner_property['valor_iptu'] if partner_property['valor_iptu'] else 0
                property_tax = partner_property['valor_condominio'] if partner_property['valor_condominio'] else 0                  
                query += Management.add(property['partner_id'], price, tax_rate, property_tax, True)   
            else:
                print("{} não foi vendido e nem teve o preco alterado".format(property['partner_code']))

        path = "scripts/inserts_check_sold.sql"

        if(query):
            Util.save_query_file(query, path)
            DataBase.insert(query)
            return("ok")
        else:
            text = "no property sold"
            Util.save_query_file(text, path)
            return(text)               

    def add_property_by_district(goal, type, location, district, city, state, pages=20):
        query = ''
        for page in (number+1 for number in range(pages)):            
            url = Util.get_url(goal, type, location, district['name'], city, state, page)
            print(url)
            response = requests.get(url = url)        
            response_json = response.json()
            properties = response_json['imoveis']
            if(len(properties) == 0):
                continue

            query += Partner.add_properties(properties, district['id']) 

        return query    

    def add(goal, type, location, city, state='mg'):
        districts = District.get_all()        
        query = ''
        for district in districts:
            query += Partner.add_property_by_district(goal, type, location, district, city, state);                    

        path = 'scripts/inserts_properties.sql'

        if(query):
            Util.save_query_file(query, path)
            DataBase.insert(query)
            return("ok")
        else:
            text = "properties not found"
            Util.save_query_file(text, path)
            return(text)

    def add_properties(properties, district_id):
        query = ""
        for property in properties:            
            data = Property.get_by_partner_id(property['id'])
            if(data):
                continue;            
                
            query += Partner.add_property(property, district_id)
            query += Partner.add_management(property)            
        
        return query
    
    def add_property(property, district_id):                
        partner_id = property['id']
        partner_code = property['codigo']
        type_id =  Util.type.get(property['tipo']['nome'], 'Casa')
        district_id = district_id
        city_id = Util.city[property['bairro']['cidade']['nome']]        
        goal_id = Util.goal.get(property['finalidade'], 'aluguel')
        number = property['numero'] if property['numero'] else " "
        street = property['logradouro'] if property['logradouro'] else " "        
        size = property['area']        
        bedroom_number = property['quartos']
        room_number = property['salas']
        bath_number = property['banheiros']        
        parking_number = property['vagas']                
        
        return Property.add(partner_id, partner_code, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number, True)

    def add_management(management):
        partner_id = management['id']
        price = management['preco']
        tax_rate = management['valor_iptu'] if management['valor_iptu'] else 0
        property_tax = management['valor_condominio'] if management['valor_condominio'] else 0        
        is_available = True
        
        return Management.add(partner_id, price, tax_rate, property_tax, is_available)

    def routine(goal, location, city, state="mg"):
        districts = District.get_all()        
        query = ""
        for district in districts:
            query += Partner.add_property_by_district(goal, "apartamento", location, district, city, state);
            query += Partner.add_property_by_district(goal, "casa", location, district, city, state);

        path = "scripts/inserts_properties.sql"

        if(query):
            Util.save_query_file(query, path)
            DataBase.insert(query)            
        else:
            text = "no new properties found"
            Util.save_query_file(text, path)

        Partner.check_sold()

    

            



    


        


