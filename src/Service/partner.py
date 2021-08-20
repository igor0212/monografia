from Service.district import District
from Service.property import Property
from Service.management import Management
from Repository.partner import Partner as RepositoryPartner
from util import Util, File, Enum

class Partner:
    def get_properties_by_code(code):        
        data = RepositoryPartner.get_properties_by_code(code)    
        if(data):
            return data['imoveis']
        return []

    def get_properties(goal, type, location, district, city, state, page):
        url = Util.get_url(goal, type, location, district, city, state, page)
        data = RepositoryPartner.get_properties(url)    
        if(data):
            return data['imoveis']
        return []

    def check_valid_property(properties, id):
        result = {}
        for property in properties:
            if(property['id'] == id):
                result = property
                break
        return result

    def check_property_sold():        
        properties_to_add = ""
        properties = Property.get_all_new_ad()        
        for property in properties:
            partner_id = property['partner_id']

            #This route can return more than one property by the given code 
            partner_properties = Partner.get_properties_by_code(property['partner_code'])

            #Then we need to validate the partner_id, as it is unique             
            partner_property = Partner.check_valid_property(partner_properties, partner_id)            

            #Check if property has been sold
            if(not partner_property):
                print("{} vendido".format(property['partner_code'])) #@TODO-
                management = Management.get_by_partner_id(partner_id)
                properties_to_add += Management.add(property['partner_id'], management['price'], management['tax_rate'], management['property_tax'], False)
                continue
            
            #Check if property value has changed
            management = Management.get_by_partner_id(partner_id)
            if partner_property['preco'] != management['price']:                
                print("{} com preco de venda alterado. Preco antigo: {} Preco Novo: {}".format(property['partner_code'], management['price'], partner_property['preco'])) #@TODO-                
                price = Util.validate_number(property.get('preco', 0))
                tax_rate = Util.validate_number(property.get('valor_iptu', 0))
                property_tax = Util.validate_number(property.get('valor_condominio', 0))
                properties_to_add += Management.add(partner_id, price, tax_rate, property_tax, management.get('is_available')) #@TODO-
            else:
                print("{} não foi vendido e nem teve o preco alterado".format(property['partner_code'])) #@TODO-
        
        text = properties_to_add if properties_to_add else "no property sold"
        File.record_insert(text, File.check_property_sold)
        Property.add_by_query(properties_to_add)

    def get_properties_by_district(goal, location, district, city, state='mg', pages_number=2):        
        list_properties = []
        for page in range(1, pages_number+1):                        
            apartments = Partner.get_properties(goal, "apartamento", location, district, city, state, page);
            if(apartments):
                list_properties.extend(apartments)

            houses = Partner.get_properties(goal, "casa", location, district, city, state, page);
            if(houses):
                list_properties.extend(apartments)

        return list_properties        

    def get_query_to_insert_property(properties, district_id):
        properties_to_add = ""
        list_id_query = []

        for property in properties:
            partner_id = property.get('id', 0)
            has_property = Property.get_by_partner_id(partner_id)
            has_property_in_query = partner_id in list_id_query

            #Check if property already exists in the database or in the list that will be inserted
            if(has_property or has_property_in_query):                
                print("ja existe esse id {} no bd ou na lista".format(partner_id)) #@TODO-
                continue;            
                
            properties_to_add += Partner.create_query_to_insert_property(property, district_id)            
            list_id_query.append(partner_id)
        
        return properties_to_add
    
    def create_query_to_insert_property(property, district_id):
        partner_id = property.get('id', 0)
        partner_code = property.get('codigo', '')
        type_id =  Enum.type.get(property.get('tipo').get('nome'), 0)
        district_id = district_id
        city_id = Enum.city.get(property.get('bairro').get('cidade').get('nome'), 0)        
        goal_id = Enum.goal.get(property.get('finalidade'), 0)
        number = Util.validate_string(property.get('numero'))
        street = Util.validate_string(property.get('logradouro'))
        size = property.get('area', 0)
        bedroom_number = property.get('quartos', 0) 
        room_number = property.get('salas', 0) 
        bath_number = property.get('banheiros', 0)
        parking_number = property.get('vagas', 0)
        price = Util.validate_number(property.get('preco', 0))
        tax_rate = Util.validate_number(property.get('valor_iptu', 0))
        property_tax = Util.validate_number(property.get('valor_condominio', 0))                
        is_available = True
        new_ad = True
        
        properties_to_add = Property.add(partner_id, partner_code, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number, new_ad)
        properties_to_add += Management.add(partner_id, price, tax_rate, property_tax, is_available)

        return properties_to_add    

    def search_properties_by_district():                
        properties_to_add = ""
        districts = District.get_all()

        for district in districts:
            properties = Partner.get_properties_by_district('venda', 'bairros', district.get('name', ''), 'belo horizonte');                        
            properties_to_add += Partner.get_query_to_insert_property(properties, district.get('id', 0))

        text = properties_to_add if properties_to_add else "no new properties found"
        File.record_insert(text, File.search_properties_by_district)
        Property.add_by_query(properties_to_add)

    def routine():
        Partner.search_properties_by_district()
        Partner.check_property_sold()