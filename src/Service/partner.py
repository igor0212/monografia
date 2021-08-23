from Service.District import District
from Service.Property import Property
from Service.Management import Management
from Repository.Partner import Partner as RepositoryPartner
from Util import Util, File, Enum, Log

class Partner:
    def get_properties_by_code(code):   
        try:     
            data = RepositoryPartner.get_properties_by_code(code)    
            if(data):
                return data.get('imoveis', [])
            return []
        except Exception as ex:
            Log.print("Partner Service - get_properties error: {}".format(ex), True)

    def get_properties(goal, type, location, district, city, state, page):
        try:
            url = Util.get_url(goal, type, location, district, city, state, page)
            data = RepositoryPartner.get_properties(url)    
            if(data):
                return data.get('imoveis', [])
            return []
        except Exception as ex:
            Log.print("Partner Service - get_properties error: {}".format(ex), True)

    def check_valid_property(properties, id):
        try:
            result = {}
            for property in properties:
                if(property.get('id', 0) == id):
                    result = property
                    break
            return result
        except Exception as ex:
            Log.print("Partner Service - check_valid_property error: {}".format(ex), True)

    def check_property_sold():
        try:
            properties_to_add = ""
            properties = Property.get_all_new_ad_and_not_sold()        
            for property in properties:
                partner_id = property.get('partner_id', 0)

                #This route can return more than one property by the given code 
                partner_properties = Partner.get_properties_by_code(property.get('partner_code', ''))

                #Then we need to validate the partner_id, as it is unique             
                partner_property = Partner.check_valid_property(partner_properties, partner_id)            

                #Check if property has been sold
                if(not partner_property):
                    Log.print("{} vendido".format(property.get('partner_code', '')), show_screen=False)
                    management = Management.get_by_partner_id(partner_id)
                    properties_to_add += Management.add(property.get('partner_id', 0), management.get('price', 0), management.get('tax_rate', 0), management.get('property_tax', 0), False)
                    continue
                
                #Check if property value has changed
                management = Management.get_by_partner_id(partner_id)
                if partner_property.get('preco', 0) != management.get('price', 0):                
                    Log.print("{} com preco de venda alterado. Preco antigo: {} Preco Novo: {}".format(property.get('partner_code', ''), management.get('price', 0), partner_property.get('preco', 0)), show_screen=False)
                    price = Util.validate_number(property.get('preco', 0))
                    tax_rate = Util.validate_number(property.get('valor_iptu', 0))
                    property_tax = Util.validate_number(property.get('valor_condominio', 0))
                    properties_to_add += Management.add(partner_id, price, tax_rate, property_tax, management.get('is_available')) 
                else:
                    Log.print("{} nao foi vendido e nem teve o preco alterado".format(property.get('partner_code', '')), show_screen=False)
            
            text = properties_to_add if properties_to_add else "no property sold"
            File.record_insert(text, File.check_property_sold)
            Property.add_by_query(properties_to_add)
        except Exception as ex:
            Log.print("Partner Service - check_property_sold error: {}".format(ex), True)

    def get_properties_by_district(goal, location, district, city, state='mg', pages_number=20): 
        try:       
            list_properties = []
            for page in range(1, pages_number+1):                        
                apartments = Partner.get_properties(goal, "apartamento", location, district, city, state, page);
                if(apartments):
                    list_properties.extend(apartments)

                houses = Partner.get_properties(goal, "casa", location, district, city, state, page);
                if(houses):
                    list_properties.extend(apartments)

            return list_properties        
        except Exception as ex:
            Log.print("Partner Service - get_properties_by_district error: {}".format(ex), True)

    def get_query_to_insert_property(properties, district_id):
        try:
            properties_to_add = ""
            list_id_query = []

            for property in properties:
                partner_id = property.get('id', 0)
                has_property = Property.get_by_partner_id(partner_id)
                has_property_in_query = partner_id in list_id_query

                #Check if property already exists in the database or in the list that will be inserted
                if(has_property or has_property_in_query):
                    text = "no bd" if has_property else "na lista"
                    Log.print("Ja existe o id {} {}".format(partner_id, text), show_screen=False)
                    continue;            
                    
                properties_to_add += Partner.create_query_to_insert_property(property, district_id)            
                list_id_query.append(partner_id)
            
            return properties_to_add
        except Exception as ex:
            Log.print("Partner Service - get_query_to_insert_property error: {}".format(ex), True)
    
    def create_query_to_insert_property(property, district_id):
        try:
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
        except Exception as ex:
            Log.print("Partner Service - create_query_to_insert_property error: {}".format(ex), True)

    def search_properties_by_district():
        try:
            properties_to_add = ""
            districts = District.get_all()

            for district in districts:
                properties = Partner.get_properties_by_district('venda', 'bairros', district.get('name', ''), 'belo horizonte');                        
                properties_to_add += Partner.get_query_to_insert_property(properties, district.get('id', 0))

            text = properties_to_add if properties_to_add else "no new properties found"
            File.record_insert(text, File.search_properties_by_district)
            Property.add_by_query(properties_to_add)
        except Exception as ex:
            Log.print("Partner Service - search_properties_by_district error: {}".format(ex), True)

    def routine():
        try:
            Partner.search_properties_by_district()
            Partner.check_property_sold()
        except Exception as ex:
            Log.print("Partner Service - routine error: {}".format(ex), True)
