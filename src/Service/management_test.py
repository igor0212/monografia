from datetime import date, datetime
import os
import sys
from multiprocessing import managers
import pytest
from management import Management
from Repository.management import Management as RepositoryManagement
from unittest.mock import MagicMock
from unittest import mock 

class TestManagement:

#TENTAIVA DE MOCK DE BANCO DE DADOS NAS FIXTURES
    def fixture_db_conecction(self):
        dbc = mock.MagicMock(spec = ['Repository.add'])
        return dbc
    
    def fixed_rows(self):
        rows = [{'id': 2, 
                                                                'partner_id': 3,
                                                                 'price': 100,
                                                                 'tax_rate': 1,
                                                                 'property_tax': 1,
                                                                 'created_on': '2022-01-01 00:00:00',
                                                                 'is_available': True},
                                                                 {'id': 3, 
                                                                 'partner_id': 4,
                                                                 'price': 1000,
                                                                 'tax_rate': 2,
                                                                 'property_tax': 2,
                                                                 'created_on': '2022-01-02 00:00:00',
                                                                 'is_available': True},
                                                                 {'id': 3, 
                                                                 'partner_id': 4,
                                                                 'price': 1000,
                                                                 'tax_rate': 2,
                                                                 'property_tax': 2,
                                                                 'created_on': '2022-01-02 00:00:00',
                                                                 'is_available': True,                                                                     
                                                                 }]
        return rows

    def test_get_all_when_it_finds_value(self):
        RepositoryManagement.get_all = MagicMock(return_value = [{'id': 2, 
                                                                'partner_id': 3,
                                                                 'price': 100,
                                                                 'tax_rate': 1,
                                                                 'property_tax': 1,
                                                                 'created_on': '2022-01-01 00:00:00',
                                                                 'is_available': True},
                                                                 {'id': 3, 
                                                                 'partner_id': 4,
                                                                 'price': 1000,
                                                                 'tax_rate': 2,
                                                                 'property_tax': 2,
                                                                 'created_on': '2022-01-02 00:00:00',
                                                                 'is_available': True},
                                                                 {'id': 3, 
                                                                 'partner_id': 4,
                                                                 'price': 1000,
                                                                 'tax_rate': 2,
                                                                 'property_tax': 2,
                                                                 'created_on': '2022-01-02 00:00:00',
                                                                 'is_available': True,                                                                     
                                                                 }])
        management = Management.get_all()
        assert len (management) == 3
    def test_get_all_when_is_empty(Self):
        RepositoryManagement.get_all = MagicMock(return_value = [])
        management = RepositoryManagement.get_all()
        assert management == []
    
    def test_get_all_when_excetpion_occurs(self):
        RepositoryManagement.get_all = MagicMock(side_effect=Exception)
        with pytest.raises(Exception, match=r".*Management Service - get_all error:*") : Management.get_all()

    def test_get_partner_by_id_when_it_finds_value (self):
        row_tested = {'id': 3, 
                       'partner_id': 4, 
                       'price': 1000,
                       'tax_rate': 2,
                       'property_tax': 2,
                       'is_available': True
                       }

        RepositoryManagement.get_by_partner_id = MagicMock(id, return_value = [{'id': 3, 
                                                                 'partner_id': 4,
                                                                 'price': 1000,
                                                                 'tax_rate': 2,
                                                                 'property_tax': 2,
                                                                 'is_available': True}])
        repositoryManagement = RepositoryManagement.get_by_partner_id(id)
        assert row_tested == repositoryManagement[0]
    
    def test_get_partner_by_id_when_not_find_any_value(self):
        partner_id = 4
        RepositoryManagement.get_by_partner_id = MagicMock(id, return_value = [])
        repositoryManagement = RepositoryManagement.get_by_partner_id(id)
        assert repositoryManagement == []

    def test_get_partner_by_id_when_return_is_invalid(self):
        partner_id = 4
        RepositoryManagement.get_by_partner_id = MagicMock(id, return_value = {'id': 3, 
                                                            'partner_id': 4,
                                                            'price': 1000,
                                                            'tax_rate': 2,
                                                            'property_tax': 2,
                                                            'is_available': True})
        with pytest.raises(Exception, match=r".*Management Service - get_by_partner_id error*") : Management.get_by_partner_id (partner_id)

    def test_get_partner_by_id_when_exception_occurs(self):
        partner_id = 1
        RepositoryManagement.get_by_partner_id = MagicMock(side_effect = Exception)
        with pytest.raises(Exception, match=r".*Management Service - get_by_partner_id error*") : Management.get_by_partner_id (partner_id)

    #TENTATIVA DE TESTE DE INSERÇÃO NO BANCO MOCKADO
    # def test_adding_property(self):
    #     data_atual = datetime.now()
    #     row_tested = {'id': 1, 
    #                    'partner_id': 1, 
    #                    'price': 1,
    #                    'tax_rate': 1,
    #                    'property_tax': 1,
    #                    'created_on': data_atual,
    #                    'is_available': False
    #                    }
    #     self.fixture_db_conecction()
    #     self.fixed_rows()
    #     RepositoryManagement.add(1,1,1,1,datetime.now(),False)
    #     # assert row_tested == RepositoryManagement.get_by_partner_id(1)

    