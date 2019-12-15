from tests.testcases import TestCaseUsingRealAPI
from tests.timer import Timer
from vortexasdk import Products
from vortexasdk.endpoints.vessels import Vessels


class TestVesselsReal(TestCaseUsingRealAPI):
    def test_search_ids(self):
        ids = [
            "6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509",
            "bf2b55bd31c709aa4cba91a3cc4111191c88c83753cbd285674c22150e42003e",
        ]

        vessels = Vessels().search(ids=ids).to_list()
        assert len(vessels) == 2

        print([x.name for x in vessels])

    def test_search_filters_vessel_class(self):
        vessel_classes = ["vlcc_plus", "aframax"]

        vessels = Vessels().search(vessel_classes=vessel_classes).to_list()

        actual = {x.vessel_class for x in vessels}

        assert actual == set(vessel_classes)

    def test_search_terms_are_combined_with_AND(self):
        aframax = set(
            v.id for v in Vessels().search(vessel_classes="aframax").to_list()
        )
        aframax_called_zhen = set(
            v.id
            for v in Vessels()
            .search(vessel_classes="aframax", term="zhen")
            .to_list()
        )

        assert aframax_called_zhen.issubset(aframax)

    def test_search_ids_dataframe(self):
        ids = [
            "6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509",
            "bf2b55bd31c709aa4cba91a3cc4111191c88c83753cbd285674c22150e42003e",
        ]

        df = Vessels().search(ids=ids).to_df()
        assert list(df.columns) == ["id", "name", "imo", "vessel_class"]
        assert len(df) == 2

    def test_find_crude_vessels(self):
        crude = [
            p.id
            for p in Products().search("crude").to_list()
            if "group" in p.layer
        ]
        df = Vessels().search(vessel_product_types=crude).to_df()
        assert len(df) > 1000

    def test_load_all(self):
        all_products = Vessels().load_all()

        assert len(all_products) > 1000

    def test_search_load_all_vessels(self):
        with Timer("Search"):
            result = Vessels().search()

        with Timer("Serialize"):
            result.to_list()

        with Timer("Dataframe"):
            df = result.to_df()
            print(df.head())

        assert len(result) >= 1_000

    def test_search_is_case_agnostic(self):
        uppercase = {
            v.id for v in Vessels().search(vessel_classes="Suezmax").to_list()
        }
        lowercase = {
            v.id for v in Vessels().search(vessel_classes="suezmax").to_list()
        }

        assert uppercase == lowercase
