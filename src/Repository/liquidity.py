from Repository.database import DataBase
from util import Util, Log

class Liquidity:

    def get_sold_properties_by_district(name, date):
        try:
            query = """
                    select count(distinct(p.partner_id)) 
                    from "Property" p                    
                    inner join "District" d ON d.id = p.district_id 
                    where lower(unaccent(d."name"))  =  \'{}\'
                    and false in 
                    (
                        select m.is_available 
                        from "Management" m 
                        where m.partner_id = p.partner_id 
                        and DATE(m.created_on) >= \'{}\'
                        order by created_on desc 
                        limit 1
                    )
            """.format(Util.format2(name), date)             
            return DataBase.select(query)[0]['count']
        except Exception as ex:
            error = "Liquidity Repository - get_sold_properties_by_district error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)


    def get_properties_by_district(name):        
        try:
            query = """
                    select count(distinct (p.partner_id)) 
                    from "Property" p
                    inner join "Management" m on m.partner_id = p.partner_id 
                    inner join "District" d ON d.id = p.district_id
                    where lower(unaccent(d."name"))  =  \'{}\'                    
            """.format(Util.format2(name))
            return DataBase.select(query)[0]['count']
        except Exception as ex:
            error = "Liquidity Repository - get_properties_by_district error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)
    
    def get_sold_properties_by_street(name, date):
        try:
            query = """
                    select count(distinct(p.partner_id)) 
                    from "Property" p                    
                    where lower(unaccent(p."street"))  =  \'{}\'
                    and false in 
                    (
                        select m.is_available
                        from "Management" m
                        where m.partner_id = p.partner_id
                        and DATE(m.created_on) >= \'{}\'
                        order by created_on desc 
                        limit 1
                    )
            """.format(Util.format2(name), date)                   
            return DataBase.select(query)[0]['count']
        except Exception as ex:
            error = "Liquidity Repository - get_sold_properties_by_street error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_properties_by_street(name):
        try:
            query = """
                    select count(distinct (p.partner_id)) 
                    from "Property" p
                    inner join "Management" m on m.partner_id = p.partner_id 
                    where lower(unaccent(p."street")) =  \'{}\'                    
            """.format(Util.format2(name))             
            return DataBase.select(query)[0]['count']
        except Exception as ex:
            error = "Liquidity Repository - get_properties_by_street error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)


    def get_sold_properties_by_region(name, date):
        try:
            query = """
                    select count(distinct(p.partner_id)) 
                    from "Property" p                    
                    inner join "District" d ON d.id = p.district_id
                    inner join "Region" r ON r.id = d.region_id
                    where lower(unaccent(r."name"))  =  \'{}\'
                    and false in 
                    (
                        select m.is_available
                        from "Management" m
                        where m.partner_id = p.partner_id
                        and DATE(m.created_on) >= \'{}\'
                        order by created_on desc 
                        limit 1
                    )
            """.format(Util.format2(name), date)
            return DataBase.select(query)[0]['count']
        except Exception as ex:
            error = "Liquidity Repository - get_sold_properties_by_region error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)


    def get_properties_by_region(name):
        try:
            query = """
                    select count(distinct (p.partner_id)) 
                    from "Property" p
                    inner join "Management" m on m.partner_id = p.partner_id 
                    inner join "District" d ON d.id = p.district_id
                    inner join "Region" r ON r.id = d.region_id
                    where lower(unaccent(r."name"))  =  \'{}\'
            """.format(Util.format2(name))
            return DataBase.select(query)[0]['count']
        except Exception as ex:
            error = "Liquidity Repository - get_properties_by_region error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_all_streets():
        try:
            query = """ select distinct (lower(p.street)) as name
                        from "Property" p                        
                        where length(street) > 3                        
                        order by name"""
            return DataBase.select(query)    
        except Exception as ex:            
            error = "Region Repository - get_all error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_announcement_dates_by_district(name):
        try:
            query = """
                    select distinct m.partner_id, min(DATE(m.created_on)) as announcement_date
                    from "Property" p
                    inner join "Management" m on p.partner_id = m.partner_id
                    inner join "District" d ON d.id = p.district_id
                    where lower(unaccent(d."name"))  =  \'{}\'
                    group by m.partner_id 
                    order by announcement_date
            """.format(Util.format2(name))
            return DataBase.select(query)
        except Exception as ex:
            error = "Liquidity Repository - get_announcement_dates_by_district error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)


    def get_announcement_dates_by_street(name):
        try:
            query = """
                    select distinct m.partner_id, min(DATE(m.created_on)) as announcement_date
                    from "Property" p
                    inner join "Management" m on p.partner_id = m.partner_id                    
                    where lower(unaccent(p."street")) = \'{}\'                    
                    group by m.partner_id 
                    order by announcement_date
            """.format(Util.format2(name))
            return DataBase.select(query)
        except Exception as ex:
            error = "Liquidity Repository - get_announcement_dates_by_street error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_announcement_dates_by_region(name):
        try:
            query = """
                    select distinct m.partner_id, min(DATE(m.created_on)) as announcement_date
                    from "Property" p
                    inner join "Management" m on p.partner_id = m.partner_id                    
                    inner join "District" d ON d.id = p.district_id
                    inner join "Region" r ON r.id = d.region_id
                    where lower(unaccent(r."name")) = \'{}\'                    
                    group by m.partner_id 
                    order by announcement_date
            """.format(Util.format2(name))
            return DataBase.select(query)
        except Exception as ex:
            error = "Liquidity Repository - get_announcement_dates_by_region error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def check_property_sold(partner_id, announcement_date, deadline):
        try:
            response = 0
            query = """
                    select count(*)
                    from "Management"
                    where partner_id = {}        
                    and DATE(created_on) > \'{}\'            
                    and DATE(created_on) <= \'{}\'
                    and is_available = false
                    group by partner_id
            """.format(partner_id, announcement_date, deadline)
            list = DataBase.select(query)
            if(list):
                response = list[0]['count']
            return response
        except Exception as ex:
            error = "Liquidity Repository - check_property_sold error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)