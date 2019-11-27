from unittest import TestCase

from vortexasdk.api.id import is_valid_id, split_ids_other


class TestID(TestCase):
    def test_is_id_recognises_id(self):
        assert is_valid_id(
            "2aaad41b89dfad19e5668918018ae02695d7710bcbe5f2dc689234e8da492de3"
        )

    def test_is_id_recognised_wrong_length_id(self):
        double_length_id = (
            "2aaad41b89dfad19e5668918018ae02695d7710bcbe5f2dc689234e8da492de3"
            + "2aaad41b89dfad19e5668918018ae02695d7710bcbe5f2dc689234e8da492de3"
        )
        assert not is_valid_id(double_length_id)

    def test_is_id_recognises_non_id(self):
        assert not is_valid_id("United Kingdom")

    def test_separate_ids_from_names(self):
        mix = [
            "2aaad41b89dfad19e5668918018ae02695d7710bcbe5f2dc689234e8da492de3",
            "China",
            "Southamton",
            "918018ae02695d7710bcbe5f2dc689234e8da492de32aaad41b89dfad19e5668",
        ]

        ids, names = split_ids_other(mix)

        assert ids == [
            "2aaad41b89dfad19e5668918018ae02695d7710bcbe5f2dc689234e8da492de3",
            "918018ae02695d7710bcbe5f2dc689234e8da492de32aaad41b89dfad19e5668",
        ]

        assert names == ["China", "Southamton"]
