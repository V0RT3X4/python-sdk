from unittest import TestCase

import jsons

from vortexasdk.api.geography import GeographyEntity


class TestGeographyEntity(TestCase):
    def test_serialize(self):
        with open("tests/api/examples/geography_entity1.json", "r") as f:
            serialized = f.read()
            deserialized = jsons.loads(serialized, GeographyEntity)

            print(serialized)
            print(deserialized)

            expected = GeographyEntity(
                id="2aaad41b89dfad19e5668918018ae02695d7710bcbe5f2dc689234e8da492de3",
                layer="country",
                label="United Kingdom",
                source="model",
                probability=1,
            )

            assert expected == deserialized
