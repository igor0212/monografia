import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

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
                    liq = Liquidity.get_district_liquidity(name, month)
                    if(liq > 0):
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
                    liq = Liquidity.get_region_liquidity(name, month)
                    if(liq > 0):
                        region_cache[name] = liq
                        Cache.record_region(name, liq, month)
            return sorted(region_cache.items(), key=operator.itemgetter(1), reverse=True)
        except Exception as ex:            
            error = "Liquidity Service - get_by_district_all error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_by_street_all(month):    
        try:
            street_cache = Cache.get_cache_street(month)
            if(street_cache):
                return sorted(street_cache.items(), key=operator.itemgetter(1), reverse=True)            

            streets = RepositoryLiquidity.get_all_streets()
            cont = 0
            for street in streets:
                if(cont == 10):
                   break
                name = street['name'].title()                
                name_fmt = unidecode(name.replace(" ", "-"))                    
                if name_fmt not in street_cache:
                    liq = Liquidity.get_street_liquidity(name, month)           
                    if(liq != 0 and liq != 1):
                        street_cache[name] = liq
                        cont += 1
                        Cache.record_street(name, liq, month)
            return sorted(street_cache.items(), key=operator.itemgetter(1), reverse=True)
        except Exception as ex:            
            error = "Liquidity Service - get_by_district_all error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_district_liquidity(name, month):
        try:
            liquidity_cache = Cache.get_cache_district_name(name, month)
            if(liquidity_cache):  
                return float(liquidity_cache)

            total_properties = 0
            total_sold_properties = 0
            liquidity = 0
            announcement_dates = RepositoryLiquidity.get_announcement_dates_by_district(name)
            for dic in announcement_dates:
                partner_id = dic.get('partner_id', 0)
                announcement_date = dic.get('announcement_date')
                deadline = Date.sum_date_by_month(announcement_date, month)
                sold = RepositoryLiquidity.check_property_sold(partner_id, announcement_date, deadline)
                total_properties += 1
                if(sold > 0):
                    total_sold_properties += 1
            if(total_properties > 0):
                liquidity = total_sold_properties/total_properties            
            Cache.set_cache_district_name(name, month, liquidity)
            return liquidity            
        except Exception as ex:            
            error = "Liquidity Service - get_district_liquidity error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_street_liquidity(name, month):
        try:
            liquidity_cache = Cache.get_cache_street_name(name, month)
            if(liquidity_cache):  
                return float(liquidity_cache)

            total_properties = 0
            total_sold_properties = 0
            liquidity = 0
            announcement_dates = RepositoryLiquidity.get_announcement_dates_by_street(name)
            for dic in announcement_dates:
                partner_id = dic.get('partner_id', 0)
                announcement_date = dic.get('announcement_date')
                deadline = Date.sum_date_by_month(announcement_date, month)
                sold = RepositoryLiquidity.check_property_sold(partner_id, announcement_date, deadline)
                total_properties += 1
                if(sold > 0):
                    total_sold_properties += 1
            if(total_properties > 0):
                liquidity = total_sold_properties/total_properties            
            Cache.set_cache_street_name(name, month, liquidity)
            return liquidity            
        except Exception as ex:            
            error = "Liquidity Service - get_street_liquidity error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_region_liquidity(name, month):
        try:        
            liquidity_cache = Cache.get_cache_region_name(name, month)
            if(liquidity_cache):  
                return float(liquidity_cache)

            total_properties = 0
            total_sold_properties = 0
            liquidity = 0
            announcement_dates = RepositoryLiquidity.get_announcement_dates_by_region(name)
            for dic in announcement_dates:
                partner_id = dic.get('partner_id', 0)
                announcement_date = dic.get('announcement_date')
                deadline = Date.sum_date_by_month(announcement_date, month)
                sold = RepositoryLiquidity.check_property_sold(partner_id, announcement_date, deadline)
                total_properties += 1
                if(sold > 0):
                    total_sold_properties += 1
            if(total_properties > 0):
                liquidity = total_sold_properties/total_properties            
            Cache.set_cache_region_name(name, month, liquidity)
            return liquidity            
        except Exception as ex:            
            error = "Liquidity Service - get_region_liquidity error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)