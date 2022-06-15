from database import DataBase

class TestDatabase:
    def test_select_city(self):
        query = 'select * from "City"'            
        cities = DataBase.select(query)        
        assert len(cities) == 1

    