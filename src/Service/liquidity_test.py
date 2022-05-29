import pytest
from liquidity import Liquidity
from Repository.liquidity import Liquidity as RepositoryLiquidity
from unittest.mock import MagicMock
from unittest import mock 

class TestLiquidity:
    def test_get_liquidity_by_district_with_zero_properties_sold(self):
        RepositoryLiquidity.get_properties_by_district = MagicMock(return_value = 10)
        RepositoryLiquidity.get_sold_properties_by_district = MagicMock(return_value = 0)
        liquidity = Liquidity.get_by_district('teste', 1)
        assert 0 == liquidity

    def test_get_liquidity_by_district_with_zero_properties_in_district(self):
        RepositoryLiquidity.get_properties_by_district = MagicMock(return_value = 0)
        RepositoryLiquidity.get_sold_properties_by_district = MagicMock(return_value = 0)
        liquidity = Liquidity.get_by_district('teste',1)
        assert 0 == liquidity

    def test_get_liquidity_by_district(self):
        RepositoryLiquidity.get_properties_by_district = MagicMock(return_value = 10)
        RepositoryLiquidity.get_sold_properties_by_district = MagicMock(return_value = 10)
        liquidity = Liquidity.get_by_district('teste',1)
        assert 1 == liquidity

    def test_get_liquidity_by_district_raise_exception(self):
        RepositoryLiquidity.get_properties_by_district = MagicMock(side_effect = Exception)        
        with pytest.raises(Exception, match=r".*Liquidity Service - get_by_district error:*") : Liquidity.get_by_district('teste',1)

    def test_get_liquidity_by_street_with_zero_property_in_street(self):
        RepositoryLiquidity.get_properties_by_street = MagicMock(return_value = 0)
        RepositoryLiquidity.get_sold_properties_by_street = MagicMock(return_value = 0)
        liquidity = Liquidity.get_by_street('teste', 1)
        assert 0 == liquidity
    
    def test_get_liquidity_by_street_with_one_property_in_street_and_zero_sold(self):
        RepositoryLiquidity.get_properties_by_street = MagicMock(return_value = 1)
        RepositoryLiquidity.get_sold_properties_by_street = MagicMock(return_value = 0)
        liquidity = Liquidity.get_by_street('teste', 1)
        assert 0 == liquidity

    def test_get_liquidity_by_street_with_one_property_in_street_and_one_sold(self):
        RepositoryLiquidity.get_properties_by_street = MagicMock(return_value = 1)
        RepositoryLiquidity.get_sold_properties_by_street = MagicMock(return_value = 1)
        liquidity = Liquidity.get_by_street('teste', 1)
        assert 1 == liquidity

    def test_get_liquidity_by_street_raises_exception(self):
        RepositoryLiquidity.get_properties_by_street = MagicMock(side_effect = Exception)        
        with pytest.raises(Exception, match=r".*Liquidity Service - get_by_street error:*") : Liquidity.get_by_street('teste',1)


    # def get_by_district(name, month):    
    #     try:
    #         liquidity = 0
    #         date = Date.get_mininum_date(month)
    #         total_properties = RepositoryLiquidity.get_properties_by_district(name)
    #         total_sold_properties = RepositoryLiquidity.get_sold_properties_by_district(name, date)            
    #         if(total_properties > 0):
    #             liquidity = total_sold_properties/total_properties            
    #         return liquidity                  
    #     except Exception as ex:            
    #         error = "Liquidity Service - get_by_district error: {} \n".format(ex)
    #         Log.print(error, True)
    #         raise Exception(error)