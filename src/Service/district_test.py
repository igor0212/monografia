from district import District
from Repository.district import District as RepositoryDistrict
from unittest.mock import MagicMock
import pytest

class TestDistrict:
    def test_get_all_when_it_finds_value(self):
        RepositoryDistrict.get_all = MagicMock(return_value = [{'id': 2, 'name': 'Buritis', 'region_id': 3}, {'id': 3, 'name': 'Padre Eustáquio', 'region_id': 4}, {'id': 4, 'name': 'Alto Vera Cruz', 'region_id': 2}, {'id': 5, 'name': 'Jardim dos Comerciários', 'region_id': 9}])
        districts = District.get_all()       
        assert len(districts) == 4

    def test_get_all_when_it_does_not_find_any_value(self):
        RepositoryDistrict.get_all = MagicMock(return_value = [])
        districts = District.get_all()  
        assert districts == []

    def test_get_all_when_exception_occurs(self):
        RepositoryDistrict.get_all = MagicMock(side_effect=Exception)
        with pytest.raises(Exception, match=r".*District Service - get_all error:*") : District.get_all()

    def test_get_by_id_when_it_finds_value(self):
        id = 1
        RepositoryDistrict.get_by_id = MagicMock(id, return_value = [{'id': 1, 'name': 'Buritis'}])        
        district = District.get_by_id(id)        
        assert id == district.get('id')

    def test_get_by_id_when_it_does_not_find_any_value(self):
        id = 1
        RepositoryDistrict.get_by_id = MagicMock(id, return_value = [])        
        district = District.get_by_id(id)        
        assert district == {}
    
    def test_get_by_id_when_retunr_is_invalid(self):
        id = 3
        RepositoryDistrict.get_by_id = MagicMock(id, return_value = {'id': 3, 'name': 'Camargos'})
        with pytest.raises(Exception, match=r".*District Service - get_by_id error:*") : District.get_by_id(id)

    def test_get_by_id_when_exception_occurs(self):
        id = 1
        RepositoryDistrict.get_by_id = MagicMock(side_effect=Exception)
        with pytest.raises(Exception, match=r".*District Service - get_by_id error:*") : District.get_by_id(id)

    def test_get_by_name_when_it_finds_value(self):
        name = 'Buritis'
        RepositoryDistrict.get_by_name = MagicMock(name, return_value = [{'id': 1, 'name': 'Buritis'}])        
        district = District.get_by_name(name)        
        assert name == district.get('name')

    def test_get_by_name_when_it_does_not_find_any_value(self):
        name = 'Buritis'
        RepositoryDistrict.get_by_name = MagicMock(name, return_value = [])        
        district = District.get_by_name(name)        
        assert district == {}
    
    def test_get_by_name_when_retunr_is_invalid(self):
        name = 'Buritis'
        RepositoryDistrict.get_by_name = MagicMock(id, return_value = {'id': 3, 'name': 'Camargos'})
        with pytest.raises(Exception, match=r".*District Service - get_by_name error:*") : District.get_by_name(name)

    def test_get_by_name_when_exception_occurs(self):
        name = 'Buritis'
        RepositoryDistrict.get_by_name = MagicMock(side_effect=Exception)
        with pytest.raises(Exception, match=r".*District Service - get_by_name error:*") : District.get_by_name(name)

