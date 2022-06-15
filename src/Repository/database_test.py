from database import DataBase

class TestDatabase:
    def teste_select(self):
        query = 'select * from "City"'            
        cities = DataBase.select(query)        
        assert len(cities) == 1

    