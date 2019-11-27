from tests.testcases import TestCaseUsingRealAPI
from tests.utils import to_markdown
from vortexasdk import Corporations


class TestCorporationsReal(TestCaseUsingRealAPI):
    def test_search(self):
        df = Corporations().search().to_df()

        print(to_markdown(df.head(2)))
