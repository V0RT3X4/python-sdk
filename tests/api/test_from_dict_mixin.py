from dataclasses import dataclass
from unittest import TestCase

from vortexasdk.api.serdes import FromDictMixin


@dataclass
class Foo(FromDictMixin):
    bar: int


class TestFromDictMixin(TestCase):
    def test_from_dict(self):
        d = {"bar": 1}

        actual = Foo.from_dict(d)

        expected = Foo(1)

        assert actual == expected
