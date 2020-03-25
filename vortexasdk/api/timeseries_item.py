from dataclasses import dataclass

from vortexasdk.api.serdes import FromDictMixin


@dataclass(frozen=True)
class KeyValueCount(FromDictMixin):
    """
    Generic container class holding a _key_, _value_ pair, and a _count_ of records contributing to the given value.

    For example, this class could hold the total tonnage exported (value) on 2019-01-01 (key), and the count of cargo
    movements contributing to this tonnage aggregate, ie the number of cargo movements on this day (count).
    """

    key: str
    value: float
    count: int
