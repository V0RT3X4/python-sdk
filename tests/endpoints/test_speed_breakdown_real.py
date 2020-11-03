from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import SpeedBreakdown, Geographies, Corporations, Attributes


class TestTonMilesBreakdownReal(TestCaseUsingRealAPI):
    def test_search_returns_one_day(self):
        date = datetime(2019, 11, 10)

        result = SpeedBreakdown().search(
            filter_activity="loading_state",
            filter_time_min=date,
            filter_time_max=date,
        )

        assert len(result) == 1

    # def test_search_returns_all_days(self):
    #     start = datetime(2019, 11, 1)
    #     end = datetime(2019, 11, 10)

    #     result = TonMilesBreakdown().search(
    #         filter_activity="loading_state",
    #         filter_time_min=start,
    #         filter_time_max=end,
    #     )

    #     n_days = (end - start).days + 1

    #     assert n_days == len(result)

    # def test_to_df(self):
    #     start = datetime(2019, 11, 1)
    #     end = datetime(2019, 11, 10)

    #     df = (
    #         TonMilesBreakdown()
    #         .search(
    #             filter_activity="loading_state",
    #             filter_time_min=start,
    #             filter_time_max=end,
    #         )
    #         .to_df()
    #     )

    #     print(to_markdown(df.head()))

    #     n_days = (end - start).days + 1

    #     assert len(df) == n_days
    #     assert list(df.columns) == ["key", "value", "count"]

    # def test_to_list(self):
    #     start = datetime(2019, 11, 1)
    #     end = datetime(2019, 11, 10)

    #     time_series_list = (
    #         TonMilesBreakdown()
    #         .search(
    #             filter_activity="loading_state",
    #             filter_time_min=start,
    #             filter_time_max=end,
    #         )
    #         .to_list()
    #     )

    #     n_days = (end - start).days + 1

    #     assert len(time_series_list) == n_days
