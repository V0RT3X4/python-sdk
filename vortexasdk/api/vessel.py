from dataclasses import dataclass
from typing import List, Optional

from vortexasdk.api.corporation import CorporateEntity
from vortexasdk.api.id import ID
from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.api.shared_types import IDName, ISODate, Node, Tag


@dataclass(frozen=True,)
class Vessel(Node, FromDictMixin):
    """
    Represent a Vessel reference record returned by the API.

    [Vessels Further Documentation](https://docs.vortexa.com/reference/GET/reference/vessels/%7Bid%7D)
    """

    related_names: List[str]
    mmsi: int

    tags: List[Tag]
    current_product_type: List

    vessel_class: str

    dead_weight: Optional[int] = None
    cubic_capacity: Optional[int] = None
    to_bow: Optional[str] = None
    to_stern: Optional[str] = None
    to_port: Optional[str] = None
    to_starboard: Optional[str] = None
    call_sign: Optional[str] = None
    year: Optional[int] = None
    imo: Optional[int] = None
    gross_tonnage: Optional[int] = None


@dataclass(frozen=True)
class VesselEntity(IDName):
    """
    A VesselEntity represents a vessel record used in CargoMovements and VesselMovements.

    [Vessel Entities Further Documentation](https://docs.vortexa.com/reference/intro-vessel-entities)
    """

    id: ID
    name: str
    mmsi: int
    imo: Optional[int]

    dwt: int

    vessel_class: str
    corporate_entities: List[CorporateEntity]
    tags: List[Tag]
    status: str

    start_timestamp: Optional[ISODate] = None

    cubic_capacity: Optional[int] = None
    voyage_id: Optional[str] = None
    fixture_fulfilled: Optional[bool] = None
    end_timestamp: Optional[ISODate] = None
    fixture_id: Optional[str] = None
