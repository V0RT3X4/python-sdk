from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.conversions import convert_to_vessel_ids
from vortexasdk.endpoints.vessels import Vessels


class TestConvert(TestCaseUsingRealAPI):
    def test_convert_name_to_vessel_ids(self):
        result = convert_to_vessel_ids(["OCEAN"])

        assert len(result) >= 10

    def test_convert_imo_to_vessel_ids(self):
        result = convert_to_vessel_ids([9083287])
        assert result == [
            "84a82843ec84ac6d67b65c50056eff78e0d58e6b9fc7a5ba9adc6c0442162cf4"
        ]

    def test_convert_mmsi_to_vessel_ids(self):
        result = convert_to_vessel_ids([563064200])
        assert result == [
            "b9f5cf3e2a3b17fe2c7eed717f7ab36d481ad69290c28197c7cd00e1669ca66a"
        ]

    def test_convert_class_to_vessel_ids(self):
        result = convert_to_vessel_ids(["panamax"])

        assert result == [
            v.id for v in Vessels().search(vessel_classes="panamax").to_list()
        ]

    def test_convert_combination_to_vessel_ids(self):
        from_mmsi = convert_to_vessel_ids([563064200])
        from_imo = convert_to_vessel_ids([9083287])
        from_name = convert_to_vessel_ids(["OCEAN"])
        from_class = convert_to_vessel_ids(["aframax"])

        result = set(
            convert_to_vessel_ids([563064200, 9083287, "OCEAN", "aframax"])
        )
        assert result == set(from_mmsi + from_imo + from_name + from_class)
