from unittest import TestCase

import pandas as pd

from tests.mock_client import example_vessels
from vortexasdk.endpoints.vessels_result import VesselsResult


class TestVesselsSearchResult(TestCase):
    vsr = VesselsResult(example_vessels)

    def test_to_df(self):
        df = self.vsr.to_df("all")

        expected = pd.DataFrame(
            {
                "call_sign": {0: "3269", 1: "839"},
                "dead_weight": {0: 6403, 1: 5000},
                "id": {
                    0: "1f6145c6e8134bed20a48d5a2a77732ffb2fe4e679b4297b25582dcb93dfaa84",
                    1: "1761da4fb069cd6ce153b6ad1c48e15cdb994eb386e4aafbe8f1bbde993cbaef",
                },
                "mmsi": {0: 900403269, 1: 413771781},
                "name": {0: "0", 1: "058"},
                "to_bow": {0: 120, 1: 18},
                "to_port": {0: 30, 1: 47},
                "to_starboard": {0: 5, 1: 36},
                "to_stern": {0: 5, 1: 28},
                "related_names": {0: ["0"], 1: ["058"]},
                "current_product_type": {
                    0: [
                        {
                            "cargo_movement_id": "12d2cbca522e5570ea988b30850ad5b762e16d1b710e920f26729f08fcfdca46",
                            "product_type": [
                                {
                                    "id": "b68cbb746f8b9098c50e2ba36bcad83001a53bd362e9031fb49085d02c36659c",
                                    "layer": "group",
                                    "label": "Clean products",
                                },
                                {
                                    "id": "cbb5acffa542aad31d26712a8cdfd9884301aa7658ac95c40f86ddb31bc29d9b",
                                    "layer": "group_product",
                                    "label": "Other Clean products",
                                },
                            ],
                            "active": False,
                        }
                    ],
                    1: [
                        {
                            "cargo_movement_id": "5b74c0aab0353cccb28a1bed34c04d7fa54120efb32de10f8f0429c00dd8d536",
                            "product_type": [
                                {
                                    "id": "b68cbb746f8b9098c50e2ba36bcad83001a53bd362e9031fb49085d02c36659c",
                                    "layer": "group",
                                    "label": "Clean products",
                                },
                                {
                                    "id": "cbb5acffa542aad31d26712a8cdfd9884301aa7658ac95c40f86ddb31bc29d9b",
                                    "layer": "group_product",
                                    "label": "Other Clean products",
                                },
                            ],
                            "active": False,
                        },
                        {
                            "cargo_movement_id": "8709d0cf0d103349c6df89f4b53ac90babc89e53c966f8cbf42aa0e93be20d96",
                            "product_type": [
                                {
                                    "id": "b68cbb746f8b9098c50e2ba36bcad83001a53bd362e9031fb49085d02c36659c",
                                    "layer": "group",
                                    "label": "Clean products",
                                },
                                {
                                    "id": "a75fcc09bfc7d16496de3336551bc52b5891838bb7c22356d2cb65451587d1e5",
                                    "layer": "group_product",
                                    "label": "Biodiesel",
                                },
                            ],
                            "active": False,
                        },
                    ],
                },
                "parent": {
                    0: [
                        {
                            "name": "Tiny Tanker",
                            "layer": ["vessel_class"],
                            "id": "tiny_tanker",
                        }
                    ],
                    1: [
                        {
                            "name": "Tiny Tanker",
                            "layer": ["vessel_class"],
                            "id": "tiny_tanker",
                        }
                    ],
                },
                "ref_type": {0: "vessel", 1: "vessel"},
                "vessel_status": {
                    0: "vessel_status_ballast",
                    1: "vessel_status_laden_unknown",
                },
                "corporate_entities": {0: [], 1: []},
                "leaf": {0: True, 1: True},
                "vessel_class": {0: "tiny_tanker", 1: "tiny_tanker"},
                "cubic_capacity": {0: 7060, 1: 6318},
                "tags": {
                    0: [
                        {
                            "tag": "vessel_decommissioned_tag",
                            "start_timestamp": "2016-06-08T09:44:57+0000",
                        }
                    ],
                    1: [
                        {
                            "tag": "vessel_decommissioned_tag",
                            "start_timestamp": "2017-07-11T13:42:37+0000",
                        }
                    ],
                },
                "layer": {0: ["vessel"], 1: ["vessel"]},
            }
        )

        assert expected.equals(df)
