from typing import List, Dict

import jsons

from vortexasdk.api import ID
from vortexasdk.abstract_client import AbstractVortexaClient
from vortexasdk.endpoints.endpoints import (
    CORPORATIONS_REFERENCE,
    VESSELS_REFERENCE,
    PRODUCTS_REFERENCE,
    VESSEL_MOVEMENTS_RESOURCE,
)


def _read(example_file) -> List[Dict]:
    with open(f"tests/api/examples/{example_file}", "r") as f:
        return jsons.loads(f.read(), List)


example_corporations: List[Dict] = _read("corporations.json")
example_vessels: List[Dict] = _read("vessels.json")
example_products: List[Dict] = _read("products.json")
example_vessel_movements: List[Dict] = _read("vessel_movements.json")
example_cargo_movements: List[Dict] = _read("vessel_movements.json")


class MockVortexaClient(AbstractVortexaClient):
    _results = {
        CORPORATIONS_REFERENCE: example_corporations,
        VESSELS_REFERENCE: example_vessels,
        PRODUCTS_REFERENCE: example_products,
        VESSEL_MOVEMENTS_RESOURCE: example_vessel_movements,
    }

    def get_reference(self, resource: str, id: ID) -> str:
        return ""

    def search(self, resource: str, **data) -> List:
        return MockVortexaClient._results[resource]
