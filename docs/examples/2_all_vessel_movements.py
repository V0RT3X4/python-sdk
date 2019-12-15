"""
Let's find some laden vessel movements

The below script returns:

|    | vessel.name       |   vessel.imo |   vessel.mmsi |   vessel.cubic_capacity |   vessel.dwt | vessel.vessel_class   | origin.location.port.label             |   origin.location.sts_zone.label |   origin.from_vessel.label |   origin.to_vessel.label | destination.location.port.label   |   destination.location.sts_zone.label |   destination.from_vessel.label |   destination.to_vessel.label | origin.start_timestamp   | destination.end_timestamp   | cargoes.0.product.group.label   | cargoes.0.product.grade.label   |   cargoes.0.product.grade.probability | vessel.corporate_entities.charterer.label   |   vessel.corporate_entities.time_charterer.label | vessel.corporate_entities.commercial_owner.label   |
|---:|:------------------|-------------:|--------------:|------------------------:|-------------:|:----------------------|:---------------------------------------|---------------------------------:|---------------------------:|-------------------------:|:----------------------------------|--------------------------------------:|--------------------------------:|------------------------------:|:-------------------------|:----------------------------|:--------------------------------|:--------------------------------|--------------------------------------:|:--------------------------------------------|-------------------------------------------------:|:---------------------------------------------------|
|  0 | 17 FEBRUARY       |  9.38089e+06 |     248896000 |                  172092 |       160391 | suezmax               | Ras Tanura [SA]                        |                              nan |                        nan |                      nan | Malacca (Melaka) [MY]             |                                   nan |                             nan |                           nan | 2017-09-29T18:30:01+0000 | 2017-10-16T04:06:03+0000    | Crude                           | Arab Light                      |                              0.299732 | nan                                         |                                              nan | CORE PETROLEUM                                     |
|  3 | A MELODY          |  9.24931e+06 |     636019335 |                  169352 |       149995 | suezmax               | Ras Tanura [SA]                        |                              nan |                        nan |                      nan | Rayong [TH]                       |                                   nan |                             nan |                           nan | 2017-09-20T09:15:15+0000 | 2017-10-09T20:07:28+0000    | Crude                           | Arab Light                      |                              0.903729 | THAI OIL                                    |                                              nan | LMCS Maritime                                      |
|  4 | A STAR            |  9.00660e+06 |     511801000 |                  333924 |       291381 | vlcc_plus             | nan                                    |                              nan |                        nan |                      nan | nan                               |                                   nan |                             nan |                           nan | nan                      | 2017-10-08T14:50:01+0000    | Crude                           | nan                             |                            nan        | nan                                         |                                              nan | nan                                                |
|  5 | A STAR            |  9.15982e+06 |     356206000 |                    9716 |        11047 | general_purpose       | Shahid Rajaee Port (Bandar Abbas) [IR] |                              nan |                        nan |                      nan | Haldia [IN]                       |                                   nan |                             nan |                           nan | 2017-09-23T23:59:30+0000 | 2017-10-16T01:49:00+0000    | Dirty products                  | Bitumen                         |                              1        | nan                                         |                                              nan | nan                                                |
| 10 | ABDIAS NASCIMENTO |  9.4539e+06  |     710032990 |                  171000 |       157055 | suezmax               | Marlim Sul Field [BR]                  |                              nan |                        nan |                      nan | Sao Francisco Do Sul, SC [BR]     |                                   nan |                             nan |                           nan | 2017-09-28T18:29:45+0000 | 2017-10-04T23:05:32+0000    | Crude                           | nan                             |                            nan        | nan                                         |                                              nan | PETROBRAS                                          |
| 11 | ABIOLA            |  8.61943e+06 |     657995000 |                   47261 |        35644 | handysize             | Port Harcourt [NG]                     |                              nan |                        nan |                      nan | nan                               |                                   nan |                             nan |                           nan | 2014-12-02T10:20:03+0000 | nan                         | Clean products                  | Full Range                      |                              0.490481 | nan                                         |                                              nan | nan                                                |
| 13 | ABLIANI           |  9.69307e+06 |     256903000 |                  124518 |       109999 | aframax               | Ceyhan [TR]                            |                              nan |                        nan |                      nan | Sarroch (Porto Foxi) [IT]         |                                   nan |                             nan |                           nan | 2017-09-26T21:33:43+0000 | 2017-10-03T15:45:15+0000    | Crude                           | Azeri Light                     |                              1        | nan                                         |                                              nan | Eastern Mediterranean Maritime Ltd                 |
| 19 | AC-D              |  9.42844e+06 |     256934000 |                    8628 |         7842 | tiny_tanker           | Varna [BG]                             |                              nan |                        nan |                      nan | Valencia [ES]                     |                                   nan |                             nan |                           nan | 2017-09-20T08:00:58+0000 | 2017-10-06T15:49:00+0000    | Clean products                  | Finished Biodiesel              |                              0.868073 | nan                                         |                                              nan | nan                                                |
| 20 | ACACIA            |  9.4766e+06  |     371044000 |                   14570 |        13566 | general_purpose       | Bontang, KL [ID]                       |                              nan |                        nan |                      nan | Lianyungang [CN]                  |                                   nan |                             nan |                           nan | 2017-09-28T13:13:57+0000 | 2017-10-07T00:30:46+0000    | Clean products                  | Chemicals                       |                              0.999186 | nan                                         |                                              nan | KOKUKA SANGYO                                      |
| 22 | ACACIA RUBRA      |  9.46853e+06 |     249374000 |                    6000 |         6065 | tiny_tanker           | Mosjoen [NO]                           |                              nan |                        nan |                      nan | Sigerfjord [NO]                   |                                   nan |                             nan |                           nan | 2017-10-01T00:01:53+0000 | 2017-10-06T10:53:20+0000    | Dirty products                  | nan                             |                            nan        | nan                                         |                                              nan | nan                                                |


"""
from datetime import datetime

from docs.utils import to_markdown
from vortexasdk import VesselMovements

# Query the API
search_result = VesselMovements().search(
    filter_time_min=datetime(2017, 10, 1, 0),
    filter_time_max=datetime(2017, 10, 1, 1),
)

# A complete list of available columns can be found at https://v0rt3x4.github.io/python-sdk/endpoints/vessel_movements/#notes
# We only require a subset of available columns here
required_columns = [
    # Show metadata about the vessel
    "vessel.name",
    "vessel.imo",
    "vessel.mmsi",
    "vessel.cubic_capacity",
    "vessel.dwt",
    "vessel.vessel_class",
    # Show any corporate information associated with the vessel
    "vessel.corporate_entities.charterer.label",
    "vessel.corporate_entities.time_charterer.label",
    "vessel.corporate_entities.commercial_owner.label",
    # Show the port, sts_zone, or vessel at the start of the vessel movement
    "origin.location.port.label",
    "origin.location.sts_zone.label",
    "origin.from_vessel.label",
    "origin.to_vessel.label",
    # Show the port, sts_zone, or vessel at the end of the vessel movement
    "destination.location.port.label",
    "destination.location.sts_zone.label",
    "destination.from_vessel.label",
    "destination.to_vessel.label",
    # The start and end timestamps of the movement
    "origin.start_timestamp",
    "destination.end_timestamp",
    # The cargo (if any), onboard the vessel during the vessel movement.
    # If the vessel was balast, then the cargo will be empty.
    "cargoes.0.product.group.label",
    "cargoes.0.product.grade.label",
    "cargoes.0.product.grade.probability",
]

# Convert the search result to a dataframe
vessel_movements = search_result.to_df(columns=required_columns)

# Laden vessel movements are movements with a cargo (unlike ballast movements, where the vessel isn't carrying any cargo).
is_laden_mask = vessel_movements["cargoes.0.product.group.label"].notna()

# Let's find the laden vessel movements.
laden_vessel_movements = vessel_movements[is_laden_mask]

print(to_markdown(laden_vessel_movements.head(10)))
