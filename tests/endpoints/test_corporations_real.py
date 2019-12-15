from tests.testcases import TestCaseUsingRealAPI
from docs.utils import to_markdown
from vortexasdk import Corporations


class TestCorporationsReal(TestCaseUsingRealAPI):
    def test_search(self):
        df = Corporations().search().to_df()

        print(to_markdown(df.head(2)))

    def test_load_all(self):
        all_corporations = Corporations().load_all()

        assert len(all_corporations) > 1000
