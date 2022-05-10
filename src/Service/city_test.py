from city import City
from Repository.city import City as RepositoryCity
from unittest.mock import MagicMock

class TestCity:
    def test_get_all(self):
        RepositoryCity.get_all = MagicMock(return_value = [{'id': 1, 'name': 'Belo Horizonte'}])        
        users = City.get_all()       
        assert len(users) == 1
