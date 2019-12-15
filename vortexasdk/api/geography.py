from dataclasses import dataclass
from typing import List, Optional, Tuple

from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.api.shared_types import (
    EntityWithProbability,
    ID,
    IDLayer,
    IDNameLayer,
    Node,
)

Position = Tuple[float, float]


@dataclass(frozen=True)
class BoundingBox:
    """Polygon with list of bounding lon lat coords."""

    type: str
    coordinates: List[Position]


@dataclass(frozen=True)
class Geography(Node, FromDictMixin):
    """Represent a Geography reference record returned by the API."""

    id: ID
    name: str
    layer: List[str]
    exclusion_rule: List[IDNameLayer]
    hierarchy: List[IDLayer]
    bounding_box: Optional[BoundingBox]
    centre_point: Optional[Position]
    location: Optional[Position]


@dataclass(frozen=True)
class GeographyEntity(EntityWithProbability):
    """
    Represents a hierarchy tree of locational data.

    [Geography Entities Further Documentation](https://docs.vortexa.com/reference/intro-geography-entries)

    """
