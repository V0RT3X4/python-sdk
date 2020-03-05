"""
Let's retrieve the daily sum of Chinese Crude/Condensate imports, over the last year.

The below script returns:

|     | key                      |    value |   count |
|----:|:-------------------------|---------:|--------:|
|   0 | 2019-01-01T00:00:00.000Z |  1237381 |       9 |
|   1 | 2019-01-02T00:00:00.000Z |  6548127 |      23 |
|   2 | 2019-01-03T00:00:00.000Z | 45457617 |      23 |
|   3 | 2019-01-04T00:00:00.000Z |  6467759 |      43 |
|   4 | 2019-01-05T00:00:00.000Z |  7777144 |       4 |
...

"""
from datetime import datetime

from vortexasdk import CargoTimeSeries, Geographies, Products

if __name__ == "__main__":
    # Find china ID
    china = [
        g.id
        for g in Geographies().search(term="china").to_list()
        if "country" in g.layer
    ]

    # Find Crude/Condensates ID
    crude_condensates = [
        p.id
        for p in Products().search(term="Crude/Condensates").to_list()
        if p.name == "Crude/Condensates"
    ]

    # Query API
    search_result = CargoTimeSeries().search(
        # We're only interested in movements into China
        filter_destinations=china,
        # We're looking at daily imports
        timeseries_frequency="day",
        # We want 'b' for barrels here
        timeseries_unit="b",
        # We're only interested in Crude/Condensates
        filter_products=crude_condensates,
        # We want all cargo movements that unloaded in 2019 to be included
        filter_activity="unloading_start",
        filter_time_min=datetime(2019, 1, 1),
        filter_time_max=datetime(2019, 12, 31),
    )

    # Convert search result to dataframe
    df = search_result.to_df()
