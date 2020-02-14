from dataclasses import dataclass
from typing import List, Optional, Union

import numpy as np

from vortexasdk.api.geography import GeographyEntity
from vortexasdk.api.product import ProductEntity
from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.api.shared_types import ISODate
from vortexasdk.api.id import ID
from vortexasdk.api.vessel import VesselEntity


@dataclass(frozen=True)
class CargoEvent:
    """

    A CargoEvent represents an event that occurred to a cargo during a cargo movement.

    [Cargo Event Entities Further Documentation](https://docs.vortexa.com/reference/intro-cargo-events)

    """

    event_type: str
    location: List[GeographyEntity]

    probability: Union[Optional[float], Optional[int]] = None
    pos: Optional[List[float]] = None
    vessel_id: Optional[str] = None
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None


@dataclass(frozen=True)
class CargoMovement(FromDictMixin):
    """

    Cargo movements are the base data set the Vortexa API is centred around.

    Each movement represents a journey of a certain quantity of a product between places.

    [Cargo Movement Further Documentation](https://docs.vortexa.com/reference/intro-cargo-movement)

    """

    cargo_movement_id: ID
    quantity: int
    status: str
    vessels: List[VesselEntity]
    product: List[ProductEntity]
    events: List[CargoEvent]


@dataclass(frozen=True)
class CargoMovementSummary:
    cargo_movement_id: ID
    quantity: int
    status: str

    vessel: VesselEntity
    vessel_owner: Optional[str] = None
    charterer: Optional[str] = None
    time_charterer: Optional[str] = None
    product: Optional[str] = None
    grade: Optional[str] = None

    origin: Optional[GeographyEntity] = None
    destination: Optional[GeographyEntity] = None

    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None


def find_primary_vessel(cm: CargoMovement) -> VesselEntity:
    pass

def find_

def create_summary(cm: CargoMovement) -> CargoMovementSummary:

    primary_vessel = find_primary_vessel(cm)

    [e for e in primary_vessel.corporate_entities if e.layer == 'commercial_owner']


    return CargoMovementSummary(
        cargo_movement_id=cm.cargo_movement_id,
        quantity=cm.quantity,
        status=cm.status,
        vessel=primary_vessel,

    )
