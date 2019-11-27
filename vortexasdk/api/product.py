from dataclasses import dataclass
from typing import List

from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.api.shared_types import Node, EntityWithProbability


@dataclass(frozen=True)
class Product(Node, FromDictMixin):
    """
    Represent a Product reference record returned by the API.

    [Product Further Documentation](https://docs.vortexa.com/reference/GET/reference/products/%7Bid%7D)
    """

    layer: List[str]
    meta: dict


@dataclass(frozen=True)
class ProductEntity(EntityWithProbability):
    """

    Represents a single product layer of a hierarchical product tree.

    [Further Documentation](https://docs.vortexa.com/reference/intro-product-entities)
    """
