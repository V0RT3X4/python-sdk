from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import VesselMovements, Geographies
from vortexasdk.endpoints import vessel_movements_result


class TestVesselMovementsReal(TestCaseUsingRealAPI):
    def test_search(self):
        rotterdam = [
            g.id
            for g in Geographies().search("rotterdam").to_list()
            if "port" in g.layer
        ]
        v = VesselMovements().search(
            filter_time_min=datetime(2017, 10, 1, 0, 0),
            filter_time_max=datetime(2017, 10, 1, 0, 10),
            filter_origins=rotterdam,
        )

        assert len(v) > 10

    def test_to_df_all_columns(self):
        rotterdam = [
            g.id
            for g in Geographies().search("rotterdam").to_list()
            if "port" in g.layer
        ]
        df = (
            VesselMovements()
            .search(
                filter_time_min=datetime(2017, 10, 1, 0, 0),
                filter_time_max=datetime(2017, 10, 1, 0, 10),
                filter_origins=rotterdam,
            )
            .to_df(columns="all")
            .head(2)
        )

        assert len(df) == 2

    def test_search_to_dataframe(self):
        rotterdam = [
            g.id
            for g in Geographies().search("rotterdam").to_list()
            if "port" in g.layer
        ]
        df = (
            VesselMovements()
            .search(
                filter_time_min=datetime(2017, 10, 1, 0, 0),
                filter_time_max=datetime(2017, 10, 1, 0, 10),
                filter_origins=rotterdam,
            )
            .to_df()
            .head(2)
        )

        assert list(df.columns) == vessel_movements_result.DEFAULT_COLUMNS
        assert len(df) == 2

    def test_search_to_dataframe_subset_of_columns(self):
        cols = ["vessel.imo", "vessel.name"]

        rotterdam = [
            g.id
            for g in Geographies().search("rotterdam").to_list()
            if "port" in g.layer
        ]
        df = (
            VesselMovements()
            .search(
                filter_time_min=datetime(2017, 10, 1, 0, 0),
                filter_time_max=datetime(2017, 10, 1, 0, 10),
                filter_origins=rotterdam,
            )
            .to_df(columns=cols)
            .head(2)
        )

        assert list(df.columns) == cols
        assert len(df) == 2
