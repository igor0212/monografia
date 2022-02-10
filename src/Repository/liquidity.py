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

    def get_duplicate():
        try:
            query = """ SELECT
                            partner_id
                        FROM
                            "Management"
                        where is_available = false
                        GROUP BY
                            partner_id
                        HAVING
                            COUNT( partner_id ) > 1
                        ORDER BY
                            partner_id
                        """
            return DataBase.select(query)    
        except Exception as ex:            
            error = "Region Repository - get_duplicate error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)  

    def get_duplicate2(partner_id):
        try:
            query = """ select partner_code  
                        from "Property" p
                        where p.partner_id  =  {}
                        """.format(partner_id)
            return DataBase.select(query)    
        except Exception as ex:            
            error = "Region Repository - get_duplicate2 error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)           