from typing import List

from vortexasdk.api.id import ID
from vortexasdk.client import default_client
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class Reference:
    """Lookup Vortexa Reference Data using an entity ID."""

    def __init__(self, resource):
        """
        Init.

        # Arguments
            resource: The vortexa endpoint used for reference lookups.

        """
        self._resource = resource

    def reference(self, id: ID):
        """
        Lookup reference data using ID.

        # Arguments
            id: ID of the entity we're looking up

        # Returns
        An entity matching the ID

        # Examples

            >>> Reference("/reference/geographies").reference(id='cfb8c4ef76585c3a37792b643791a0f4ff6d5656d5508927d8017319e21f2fca')

        """
        logger.info(
            f"Looking up {self.__class__.__name__} reference data with id: {id}"
        )
        return default_client().get_reference(self._resource, id)


class Search:
    """Search Vortexa Reference Data."""

    def __init__(self, resource):
        """
        Init.

        # Arguments
            resource: Appropriate search resource

        """
        self._resource = resource

    def search(self, **params) -> List[dict]:
        """
        Search Reference data filtering on `params`.

        # Arguments
            params: Search parameters

        # Returns
        Result of VortexaAPI call from hitting querying the `resource` endpoint filtering with `params`.

        # Examples

            >>> Search("/reference/vessels").search(term="DHT")

        """
        logger.info(
            f"Searching {self.__class__.__name__} with params: {params}"
        )
        return default_client().search(self._resource, **params)
