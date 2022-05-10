import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from Service.district import District
from Repository.district import District as RepositoryDistrict
from unittest.mock import MagicMock

class TestDistrict:
    def test_get_all(self):
        RepositoryDistrict.get_all = MagicMock(return_value = [{'id': 2, 'name': 'Buritis', 'region_id': 3}, {'id': 3, 'name': 'Padre Eustáquio', 'region_id': 4}, {'id': 4, 'name': 'Alto Vera Cruz', 'region_id': 2}, {'id': 5, 'name': 'Jardim dos Comerciários', 'region_id': 9}])
        users = District.get_all()       
        assert len(users) == 4
