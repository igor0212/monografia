from Repository.liquidity import Liquidity as RepositoryLiquidity
from Service.district import District
from Service.region import Region
from util import Log, Date, Cache, Util
from unidecode import unidecode
import operator
from Service.partner import Partner as ServicePartner
from Service.management import Management as ServiceManagement
from Service.property import Property as ServiceProperty


class Liquidity:
    def get_by_district(name, month):    
        try:
            liquidity = 0
            date = Date.get_mininum_date(month)
            total_properties = RepositoryLiquidity.get_properties_by_district(name)
            total_sold_properties = RepositoryLiquidity.get_sold_properties_by_district(name, date)            
            if(total_properties > 0):
                liquidity = total_sold_properties/total_properties            
            return liquidity                  
        except Exception as ex:            
            error = "Liquidity Service - get_by_district error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_by_street(name, month):    
        try:
            liquidity = 0
            date = Date.get_mininum_date(month)
            total_properties = RepositoryLiquidity.get_properties_by_street(name)
            total_sold_properties = RepositoryLiquidity.get_sold_properties_by_street(name, date)
            if(total_properties > 0):
                liquidity = total_sold_properties/total_properties            
            return liquidity
        except Exception as ex:            
            error = "Liquidity Service - get_by_street error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_by_region(name, month):
        try:             
            liquidity = 0
            date = Date.get_mininum_date(month)
            total_properties = RepositoryLiquidity.get_properties_by_region(name)
            total_sold_properties = RepositoryLiquidity.get_sold_properties_by_region(name, date)            
            if(total_properties > 0):
                liquidity = total_sold_properties/total_properties            
            return liquidity
        except Exception as ex:            
            error = "Liquidity Service - get_by_region error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_by_district_all(month):    
        try:
            district_cache = Cache.get_cache_district(month)
            if(district_cache):
                return sorted(district_cache.items(), key=operator.itemgetter(1), reverse=True)

            districts = District.get_all()
            cont = 0
            for district in districts:
                if(cont == 10):
                    break
                name = district['name']
                name_fmt = unidecode(name.replace(" ", "-"))                
                if name_fmt not in district_cache:
                    liq = Liquidity.get_by_district(name, month)                
                    if(liq != 1 and liq != 0):
                        district_cache[name] = liq
                        cont += 1
                        Cache.record_district(name, liq, month)
            return sorted(district_cache.items(), key=operator.itemgetter(1), reverse=True)
        except Exception as ex:            
            error = "Liquidity Service - get_by_district_all error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_by_region_all(month):    
        try:            
            region_cache = Cache.get_cache_region(month)
            if(region_cache):
                return sorted(region_cache.items(), key=operator.itemgetter(1), reverse=True)

            regions = Region.get_all()
            for region in regions:
                name = region['name']
                name_fmt = unidecode(name.replace(" ", "-"))                
                if name_fmt not in region_cache:
                    liq = Liquidity.get_by_region(name, month)
                    region_cache[name] = liq
                    Cache.record_region(name, liq, month)
            return sorted(region_cache.items(), key=operator.itemgetter(1), reverse=True)
        except Exception as ex:            
            error = "Liquidity Service - get_by_district_all error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_all_streets():
        try:
            data = RepositoryLiquidity.get_all_streets()    
            if(data):
                return data
        except Exception as ex:
            error = "Liquidity Service - get_all_streets error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_by_street_all(month):    
        try:
            street_cache = Cache.get_cache_street(month)
            #if(street_cache):
            #    return sorted(street_cache.items(), key=operator.itemgetter(1), reverse=True)

            streets = Liquidity.get_all_streets()
            cont = 0
            for street in streets:
                if(cont == 10):
                   break
                name = street['name'].title()                
                name_fmt = unidecode(name.replace(" ", "-"))                    
                #if name_fmt not in street_cache:
                liq = Liquidity.get_by_street(name, month)
                if(liq != 1 and liq != 0):
                    street_cache[name] = liq
                    cont += 1
                    #Cache.record_street(name, liq, month)
            return sorted(street_cache.items(), key=operator.itemgetter(1), reverse=True)
        except Exception as ex:            
            error = "Liquidity Service - get_by_district_all error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_duplicate():
        try:            
            properties = RepositoryLiquidity.get_duplicate()
            properties_to_add = ""
            for property in properties:
                partner_id = property.get('partner_id')
                list = RepositoryLiquidity.get_duplicate2(partner_id)
                partner_code = list[0]['partner_code']   

                partner_properties = ServicePartner.get_properties_by_code(partner_code)             

                #Then we need to validate the partner_id, as it is unique             
                partner_property = ServicePartner.check_valid_property(partner_properties, partner_id)  

                #Check if property has been sold
                if(not partner_property):                        
                    management = ServiceManagement.get_by_partner_id(partner_id)
                    if(management.get('is_available')):
                        Log.print("{} - {} propriedade vendida".format(partner_id, partner_code), show_screen=False)
                        properties_to_add += ServiceManagement.add(partner_id, management.get('price'), management.get('tax_rate', 0), management.get('property_tax', 0), False)                            
                    continue    

                #Check if property value has changed
                management = ServiceManagement.get_by_partner_id(partner_id)                
                if partner_property.get('preco') != management.get('price'):                
                    Log.print("{} - {} com preco de venda alterado. Preco antigo: {} Preco Novo: {}".format(partner_id, partner_code, management.get('price'), partner_property.get('preco')), show_screen=False)                    
                    price = Util.validate_number(partner_property.get('preco'))                    
                    tax_rate = Util.validate_number(partner_property.get('valor_iptu', 0))
                    property_tax = Util.validate_number(partner_property.get('valor_condominio', 0))                                        
                    properties_to_add += ServiceManagement.add(partner_id, price, tax_rate, property_tax, management.get('is_available'))       

            ServiceProperty.add_by_query(properties_to_add)
                
                
            
        except Exception as ex:            
            error = "Liquidity Service - get_duplicate error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)