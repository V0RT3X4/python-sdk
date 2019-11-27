from tests.testcases import TestCaseUsingMockAPI
from vortexasdk.endpoints.products import Products


class TestProducts(TestCaseUsingMockAPI):
    def test_search_ids_retreives_names(self):
        products = Products().search().to_df()
        assert len(products) > 0
