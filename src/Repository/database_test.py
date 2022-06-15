from database import DataBase

class TestDatabase:
    def test_select_city(self):
        query = 'select * from "City"'            
        cities = DataBase.select(query)        
        assert len(cities) == 1
    
    def test_select_goal(self):
        query = 'select * from "Goal"'            
        goals = DataBase.select(query)        
        assert len(goals) == 2

    def test_select_type(self):
        query = 'select * from "Type"'            
        types = DataBase.select(query)        
        assert len(types) == 3

    def test_select_district(self):
        query = 'select * from "District"'            
        districts = DataBase.select(query)        
        assert len(districts) == 488

    def test_select_region(self):
        query = 'select * from "Region"'            
        regions = DataBase.select(query)        
        assert len(regions) == 9

    