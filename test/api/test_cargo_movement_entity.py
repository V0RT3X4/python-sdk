from unittest import TestCase

import jsons

from python_sdk.api.entities import GeographyEntity, ProductEntity, CorporateEntity, VesselEntity, \
    CargoEventEntity, CargoMovementEntity


class TestCargoMovementEntity(TestCase):

    def test_serialize(self):
        with open("test/api/examples/cargo_movement_entity1.json", 'r') as f:
            serialized = f.read()
            deserialized = jsons.loads(serialized, CargoMovementEntity)

            dictionary = {
                "cargo_movement_id": "00886b05a0747522b67322f50123ee60e61e219fc9a9c6011be1a1dade65f63e",
                "quantity": 4401,
                "status": "unloaded_state",
                "vessels": [
                    VesselEntity(**{
                        "id": "9cbf7c0fc6ccf1dfeacde02b87f3b6b1653030f560d4fc677bf1d7d0be8f8449",
                        "mmsi": 255804460,
                        "imo": 9480980,
                        "name": "JOHANN ESSBERGER",
                        "dwt": 5260,
                        "cubic_capacity": 6100,
                        "vessel_class": "tiny_tanker",
                        "corporate_entities": [
                            CorporateEntity(**{
                                "id": "f9bd45e65e292909a7b751b0026dcf7795c6194b3c0712910a241caee32c99b8",
                                "label": "Essberger J.T.",
                                "layer": "commercial_owner",
                                "probability": 1,
                                "source": "external"
                            })
                        ],
                        "start_timestamp": "2019-10-18T21:38:34+0000",
                        "end_timestamp": "2019-10-25T00:40:46+0000",
                        "fixture_fulfilled": False,
                        "voyage_id": "401f0e74fc42401248a484aca2e9955dea885378796f7f4d0bc8e92c35ea270a",
                        "tags": [],
                        "status": "vessel_status_laden_known"
                    })
                ],
                "product": [
                    ProductEntity(**{
                        "id": "b68cbb746f8b9098c50e2ba36bcad83001a53bd362e9031fb49085d02c36659c",
                        "layer": "group",
                        "probability": 0.4756425,
                        "source": "model",
                        "label": "Clean products"
                    }),
                    ProductEntity(**{
                        "id": "a75fcc09bfc7d16496de3336551bc52b5891838bb7c22356d2cb65451587d1e5",
                        "layer": "group_product",
                        "probability": 0.4756425,
                        "source": "model",
                        "label": "Biodiesel"
                    }),
                    ProductEntity(**{
                        "id": "9d52ede1cff0421a8cd7283b0171afe8d23f519dca5f4e489734522f9cdf804c",
                        "layer": "grade",
                        "probability": 0.4756425,
                        "source": "model",
                        "label": "Biodiesel Feedstock"
                    })
                ],
                "events": [
                    CargoEventEntity(**{
                        "event_type": "cargo_port_load_event",
                        "location": [
                            GeographyEntity(**{
                                "id": "2dfc3d43a21697c02ec3b2700b3b570a6ed1abb66d01c4fe6310ef362fcf6653",
                                "layer": "country",
                                "label": "Netherlands",
                                "source": "model",
                                "probability": 1
                            })
                        ],
                        "probability": 1,
                        "pos": [
                            4.29914090037834,
                            51.87936163368058
                        ],
                        "start_timestamp": "2019-10-18T21:38:34+0000",
                        "end_timestamp": "2019-10-20T16:41:49+0000"
                    })
                ]
            }

            expected = CargoMovementEntity(**dictionary)

            assert expected == deserialized
