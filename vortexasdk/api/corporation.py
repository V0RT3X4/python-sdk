from dataclasses import dataclass
from typing import List

from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.api.shared_types import IDName, EntityWithProbability


@dataclass(frozen=True)
class Corporation(IDName, FromDictMixin):
    """Represent a Corporation reference record returned by the API."""

    corporate_entity_type: List[str]
    ref_type: str
    leaf: bool
    parent: List[str]


@dataclass(frozen=True)
class CorporateEntity(EntityWithProbability):
    """
    Represents a relationship between a corporation and another entity like a vessel.

    [Corporate Entity Further Documentation](https://docs.vortexa.com/reference/intro-corporate-entities)


    """
