import pytest
from property import Property
from Repository.property import Property as RepositoryProperty
from unittest.mock import MagicMock

class TestProperty:
    def test_get_all_should_return_the_list_properties(self):
        RepositoryProperty.get_all = MagicMock(return_value=[{'id': 2},
                                                             {'id': 3},
                                                             {'id': 4}])
        properties = Property.get_all()
        assert len(properties) == 3

    def test_get_all_should_return_empty_list(self):
        RepositoryProperty.get_all = MagicMock(return_value=[])
        properties = Property.get_all()
        assert properties == []

    def test_get_all_should_raise_exception(self):
        RepositoryProperty.get_all = MagicMock(side_effect=Exception)
        with pytest.raises(Exception, match=r".*Partner Service - get_all error:*"): Property.get_all()

    def test_get_by_partner_id_should_return_property_when_it_is_found(self):
        id = 3
        RepositoryProperty.get_by_partner_id = MagicMock(id, return_value=[{'id': 1, 'city_id': 2, 'partner_id': 3}])
        property = Property.get_by_partner_id(id)
        assert id == property.get('partner_id')

    def test_get_by_partner_id_should_return_empty_object_when_it_is_not_found(self):
        id = 1
        RepositoryProperty.get_by_partner_id = MagicMock(id, return_value=[])
        property = Property.get_by_partner_id(id)
        assert property == {}

