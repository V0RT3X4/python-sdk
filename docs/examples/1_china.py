"""
Let's retrieve all the VLCCs that have discharged into China in the last 3 months.

The below script returns:

|    | events.cargo_port_unload_event.0.start_timestamp   | product.group.label   | product.grade.label   |   quantity | vessels.0.name   |
|---:|:---------------------------------------------------|:----------------------|:----------------------|-----------:|:-----------------|
|  0 | 2019-10-08T00:41:00+0000                           | Crude                 | Djeno                 |     123457 | AROME            |
|  1 | 2019-11-08T00:41:52+0000                           | Crude                 | Arab Medium           |      99898 | SCOOBYDOO        |
|  2 | 2019-09-30T23:49:41+0000                           | Crude                 | Arab Heavy            |    9879878 | DAVID            |
|  3 | 2019-12-01T01:40:00+0000                           | Crude                 | Usan                  |     999999 | DUCK             |


"""
from datetime import datetime

from vortexasdk import CargoMovements, Geographies, Vessels

# Find china ID
china = [
    g.id
    for g in Geographies().search(term="china").to_list()
    if "country" in g.layer
]

# Find the ID of all VLCCs
vlccs = [v.id for v in Vessels().search(vessel_classes="vlcc_plus")]

# Query API
search_result = CargoMovements().search(
    filter_activity="loading_start",
    filter_vessels=vlccs,
    filter_destinations=china,
    filter_time_min=datetime(2019, 8, 29),
    filter_time_max=datetime(2019, 10, 30),
)

# Convert search result to dataframe
df = search_result.to_df()
