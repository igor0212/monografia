import pytest
from Service.city import City
from Repository.city import City as RepositoryCity
from unittest.mock import MagicMock


class TestCity:
    def test_get_all_when_it_finds_value(self):
        RepositoryCity.get_all = MagicMock(
            return_value=[{'id': 1, 'name': 'Belo Horizonte'}, {'id': 2, 'name': 'Contagem'}])
        cities = City.get_all()
        assert len(cities) == 2

    def test_get_all_when_it_does_not_find_any_value(self):
        RepositoryCity.get_all = MagicMock(return_value=[])
        cities = City.get_all()
        assert cities == []

    def test_get_all_when_exception_occurs(self):
        RepositoryCity.get_all = MagicMock(side_effect=Exception)
        with pytest.raises(Exception, match=r".*City Service - get_all error:*"):
            City.get_all()

    def test_get_by_id_when_it_finds_value(self):
        id = 1
        RepositoryCity.get_by_id = MagicMock(id, return_value=[{'id': 1, 'name': 'Belo Horizonte'}])
        city = City.get_by_id(id)
        assert id == city.get('id')

    def test_get_by_id_when_it_does_not_find_any_value(self):
        id = 1
        RepositoryCity.get_by_id = MagicMock(id, return_value=[])
        city = City.get_by_id(id)
        assert city == {}

    def test_get_by_id_when_return_is_invalid(self):
        id = 1
        RepositoryCity.get_by_id = MagicMock(id, return_value={'id': 1, 'name': 'Belo Horizonte'})
        with pytest.raises(Exception, match=r".*"):
            City.get_by_id(id)

    def test_get_by_id_when_exception_occurs(self):
        id = 1
        RepositoryCity.get_by_id = MagicMock(side_effect=Exception)
        with pytest.raises(Exception, match=r".*City Service - get_by_id error:*"):
            City.get_by_id(id)
