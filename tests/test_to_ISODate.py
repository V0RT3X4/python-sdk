from datetime import datetime
from unittest import TestCase

from vortexasdk.api.shared_types import to_ISODate


class TestToISODate(TestCase):
    def test_to_ISODate(self):
        assert to_ISODate(datetime(2018, 12, 31)) == "2018-12-31T00:00:00.000Z"

    def test_to_ISODate_with_time(self):
        assert (
            to_ISODate(datetime(2018, 12, 31, 23, 59, 59, 123456))
            == "2018-12-31T23:59:59.123Z"
        )
