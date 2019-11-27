from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.client import create_client, set_client
from vortexasdk.endpoints.products import Products
from vortexasdk.endpoints.products_result import DEFAULT_COLUMNS


class TestProductsReal(TestCaseUsingRealAPI):
    def test_search_ids(self):
        ids = [
            "e166e6253dd843624f6cbe4fd45e7f2cff4671e600b4d6371172dd92a0255946",
            "6cd99c8f9e67e61892a691237b3342a4caae5ec1c76784b1b93952afda44ae24",
        ]

        products = Products().search(ids=ids).to_list()
        assert len(products) == 2

        print([x.name for x in products])

    def test_search_ids_dataframe(self):
        ids = [
            "e166e6253dd843624f6cbe4fd45e7f2cff4671e600b4d6371172dd92a0255946",
            "6cd99c8f9e67e61892a691237b3342a4caae5ec1c76784b1b93952afda44ae24",
        ]

        df = Products().search(ids=ids).to_df()
        assert list(df.columns) == DEFAULT_COLUMNS
        assert len(df) == 2

    def test_search_ids_dataframe_subset_of_cols(self):
        ids = [
            "e166e6253dd843624f6cbe4fd45e7f2cff4671e600b4d6371172dd92a0255946",
            "6cd99c8f9e67e61892a691237b3342a4caae5ec1c76784b1b93952afda44ae24",
        ]

        df = Products().search(ids=ids).to_df(columns=["name", "id"])
        assert list(df.columns) == ["name", "id"]
        assert len(df) == 2

    def test_search_crude(self):
        set_client(create_client())

        result = [p.id for p in Products().search("Crude").to_list()]

        assert (
            "6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653"
            in result
        )

    def test_search_multiple_terms_to_dataframe(self):
        df = (
            Products()
            .search(term=["diesel", "fuel oil", "grane"])
            .to_df("all")
        )

        assert set(df.columns) == {
            "id",
            "name",
            "layer.0",
            "leaf",
            "parent.0.name",
            "parent.0.layer.0",
            "parent.0.id",
            "meta.api_min",
            "meta.api_max",
            "ref_type",
            "meta.sulphur_min",
            "meta.sulphur_max",
        }

    def test_lookup_crude(self):
        set_client(create_client())

        result = Products().reference(
            "6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653"
        )

        assert result[0]["name"] == "Crude"
