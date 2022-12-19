# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CssRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CSS")


    CN_SOUTH_1 = Region(id="cn-south-1", endpoint="https://css.cn-south-1.myhuaweicloud.com")

    CN_EAST_3 = Region(id="cn-east-3", endpoint="https://css.cn-east-3.myhuaweicloud.com")

    CN_NORTH_4 = Region(id="cn-north-4", endpoint="https://css.cn-north-4.myhuaweicloud.com")

    CN_NORTH_2 = Region(id="cn-north-2", endpoint="https://css.cn-north-2.myhuaweicloud.com")

    CN_NORTH_1 = Region(id="cn-north-1", endpoint="https://es.cn-north-1.myhuaweicloud.com")

    CN_NORTH_9 = Region(id="cn-north-9", endpoint="https://css.cn-north-9.myhuaweicloud.com")

    CN_EAST_2 = Region(id="cn-east-2", endpoint="https://es.cn-east-2.myhuaweicloud.com")

    CN_SOUTH_4 = Region(id="cn-south-4", endpoint="https://css.cn-south-4.myhuaweicloud.com")

    CN_SOUTHWEST_2 = Region(id="cn-southwest-2", endpoint="https://css.cn-southwest-2.myhuaweicloud.com")

    AP_SOUTHEAST_2 = Region(id="ap-southeast-2", endpoint="https://css.ap-southeast-2.myhuaweicloud.com")

    AP_SOUTHEAST_3 = Region(id="ap-southeast-3", endpoint="https://css.ap-southeast-3.myhuaweicloud.com")

    AP_SOUTHEAST_1 = Region(id="ap-southeast-1", endpoint="https://css.ap-southeast-1.myhuaweicloud.com")

    SA_BRAZIL_1 = Region(id="sa-brazil-1", endpoint="https://css.sa-brazil-1.myhuaweicloud.com")

    NA_MEXICO_1 = Region(id="na-mexico-1", endpoint="https://css.na-mexico-1.myhuaweicloud.com")

    LA_NORTH_2 = Region(id="la-north-2", endpoint="https://css.la-north-2.myhuaweicloud.com")

    AF_SOUTH_1 = Region(id="af-south-1", endpoint="https://css.af-south-1.myhuaweicloud.com")

    LA_SOUTH_2 = Region(id="la-south-2", endpoint="https://css.la-south-2.myhuaweicloud.com")

    CN_SOUTH_2 = Region(id="cn-south-2", endpoint="https://css.cn-south-2.myhuaweicloud.com")

    static_fields = {
        "cn-south-1": CN_SOUTH_1,
        "cn-east-3": CN_EAST_3,
        "cn-north-4": CN_NORTH_4,
        "cn-north-2": CN_NORTH_2,
        "cn-north-1": CN_NORTH_1,
        "cn-north-9": CN_NORTH_9,
        "cn-east-2": CN_EAST_2,
        "cn-south-4": CN_SOUTH_4,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "sa-brazil-1": SA_BRAZIL_1,
        "na-mexico-1": NA_MEXICO_1,
        "la-north-2": LA_NORTH_2,
        "af-south-1": AF_SOUTH_1,
        "la-south-2": LA_SOUTH_2,
        "cn-south-2": CN_SOUTH_2,
    }

    @classmethod
    def value_of(cls, region_id, static_fields=None):
        if not region_id:
            raise KeyError("Unexpected empty parameter: region_id.")

        fields = static_fields if static_fields else cls.static_fields

        region = cls._PROVIDER.get_region(region_id)
        if region:
            return region

        if region_id in fields:
            return fields.get(region_id)

        raise KeyError("Unexpected region_id: " + region_id)


