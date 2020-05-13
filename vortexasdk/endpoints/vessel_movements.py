"""Vessel Movements Endpoint."""
from datetime import datetime
from typing import List, Union

from vortexasdk.api.shared_types import to_ISODate
from vortexasdk.endpoints.endpoints import VESSEL_MOVEMENTS_RESOURCE
from vortexasdk.endpoints.vessel_movements_result import VesselMovementsResult
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list

logger = get_logger(__name__)


class VesselMovements(Search):
    """
    Vessel Movements Endpoint, use this to search through Vortexa's VesselMovements.

    A VesselMovement represents a single vessel moving between two locations.

    * The vessel may carry one cargo, many cargoes (coloads), or zero cargos (ballast).
    * The start and end locations for a VesselMovement may be on land (loadings and discharges), they may be STS Zones
    (STS events), or they may be Floating Storage.

    A detailed explanation of Cargo/Vessel Movements can be found [here](https://docs.vortexa.com/reference/intro-movement-difference).
    """

    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Search.__init__(self, VESSEL_MOVEMENTS_RESOURCE)

    def search(
        self,
        filter_time_min: datetime = datetime(2019, 10, 1, 0),
        filter_time_max: datetime = datetime(2019, 10, 1, 1),
        unit: str = "b",
        filter_activity: str = None,
        filter_charterers: Union[str, List[str]] = None,
        filter_destinations: Union[str, List[str]] = None,
        filter_origins: Union[str, List[str]] = None,
        filter_owners: Union[str, List[str]] = None,
        filter_products: Union[str, List[str]] = None,
        filter_vessels: Union[str, List[str]] = None,
        filter_vessel_classes: Union[str, List[str]] = None,
        filter_vessel_status: Union[str, List[str]] = None,
        exclude_origins: Union[str, List[str]] = None,
        exclude_destinations: Union[str, List[str]] = None,
        exclude_products: Union[str, List[str]] = None,
        exclude_vessels: Union[str, List[str]] = None,
        exclude_vessel_classes: Union[str, List[str]] = None,
        exclude_charterers: Union[str, List[str]] = None,
        exclude_owners: Union[str, List[str]] = None,
    ) -> VesselMovementsResult:
        """
        Find VesselMovements matching the given search parameters.

        # Arguments
            filter_activity: Movement activity on which to base the time filter. Must be one of ['loading_state',
             'loading_start', 'loading_end', 'identified_for_loading_state', 'unloading_state', 'unloading_start',
              'unloading_end', 'unloaded_state', 'storing_state', 'storing_start', 'storing_end', 'transiting_state',
               'any_activity'].

            filter_time_min: The UTC start date of the time filter.

            filter_time_max: The UTC end date of the time filter.

            unit: Unit of measurement. Enter 'b' for barrels or 't' for tonnes.

            filter_charterers: A charterer ID, or list of charterer IDs to filter on.

            filter_destinations: A geography ID, or list of geography IDs to filter on.

            filter_origins: A geography ID, or list of geography IDs to filter on.

            filter_owners: An corporation ID, or list of corporation IDs to filter on.

            filter_products: A product ID, or list of product IDs to filter on.

            filter_vessels: A vessel ID, or list of vessel IDs to filter on.

            filter_vessel_classes: A vessel class, or list of vessel classes to filter on.

            filter_vessel_status: The vessel status on which to base the filter. Enter 'vessel_status_ballast' for ballast vessels, 'vessel_status_laden_known' for laden vessels with known cargo (i.e. a type of cargo that Vortexa currently tracks) or 'vessel_status_laden_unknown' for laden vessels with unknown cargo (i.e. a type of cargo that Vortexa currently does not track).

            exclude_origins: A geography ID, or list of geography IDs to exclude.

            exclude_destinations: A geography ID, or list of geography IDs to exclude.

            exclude_products: A product ID, or list of product IDs to exclude.

            exclude_vessels: A vessel ID, or list of vessel IDs to exclude.

            exclude_vessel_classes: A vessel class, or list of vessel classes to exclude.

            exclude_charterers: A charterer ID, or list of charterer IDs to exclude.

            exclude_owners: An owner ID, or list of owner IDs to exclude.


        # Returns
        `VesselMovementsResult`, containing all the vessel movements matching the given search terms.


        # Example
        Let's search for all vessels that departed from `Rotterdam [NL]` on the morning of 1st December 2018.

        ```python
        >>> from vortexasdk import VesselMovements, Geographies
        >>> rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]
        >>> df = VesselMovements().search(
        ...        filter_time_min=datetime(2017, 10, 1, 0, 0),
        ...        filter_time_max=datetime(2017, 10, 1, 0, 10),
        ...        filter_origins=rotterdam
        ... ).to_df().head(2)

        ```

        |    | start_timestamp          | end_timestamp            |   vessel.imo | vessel.name   | vessel.vessel_class   | origin.location.country.label   | origin.location.port.label   | destination.location.country.label   | destination.location.port.label   |   cargoes.0.quantity | cargoes.0.product.grade.label   |
        |---:|:-------------------------|:-------------------------|-------------:|:--------------|:----------------------|:--------------------------------|:-----------------------------|:-------------------------------------|:----------------------------------|---------------------:|:--------------------------------|
        |  0 | 2017-09-30T15:30:27+0000 | 2017-10-03T01:46:06+0000 |  9.21091e+06 | ADEBOMI 3     | handysize             | Netherlands                     | Rotterdam [NL]               | Netherlands                          | Rotterdam [NL]                    |                  nan | nan                             |
        |  1 | 2017-08-29T14:51:32+0000 | 2017-10-04T14:46:21+0000 |  9.64544e+06 | AEGEAN VISION | suezmax               | Netherlands                     | Rotterdam [NL]               | Singapore                            | Singapore [SG]                    |               852261 | High Sulphur                    |

        [Vessel Movements Endpoint Further Documentation](https://docs.vortexa.com/reference/POST/vessel-movements/search)

        """
        exclude_params = {
            "filter_origins": convert_to_list(exclude_origins),
            "filter_destinations": convert_to_list(exclude_destinations),
            "filter_products": convert_to_list(exclude_products),
            "filter_vessels": convert_to_list(exclude_vessels),
            "filter_vessel_classes": convert_to_list(exclude_vessel_classes),
            "filter_charterers": convert_to_list(exclude_charterers),
            "filter_owners": convert_to_list(exclude_owners),
        }

        params = {
            "filter_activity": filter_activity,
            "filter_time_min": to_ISODate(filter_time_min),
            "filter_time_max": to_ISODate(filter_time_max),
            "unit": unit,
            "filter_charterers": convert_to_list(filter_charterers),
            "filter_owners": convert_to_list(filter_owners),
            "filter_destinations": convert_to_list(filter_destinations),
            "filter_origins": convert_to_list(filter_origins),
            "filter_products": convert_to_list(filter_products),
            "filter_vessels": convert_to_list(filter_vessels),
            "filter_vessel_classes": convert_to_list(filter_vessel_classes),
            "filter_vessel_status": convert_to_list(filter_vessel_status),
            "exclude": exclude_params,
            "size": self._MAX_PAGE_RESULT_SIZE,
        }

        return VesselMovementsResult(super().search(**params))
