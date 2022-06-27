from ast import Eq
from database import DataBase

class TestDatabase:
    def test_select_all_when_it_finds_cities(self):
        query = 'select * from "City"'            
        cities = DataBase.select(query)        
        assert len(cities) == 1
    
    def test_select_all_when_it_finds_goals(self):
        query = 'select * from "Goal"'            
        goals = DataBase.select(query)        
        assert len(goals) == 2

    def test_select_all_when_it_finds_types(self):
        query = 'select * from "Type"'            
        types = DataBase.select(query)        
        assert len(types) == 3

    def test_select_all_when_it_finds_districts(self):
        query = 'select * from "District"'            
        districts = DataBase.select(query)        
        assert len(districts) == 488

    def test_select_all_when_it_finds_regions(self):
        query = 'select * from "Region"'            
        regions = DataBase.select(query)        
        assert len(regions) == 9

    def test_insertion_district(self):
        query = 'INSERT INTO "District" ("id", "name") VALUES' + "(1000, 'BairroTeste')"
        district = DataBase.insert(query)
        existing = DataBase.select('select name from "District" where id = 1000')
        assert [{'name': 'BairroTeste'}] == existing
    
    def test_insertion_region(self):
        query = 'INSERT INTO "Region" ("id", "name") VALUES' + "(1000, 'RegiaoTeste')"
        regions = DataBase.insert(query)
        existing = DataBase.select('select name from "Region" where id = 1000')
        assert  [{'name': 'RegiaoTeste'}] == existing

