from unittest import TestCase

from api.timeseries_item import KeyValueCount


class TestKeyValueCount(TestCase):
    def test_get_set(self):
        item = KeyValueCount("k", 0.7, 100)

        assert item.key == "k"
        assert item.value == 0.7
        assert item.count == 100

    def test_from_dict(self):
        item = KeyValueCount.from_dict({"key": "k", "value": 0.7, "count": 100})

        assert item.key == "k"
        assert item.value == 0.7
        assert item.count == 100
