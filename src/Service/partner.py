from Service.district import District
from Service.property import Property
from Service.management import Management
from Service.job import Job
from Repository.partner import Partner as RepositoryPartner
from util import Util, File, Enum, Log
from tqdm import tqdm

class Partner:
    def get_properties_by_code(code):   
        try:     
            data = RepositoryPartner.get_properties_by_code(code)    
            if(data):
                return data.get('imoveis', [])
            return []
        except Exception as ex:
            error = "Partner Service - get_properties_by_code error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def get_properties(goal, type, location, district, city, state, page):
        try:
            url = Util.get_url(goal, type, location, district, city, state, page)
            data = RepositoryPartner.get_properties(url)    
            if(data):
                return data.get('imoveis', [])
            return []
        except Exception as ex:
            error = "Partner Service - get_properties error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def check_valid_property(properties, id):
        try:            
            result = {}
            for property in properties:
                if(property.get('id', 0) == id):
                    result = property
                    break
            return result
        except Exception as ex:
            error = "Partner Service - check_valid_property error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def check_property_sold():
        properties_to_add = ""
        try:            
            properties = Property.get_all_new_ad()        
            for property in tqdm(properties):
                try:
                    partner_id = property.get('partner_id')
                    partner_code = property.get('partner_code', '')

                    #This route can return more than one property by the given code 
                    partner_properties = Partner.get_properties_by_code(partner_code)

                    #Then we need to validate the partner_id, as it is unique             
                    partner_property = Partner.check_valid_property(partner_properties, partner_id)            

                    #Check if property has been sold
                    if(not partner_property):                        
                        management = Management.get_by_partner_id(partner_id)
                        if(management.get('is_available')):
                            Log.print("{} - {} propriedade vendida".format(partner_id, partner_code), show_screen=False)
                            properties_to_add += Management.add(partner_id, management.get('price'), management.get('tax_rate', 0), management.get('property_tax', 0), False)                            
                        continue
                    
                    #Check if property value has changed
                    management = Management.get_by_partner_id(partner_id)                
                    if partner_property.get('preco') != management.get('price'):                
                        Log.print("{} - {} com preco de venda alterado. Preco antigo: {} Preco Novo: {}".format(partner_id, partner_code, management.get('price'), partner_property.get('preco')), show_screen=False)                    
                        price = Util.validate_number(partner_property.get('preco'))                    
                        tax_rate = Util.validate_number(partner_property.get('valor_iptu', 0))
                        property_tax = Util.validate_number(partner_property.get('valor_condominio', 0))                                        
                        properties_to_add += Management.add(partner_id, price, tax_rate, property_tax, True) 
                    
                except Exception as ex:
                    error = "Partner Service - check_property_sold - property {} with error: {} \n".format(partner_code, ex)
                    Log.print(error, True)

            Property.add_by_query(properties_to_add)
        except Exception as ex:
            error = "Partner Service - check_property_sold error: {} \n".format(ex)
            Log.print(error, True)            
        finally:
            text = properties_to_add if properties_to_add else "no property sold"
            File.record_insert(text)

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
            error = "Partner Service - get_properties_by_district error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

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
            error = "Partner Service - get_query_to_insert_property error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)            
    
    def create_query_to_insert_property(property, district_id):
        try:
            partner_id = property.get('id')
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
            price = Util.validate_number(property.get('preco'))
            tax_rate = Util.validate_number(property.get('valor_iptu', 0))
            property_tax = Util.validate_number(property.get('valor_condominio', 0))                
            is_available = True
            new_ad = True
            
            properties_to_add = Property.add(partner_id, partner_code, type_id, district_id, city_id, goal_id, number, street, size, bedroom_number, room_number, bath_number, parking_number, new_ad)
            properties_to_add += Management.add(partner_id, price, tax_rate, property_tax, is_available)

            return properties_to_add    
        except Exception as ex:
            error = "Partner Service - create_query_to_insert_property error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)            

    def search_properties_by_district():
        properties_to_add = ""        
        try:            
            districts = District.get_all()
            for district in tqdm(districts):

                try:
                    properties = Partner.get_properties_by_district('venda', 'bairros', district.get('name', ''), 'belo horizonte');                        
                    properties_to_add += Partner.get_query_to_insert_property(properties, district.get('id', 0))
                except Exception as ex:
                    error = "Partner Service - district {} with error: {} \n".format(district.get('name', ''), ex)
                    Log.print(error, True)
            
            Property.add_by_query(properties_to_add)
        except Exception as ex:
            error = "Partner Service - search_properties_by_district error: {} \n".format(ex)
            Log.print(error, True)            
        finally:
            text = properties_to_add if properties_to_add else "no new properties found"
            File.record_insert(text)

    def search_properties_by_district_name(name):
        properties_to_add = ""        
        try:            
            district = District.get_by_name(name)            
            properties = Partner.get_properties_by_district('venda', 'bairros', district.get('name', ''), 'belo horizonte');                        
            properties_to_add += Partner.get_query_to_insert_property(properties, district.get('id', 0))            
            Property.add_by_query(properties_to_add)
        except Exception as ex:
            error = "Partner Service - search_properties_by_district_name error: {} \n".format(ex)
            Log.print(error, True)            
        finally:
            text = properties_to_add if properties_to_add else "no new properties found"
            File.record_insert(text)

    def check_property_sold_by_code(code):
        properties_to_add = ""
        try:            
            property = Property.get_by_partner_code(code)                
            partner_id = property.get('partner_id')

            #This route can return more than one property by the given code 
            partner_properties = Partner.get_properties_by_code(property.get('partner_code', ''))

            #Then we need to validate the partner_id, as it is unique             
            partner_property = Partner.check_valid_property(partner_properties, partner_id)            

            #Check if property has been sold
            if(not partner_property):
                Log.print("{} vendido".format(property.get('partner_code', '')), show_screen=False)
                management = Management.get_by_partner_id(partner_id)
                properties_to_add += Management.add(partner_id, management.get('price'), management.get('tax_rate', 0), management.get('property_tax', 0), False)                
            
            #Check if property value has changed
            management = Management.get_by_partner_id(partner_id)                
            if partner_property.get('preco') != management.get('price'):                
                Log.print("{} com preco de venda alterado. Preco antigo: {} Preco Novo: {}".format(property.get('partner_code', ''), management.get('price'), partner_property.get('preco')), show_screen=False)                    
                price = Util.validate_number(partner_property.get('preco'))                    
                tax_rate = Util.validate_number(partner_property.get('valor_iptu', 0))
                property_tax = Util.validate_number(partner_property.get('valor_condominio', 0))                                        
                properties_to_add += Management.add(partner_id, price, tax_rate, property_tax, management.get('is_available')) 
            else:
                Log.print("{} nao foi vendido e nem teve o preco alterado".format(property.get('partner_code', '')), show_screen=False)                     

            Property.add_by_query(properties_to_add)
        except Exception as ex:
            error = "Partner Service - check_property_sold_by_code error: {} \n".format(ex)
            Log.print(error, True)            
        finally:
            text = properties_to_add if properties_to_add else "no property sold"
            File.record_insert(text)

    def routine():
        has_error = False
        error = ''
        try:
            Partner.search_properties_by_district()
            Partner.check_property_sold()
        except Exception as ex:
            error = "Partner Service - routine error: {} \n".format(ex)
            has_error = True            
            Log.print(error, True)  
        finally:
            text = Job.add('routine', has_error, error)        
            File.record_insert(text)                  
