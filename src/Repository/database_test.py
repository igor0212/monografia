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

        #ajuste no Banco para limpá-lo de testes anteriores
        DataBase.update('DELETE FROM "District" where name =' + "'BairroTeste'")
        query = 'select * from "District"'            
        districts = DataBase.select(query)        
        assert len(districts) == 488

    def test_select_all_when_it_finds_regions(self):
        
        #ajuste no Banco para limpá-lo de testes anteriores
        DataBase.update('DELETE FROM "Region" where id >= 10')
        query = 'select * from "Region"'            
        regions = DataBase.select(query)        
        assert len(regions) == 9

    def test_insertion_district(self):
        query = 'INSERT INTO "District" ("id", "name") VALUES' + "(1010, 'BairroTeste')"
        DataBase.insert(query)
        existing = DataBase.select('select name from "District" where id = 1010')
        assert [{'name': 'BairroTeste'}] == existing
    
    def test_insertion_region(self):
        query = 'INSERT INTO "Region" ("id", "name") VALUES' + "(1010, 'RegiaoTeste')"
        DataBase.insert(query)
        existing = DataBase.select('select name from "Region" where id = 1010')
        assert  [{'name': 'RegiaoTeste'}] == existing

