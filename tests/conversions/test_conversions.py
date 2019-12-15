from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import Geographies
from vortexasdk.conversions import (
    convert_to_corporation_ids,
    convert_to_geography_ids,
    convert_to_product_ids,
)


class TestConvert(TestCaseUsingRealAPI):
    def test_convert_to_geography_ids(self):
        rotterdam_id = (
            "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"
        )
        rotterdam_name = Geographies().reference(rotterdam_id)["name"]

        result = convert_to_geography_ids([rotterdam_name])

        assert [rotterdam_id] == result

    def test_convert_to_corporation_ids(self):
        result = convert_to_corporation_ids(["DHT"])

        assert len(result) >= 1

    def test_convert_to_product_ids(self):
        result = convert_to_product_ids(["crude"])

        CRUDE_ID = (
            "6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653"
        )
        assert CRUDE_ID in result

    def test_convert_to_ids_retains_id_argument(self):
        id = "f00e3068faf65af1345067f11dc6723b8da324a6f33c000118fccd81947deb4e"
        corporation_result = convert_to_corporation_ids(["DHT"])
        corporation_result_with_id = convert_to_corporation_ids(["DHT", id])

        assert corporation_result_with_id == [id] + corporation_result
