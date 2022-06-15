import pytest
from Service.region import Region
from Repository.region import Region as RepositoryRegion
from unittest.mock import MagicMock


class TestRegion:
    def test_get_all_should_return_the_list_of_all_regions(self):
        RepositoryRegion.get_all = MagicMock(return_value=[{'id': 1},
                                                           {'id': 2},
                                                           {'id': 3}])
        regions = Region.get_all()
        assert len(regions) == 3

    def test_get_all_should_return_empty_list_when_not_found(self):
        RepositoryRegion.get_all = MagicMock(return_value=[])
        regions = Region.get_all()
        assert regions == []

    def test_get_all_should_raise_exception(self):
        RepositoryRegion.get_all = MagicMock(side_effect=Exception)
        with pytest.raises(Exception, match=r".*Region Service - get_all error:*"):
            Region.get_all()
