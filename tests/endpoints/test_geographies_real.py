from tests.testcases import TestCaseUsingRealAPI
from docs.utils import to_markdown
from vortexasdk import Geographies


class TestGeographiesReal(TestCaseUsingRealAPI):
    def test_search(self):
        geographies = Geographies().search(term=["Liverpool", "Southampton"])
        names = [g["name"] for g in geographies]

        assert "Liverpool [GB]" in names

    def test_load_all(self):
        all_geogs = Geographies().load_all()

        assert len(all_geogs) > 1000

    def test_search_empty_args(self):
        Geographies().search()

    def test_search_to_df(self):
        geographies = (
            Geographies().search(term=["Liverpool", "Southampton"]).to_df()
        )

        print(to_markdown(geographies))
