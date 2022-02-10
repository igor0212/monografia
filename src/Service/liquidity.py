from Repository.liquidity import Liquidity as RepositoryLiquidity
from Service.district import District
from Service.region import Region
from util import Log, Date, Cache
from unidecode import unidecode
import operator

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