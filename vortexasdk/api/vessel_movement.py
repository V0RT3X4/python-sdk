from dataclasses import dataclass
from typing import List, Optional

from vortexasdk.api.geography import GeographyEntity
from vortexasdk.api.id import ID
from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.api.shared_types import ISODate
from vortexasdk.api.vessel import VesselEntity


@dataclass(frozen=True)
class VesselEvent:
    """Represent an event that occurred to a vessel during a vessel movement."""

    event_type: str
    location: List[GeographyEntity]
    pos: Optional[List[float]] = None

    event_id: Optional[ID] = None
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None


@dataclass(frozen=True)
class VesselMovement(FromDictMixin):
    """
    What is a vessel movement. TODO.

    [Vessel Movement Further Documentation](https://docs.vortexa.com/reference/intro-vessel-movement)

    """

    vessel_movement_id: ID
    voyage_id: ID
    vessel: VesselEntity

    origin: VesselEvent
    destination: VesselEvent
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None
