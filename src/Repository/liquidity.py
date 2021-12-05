from Repository.database import DataBase
from util import Log

class Liquidity:

    def get_sold_properties_by_district(name, date):
        try:
            query = """
                    select count(distinct (p.partner_id)) 
                    from "Property" p
                    inner join "Management" m on m.partner_id = p.partner_id 
                    inner join "District" d ON d.id = p.district_id 
                    where m.is_available = false and d."name"  =  \'{}\'
                    and DATE(m.created_on) >= \'{}\'
            """.format(name, date)
            return DataBase.select(query)[0]['count']
        except Exception as ex:
            error = "Liquidity Repository - get_sold_properties_by_district error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)


    def get_properties_by_district(name, date):
        try:
            query = """
                    select count(distinct (p.partner_id)) 
                    from "Property" p
                    inner join "Management" m on m.partner_id = p.partner_id 
                    inner join "District" d ON d.id = p.district_id
                    where d."name"  =  \'{}\'
                    and DATE(m.created_on) >= \'{}\'
            """.format(name, date)
            return DataBase.select(query)[0]['count']
        except Exception as ex:
            error = "Liquidity Repository - get_properties_by_district error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)
    
    def get_sold_properties_by_street(name, date):
        try:
            query = """
                    select count(distinct (p.partner_id)) 
                    from "Property" p
                    inner join "Management" m on m.partner_id = p.partner_id 
                    where m.is_available = false and p."street"  =  \'{}\'
                    and DATE(m.created_on) >= \'{}\'
            """.format(name, date)
            return DataBase.select(query)[0]['count']
        except Exception as ex:
            error = "Liquidity Repository - get_sold_properties_by_street error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def get_properties_by_street(name, date):
        try:
            query = """
                    select count(distinct (p.partner_id)) 
                    from "Property" p
                    inner join "Management" m on m.partner_id = p.partner_id 
                    where p."street" =  \'{}\'
                    and DATE(m.created_on) >= \'{}\'
            """.format(name, date)
            return DataBase.select(query)[0]['count']
        except Exception as ex:
            error = "Liquidity Repository - get_properties_by_street error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)