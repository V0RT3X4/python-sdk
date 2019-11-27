from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import VesselMovements
from vortexasdk.endpoints import vessel_movements_result


class TestVesselMovementsReal(TestCaseUsingRealAPI):
    def test_search(self):
        v = VesselMovements().search(
            filter_time_min="2019-10-01T00:00:00.000Z",
            filter_time_max="2019-10-01T00:10:00.000Z",
            filter_origins="rotterdam",
        )

        assert len(v) > 10

    def test_search_to_dataframe(self):
        df = (
            VesselMovements()
            .search(
                filter_time_min="2017-10-01T00:00:00.000Z",
                filter_time_max="2017-10-01T00:10:00.000Z",
                filter_origins="rotterdam",
            )
            .to_df()
            .head(2)
        )

        assert list(df.columns) == vessel_movements_result.DEFAULT_COLUMNS
        assert len(df) == 2

    def test_search_to_dataframe_subset_of_columns(self):
        cols = ["vessel.imo", "vessel.name"]
        df = (
            VesselMovements()
            .search(
                filter_time_min="2017-10-01T00:00:00.000Z",
                filter_time_max="2017-10-01T00:10:00.000Z",
                filter_origins="rotterdam",
            )
            .to_df(columns=cols)
            .head(2)
        )

        assert list(df.columns) == cols
        assert len(df) == 2
