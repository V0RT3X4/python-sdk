# from cargo_movements import CargoMovements
# from python_sdk.vessels import Vessels
# import pandas as pd
# ids = [
#     "6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509",
#     "bf2b55bd31c709aa4cba91a3cc4111191c88c83753cbd285674c22150e42003e"
# ]
#
# Vessels().search(ids=ids).to_list()
# vessels = Vessels().search(ids=ids).to_df()
#
#
# v = Vessels().search(vessel_classes=['vlcc'], term='ocean').to_df(columns=['name', 'imo', 'mmsi', 'related_names'])
#
# from tabulate import tabulate
# print(tabulate(v, headers='keys', tablefmt='pipe'))
#
# c = CargoMovements().search(
#     filter_origins=['68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e'],
#     filter_time_min="2019-08-29T00:00:00.000Z",
#     filter_time_max="2019-10-30T00:00:00.000Z",
# )
#
# print(c)
