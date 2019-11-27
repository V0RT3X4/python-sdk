from unittest import TestCase

import jsons

from vortexasdk.api.cargo_movement import CargoEvent
from vortexasdk.api.geography import GeographyEntity


class TestCargoEventEntity(TestCase):
    def test_serialize(self):
        with open("tests/api/examples/cargo_event_entity1.json", "r") as f:
            serialized = f.read()
            deserialized = jsons.loads(serialized, CargoEvent)

            expected = CargoEvent(
                event_type="cargo_port_unload_event",
                location=[
                    GeographyEntity(
                        id="2aaad41b89dfad19e5668918018ae02695d7710bcbe5f2dc689234e8da492de3",
                        layer="country",
                        label="United Kingdom",
                        source="model",
                        probability=1,
                    )
                ],
                probability=1,
                pos=[-0.256674902984994, 53.74191566386998],
                start_timestamp="2019-10-24T13:16:43+0000",
                end_timestamp="2019-10-25T00:40:46+0000",
            )

            assert expected == deserialized
