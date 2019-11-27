"""Vessel Movements Endpoint."""
from typing import List, Union

from vortexasdk.conversions import (
    convert_to_corporation_ids,
    convert_to_geography_ids,
    convert_to_product_ids,
    convert_to_vessel_ids,
)
from vortexasdk.endpoints.endpoints import VESSEL_MOVEMENTS_RESOURCE
from vortexasdk.endpoints.vessel_movements_result import VesselMovementsResult
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list


class VesselMovements(Search):
    """
    Vessel Movements Endpoint, use this to search through Vortexa's VesselMovements.

    A VesselMovement represents a single vessel moving between two locations.

    * The vessel may carry one cargo, many cargoes (coloads), or zero cargos (ballast).
    * The start and end locations for a VesselMovement may be on land (loadings and discharges), they may be STS Zones
    (STS events), or they may be Floating Storage.
    """

    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Search.__init__(self, VESSEL_MOVEMENTS_RESOURCE)

    def search(
        self,
        filter_time_min: str = "2019-10-01T00:00:00.000Z",
        filter_time_max: str = "2019-10-01T01:00:00.000Z",
        unit: str = "b",
        filter_charterers: Union[str, List[str]] = None,
        filter_destinations: Union[str, List[str]] = None,
        filter_origins: Union[str, List[str]] = None,
        filter_owners: Union[str, List[str]] = None,
        filter_products: Union[str, List[str]] = None,
        filter_vessels: Union[str, List[str]] = None,
        filter_vessel_classes: Union[str, List[str]] = None,
    ) -> VesselMovementsResult:
        """
        Find VesselMovements matching the given search parameters.

        # Arguments
            filter_time_min: The start date of the time filter.

            filter_time_max: The end date of the time filter.

            unit: Unit of measurement. Enter 'b' for barrels or 't' for tonnes.

            filter_corporations: A corporation, or list of corporations to filter on.

            filter_destinations: A geography, or list of geographies to filter on. Both geography names or IDs can be entered here.

            filter_origins: A geography, or list of geographies to filter on. Both geography names or IDs can be entered here.

            filter_owners: An owner, or list of owners to filter on. Both charterer/owner names or IDs can be entered here.

            filter_products: A product, or list of products to filter on. Both product names or IDs can be entered here.

            filter_vessels: A vessel, or list of vessels to filter on. Both vessel names or IDs can be entered here,

            filter_vessel_classes: A vessel class, or list of vessel classes to filter on. Both vessel names or IDs can be entered here,

        # Returns
        `VesselMovementsResult`, containing all the vessel movements matching the given search terms.


        # Example
        Let's search for all vessels that departed from `Rotterdam [NL]` on the morning of 1st December 2018.

        ```python
        >>> from vortexasdk import VesselMovements
        >>> df = VesselMovements().search(
            filter_time_min="2017-10-01T00:00:00.000Z",
            filter_time_max="2017-10-01T00:10:00.000Z",
            filter_origins='rotterdam'
        ).to_df().head(2)
        ```

        |    | start_timestamp          | end_timestamp            |   vessel.imo | vessel.name   | vessel.vessel_class   | origin.location.country.label   | origin.location.port.label   | destination.location.country.label   | destination.location.port.label   |   cargoes.0.quantity | cargoes.0.product.grade.label   |
        |---:|:-------------------------|:-------------------------|-------------:|:--------------|:----------------------|:--------------------------------|:-----------------------------|:-------------------------------------|:----------------------------------|---------------------:|:--------------------------------|
        |  0 | 2017-09-30T15:30:27+0000 | 2017-10-03T01:46:06+0000 |  9.21091e+06 | ADEBOMI 3     | handysize             | Netherlands                     | Rotterdam [NL]               | Netherlands                          | Rotterdam [NL]                    |                  nan | nan                             |
        |  1 | 2017-08-29T14:51:32+0000 | 2017-10-04T14:46:21+0000 |  9.64544e+06 | AEGEAN VISION | suezmax               | Netherlands                     | Rotterdam [NL]               | Singapore                            | Singapore [SG]                    |               852261 | High Sulphur                    |

        [Vessel Movements Endpoint Further Documentation](https://docs.vortexa.com/reference/POST/vessel-movements/search)

        """
        params = {
            # Compulsory search parameters
            "filter_time_min": filter_time_min,
            "filter_time_max": filter_time_max,
            "unit": unit,
            "size": self._MAX_PAGE_RESULT_SIZE,
            "filter_charterers": convert_to_corporation_ids(filter_charterers),
            "filter_owners": convert_to_corporation_ids(filter_owners),
            "filter_destinations": convert_to_geography_ids(
                filter_destinations
            ),
            "filter_origins": convert_to_geography_ids(filter_origins),
            "filter_products": convert_to_product_ids(filter_products),
            "filter_vessels": convert_to_vessel_ids(
                convert_to_list(filter_vessels)
            ),
            "filter_vessel_classes": convert_to_list(filter_vessel_classes),
        }

        return VesselMovementsResult(super().search(**params))
