import pytest
from Service.property import Property
from Repository.property import Property as RepositoryProperty
from unittest.mock import MagicMock


class TestProperty:
    def test_get_all_should_return_the_list_of_all_properties(self):
        RepositoryProperty.get_all = MagicMock(return_value=[{'id': 1},
                                                             {'id': 2},
                                                             {'id': 3}])
        properties = Property.get_all()
        assert len(properties) == 3

    def test_get_all_should_return_empty_list_when_not_found(self):
        RepositoryProperty.get_all = MagicMock(return_value=[])
        properties = Property.get_all()
        assert properties == []

    def test_get_all_should_raise_exception(self):
        RepositoryProperty.get_all = MagicMock(side_effect=Exception)
        with pytest.raises(Exception, match=r".*Partner Service - get_all error:*"):
            Property.get_all()

    def test_get_all_new_ad_should_return_the_list_of_new_properties(self):
        RepositoryProperty.get_all_new_ad = MagicMock(return_value=[{'id': 2},
                                                                     {'id': 3}])
        properties = Property.get_all_new_ad()
        assert len(properties) == 2

    def test_get_all_new_ad_should_return_empty_list_when_not_found(self):
        RepositoryProperty.get_all_new_ad = MagicMock(return_value=[])
        properties = Property.get_all_new_ad()
        assert properties == []

    def test_get_all_new_ad_should_raise_exception(self):
        RepositoryProperty.get_all_new_ad = MagicMock(side_effect=Exception)
        with pytest.raises(Exception, match=r".*Partner Service - get_all_new_ad error:*"):
            Property.get_all_new_ad()

    def test_get_by_partner_id_should_return_property_when_found(self):
        id = 3
        RepositoryProperty.get_by_partner_id = MagicMock(id, return_value=[{'id': 1, 'city_id': 2, 'partner_id': 3}])
        property = Property.get_by_partner_id(id)
        assert id == property.get('partner_id')

    def test_get_by_partner_id_should_return_empty_object_when_not_found(self):
        id = 1
        RepositoryProperty.get_by_partner_id = MagicMock(id, return_value=[])
        property = Property.get_by_partner_id(id)
        assert property == {}

    def test_get_by_partner_id_should_raise_exception_when_invalid_result(self):
        id = 3
        RepositoryProperty.get_by_partner_id = MagicMock(id, return_value={'any': 'invalid value'})
        with pytest.raises(Exception, match=r".*"):
            Property.get_by_partner_id(id)

    def test_get_by_partner_id_should_raise_exception(self):
        id = 1
        RepositoryProperty.get_by_partner_id = MagicMock(side_effect=Exception)
        with pytest.raises(Exception, match=r".*Partner Service - get_by_partner_id error:*"):
            Property.get_by_partner_id(id)

    def test_get_by_partner_code_should_return_property_when_found(self):
        code = 'xyz'
        RepositoryProperty.get_by_partner_code = MagicMock(code, return_value=[{'id': 1, 'partner_code': 'xyz'}])
        property = Property.get_by_partner_code(code)
        assert code == property.get('partner_code')

    def test_get_by_partner_code_should_return_empty_object_when_not_found(self):
        code = 'xyz'
        RepositoryProperty.get_by_partner_code = MagicMock(code, return_value=[])
        property = Property.get_by_partner_code(code)
        assert property == {}

    def test_get_by_partner_code_should_when_invalid_result(self):
        code = 'xyz'
        RepositoryProperty.get_by_partner_code = MagicMock(code, return_value={'result': 'invalid'})
        with pytest.raises(Exception, match=r".*"):
            Property.get_by_partner_code(code)

    def test_get_by_partner_code_should_raise_exception(self):
        code = 'xyz'
        RepositoryProperty.get_by_partner_code = MagicMock(side_effect=Exception)
        with pytest.raises(Exception, match=r".*Partner Service - get_by_partner_code error:*"):
            Property.get_by_partner_code(code)
