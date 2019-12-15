from tests.testcases import TestCaseUsingRealAPI
from docs.utils import to_markdown
from vortexasdk import Geographies


class TestGeographiesReal(TestCaseUsingRealAPI):
    def test_search(self):
        geographies = Geographies().search(term=["Liverpool", "Southampton"])
        names = [g["name"] for g in geographies]

        assert "Liverpool [GB]" in names

    def test_search_to_df(self):
        geographies = (
            Geographies().search(term=["Liverpool", "Southampton"]).to_df()
        )

        print(to_markdown(geographies))
