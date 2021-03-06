import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

import csv
from util import Log
from Repository.region import Region as RepositoryRegion


class Region:
    def get_all():
        try:
            data = RepositoryRegion.get_all()
            if (data):
                return data
            return []
        except Exception as ex:
            error = "Region Service - get_all error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)

    def link():
        try:
            with open('drafts/region.csv', encoding="utf8") as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    region = row[0]
                    district = row[1]
                    region_id = RepositoryRegion.get_by_name(region)
                    district_id = RepositoryRegion.get_district_by_name(district)
                    if region_id > 0 and district_id > 0:
                        RepositoryRegion.link(region_id, district_id)

        except Exception as ex:
            error = "Region Service - link error: {} \n".format(ex)
            Log.print(error, True)
            raise Exception(error)
