from typing import List
from unittest import TestCase

import jsons

from vortexasdk.api import (
    CargoEvent,
    CargoMovement,
    CorporateEntity,
    GeographyEntity,
    ProductEntity,
    VesselEntity,
)
from vortexasdk.api.entity_flattening import (
    convert_cargo_movement_to_flat_dict,
)
from vortexasdk.api.serdes import serialize_to_dict
from vortexasdk.api import (
    CargoEvent,
    CargoMovement,
    CorporateEntity,
    GeographyEntity,
    ProductEntity,
    VesselEntity,
)


class TestCargoMovement(TestCase):
    dictionary = {
        "cargo_movement_id": "00886b05a0747522b67322f50123ee60e61e219fc9a9c6011be1a1dade65f63e",
        "quantity": 4401,
        "status": "unloaded_state",
        "vessels": [
            VesselEntity(
                **{
                    "id": "9cbf7c0fc6ccf1dfeacde02b87f3b6b1653030f560d4fc677bf1d7d0be8f8449",
                    "mmsi": 255804460,
                    "imo": 9480980,
                    "name": "JOHANN ESSBERGER",
                    "dwt": 5260,
                    "cubic_capacity": 6100,
                    "vessel_class": "tiny_tanker",
                    "corporate_entities": [
                        CorporateEntity(
                            **{
                                "id": "f9bd45e65e292909a7b751b0026dcf7795c6194b3c0712910a241caee32c99b8",
                                "label": "Essberger J.T.",
                                "layer": "commercial_owner",
                                "probability": 1,
                                "source": "external",
                            }
                        )
                    ],
                    "start_timestamp": "2019-10-18T21:38:34+0000",
                    "end_timestamp": "2019-10-25T00:40:46+0000",
                    "fixture_fulfilled": False,
                    "voyage_id": "401f0e74fc42401248a484aca2e9955dea885378796f7f4d0bc8e92c35ea270a",
                    "tags": [],
                    "status": "vessel_status_laden_known",
                }
            )
        ],
        "product": [
            ProductEntity(
                **{
                    "id": "b68cbb746f8b9098c50e2ba36bcad83001a53bd362e9031fb49085d02c36659c",
                    "layer": "group",
                    "probability": 0.4756425,
                    "source": "model",
                    "label": "Clean products",
                }
            ),
            ProductEntity(
                **{
                    "id": "a75fcc09bfc7d16496de3336551bc52b5891838bb7c22356d2cb65451587d1e5",
                    "layer": "group_product",
                    "probability": 0.4756425,
                    "source": "model",
                    "label": "Biodiesel",
                }
            ),
            ProductEntity(
                **{
                    "id": "9d52ede1cff0421a8cd7283b0171afe8d23f519dca5f4e489734522f9cdf804c",
                    "layer": "grade",
                    "probability": 0.4756425,
                    "source": "model",
                    "label": "Biodiesel Feedstock",
                }
            ),
        ],
        "events": [
            CargoEvent(
                **{
                    "event_type": "cargo_port_load_event",
                    "location": [
                        GeographyEntity(
                            **{
                                "id": "2dfc3d43a21697c02ec3b2700b3b570a6ed1abb66d01c4fe6310ef362fcf6653",
                                "layer": "country",
                                "label": "Netherlands",
                                "source": "model",
                                "probability": 1,
                            }
                        )
                    ],
                    "probability": 1,
                    "pos": [4.29914090037834, 51.87936163368058],
                    "start_timestamp": "2019-10-18T21:38:34+0000",
                    "end_timestamp": "2019-10-20T16:41:49+0000",
                }
            )
        ],
    }

    cm = CargoMovement(**dictionary)

    def test_serialize(self):
        with open("tests/api/examples/cargo_movements.json", "r") as f:
            serialized = f.read()
            deserialized = jsons.loads(serialized, List[CargoMovement])

            assert [self.cm] == deserialized

    def test_convert_to_flat_dict(self):
        flat = convert_cargo_movement_to_flat_dict(serialize_to_dict(self.cm))

        expected = {
            "cargo_movement_id": "00886b05a0747522b67322f50123ee60e61e219fc9a9c6011be1a1dade65f63e",
            "events.cargo_port_load_event.0.end_timestamp": "2019-10-20T16:41:49+0000",
            "events.cargo_port_load_event.0.event_type": "cargo_port_load_event",
            "events.cargo_port_load_event.0.location.country.id": "2dfc3d43a21697c02ec3b2700b3b570a6ed1abb66d01c4fe6310ef362fcf6653",
            "events.cargo_port_load_event.0.location.country.label": "Netherlands",
            "events.cargo_port_load_event.0.location.country.layer": "country",
            "events.cargo_port_load_event.0.location.country.probability": 1,
            "events.cargo_port_load_event.0.location.country.source": "model",
            "events.cargo_port_load_event.0.pos.0": 4.29914090037834,
            "events.cargo_port_load_event.0.pos.1": 51.87936163368058,
            "events.cargo_port_load_event.0.probability": 1,
            "events.cargo_port_load_event.0.start_timestamp": "2019-10-18T21:38:34+0000",
            "events.cargo_port_load_event.0.vessel_id": None,
            "product.group.id": "b68cbb746f8b9098c50e2ba36bcad83001a53bd362e9031fb49085d02c36659c",
            "product.group.label": "Clean products",
            "product.group.layer": "group",
            "product.group.probability": 0.4756425,
            "product.group.source": "model",
            "product.group_product.id": "a75fcc09bfc7d16496de3336551bc52b5891838bb7c22356d2cb65451587d1e5",
            "product.group_product.label": "Biodiesel",
            "product.group_product.layer": "group_product",
            "product.group_product.probability": 0.4756425,
            "product.group_product.source": "model",
            "product.grade.id": "9d52ede1cff0421a8cd7283b0171afe8d23f519dca5f4e489734522f9cdf804c",
            "product.grade.label": "Biodiesel Feedstock",
            "product.grade.layer": "grade",
            "product.grade.probability": 0.4756425,
            "product.grade.source": "model",
            "quantity": 4401,
            "status": "unloaded_state",
            "vessels.0.corporate_entities.commercial_owner.id": "f9bd45e65e292909a7b751b0026dcf7795c6194b3c0712910a241caee32c99b8",
            "vessels.0.corporate_entities.commercial_owner.label": "Essberger J.T.",
            "vessels.0.corporate_entities.commercial_owner.layer": "commercial_owner",
            "vessels.0.corporate_entities.commercial_owner.probability": 1,
            "vessels.0.corporate_entities.commercial_owner.source": "external",
            "vessels.0.cubic_capacity": 6100,
            "vessels.0.dwt": 5260,
            "vessels.0.end_timestamp": "2019-10-25T00:40:46+0000",
            "vessels.0.fixture_fulfilled": False,
            "vessels.0.fixture_id": None,
            "vessels.0.id": "9cbf7c0fc6ccf1dfeacde02b87f3b6b1653030f560d4fc677bf1d7d0be8f8449",
            "vessels.0.imo": 9480980,
            "vessels.0.mmsi": 255804460,
            "vessels.0.name": "JOHANN ESSBERGER",
            "vessels.0.start_timestamp": "2019-10-18T21:38:34+0000",
            "vessels.0.status": "vessel_status_laden_known",
            "vessels.0.vessel_class": "tiny_tanker",
            "vessels.0.voyage_id": "401f0e74fc42401248a484aca2e9955dea885378796f7f4d0bc8e92c35ea270a",
        }

        assert flat == expected
