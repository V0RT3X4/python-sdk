"""Cargo Movements Endpoint."""
from datetime import datetime
from typing import List, Union

from vortexasdk.api.shared_types import to_ISODate
from vortexasdk.conversions import (
    convert_to_corporation_ids,
    convert_to_geography_ids,
    convert_to_product_ids,
    convert_to_vessel_ids,
)
from vortexasdk.endpoints.cargo_movements_result import CargoMovementsResult
from vortexasdk.endpoints.endpoints import CARGO_MOVEMENTS_RESOURCE
from vortexasdk.operations import Search


class CargoMovements(Search):
    """Cargo Movements Endpoint, use this to search through Vortexa's cargo movements."""

    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Search.__init__(self, CARGO_MOVEMENTS_RESOURCE)

    def search(
        self,
        filter_activity: str,
        filter_time_min: datetime = datetime(2019, 10, 1, 0),
        filter_time_max: datetime = datetime(2019, 10, 1, 1),
        cm_unit: str = "b",
        filter_charterers: Union[str, List[str]] = None,
        filter_destinations: Union[str, List[str]] = None,
        filter_origins: Union[str, List[str]] = None,
        filter_owners: Union[str, List[str]] = None,
        filter_products: Union[str, List[str]] = None,
        filter_vessels: Union[str, List[str]] = None,
        filter_storage_locations: Union[str, List[str]] = None,
        filter_ship_to_ship_locations: Union[str, List[str]] = None,
        filter_waypoints: Union[str, List[str]] = None,
        disable_geographic_exclusion_rules: bool = None,
    ) -> CargoMovementsResult:
        """

        Find CargoMovements matching the given search parameters.

        # Arguments
            filter_activity: Movement activity on which to base the time filter. Must be one of ['loading_state',
             'loading_start', 'loading_end', 'identified_for_loading_state', 'unloading_state', 'unloading_start',
              'unloading_end', 'unloaded_state', 'storing_state', 'storing_start', 'storing_end', 'transiting_state',
               'any_activity'].

            filter_time_min: The UTC start date of the time filter.

            filter_time_max: The UTC end date of the time filter.

            cm_unit: Unit of measurement. Enter 'b' for barrels or 't' for tonnes.

            filter_corporations: A corporation, or list of corporations to filter on.

            filter_destinations: A geography, or list of geographies to filter on. Both geography names or IDs can be entered here.

            filter_origins: A geography, or list of geographies to filter on. Both geography names or IDs can be entered here.

            filter_owners: An owner, or list of owners to filter on. Both charterer/owner names or IDs can be entered here.

            filter_products: A product, or list of products to filter on. Both product names or IDs can be entered here.

            filter_vessels: A vessel, or list of vessels to filter on. Vessel name, imo, mmsi, vessel class, or vessel IDs can be entered here,

            filter_storage_locations: A geography, or list of geography to filter on. Both geography names or IDs can be entered here.

            filter_ship_to_ship_locations: A geography, or list of geography to filter on. Both geography names or IDs can be entered here.

            filter_waypoints: A geography, or list of geography to filter on. Both geography names or IDs can be entered here.

            disable_geographic_exclusion_rules: This controls a popular industry term "intra-movements" and determines
             the filter behaviour for cargo leaving then entering the same geographic area.

        # Returns
        `CargoMovementsResult`, containing all the cargo movements matching the given search terms.


        # Example

        * _Which cargoes were loaded from Rotterdam on the morning of 1st December 2018?_


        ```python
        >>> from vortexasdk import CargoMovements
        >>> df = CargoMovements().search(
            filter_origins="Rotterdam",
            filter_activity='loading_state',
            filter_time_min=datetime(2018, 12, 1),
            filter_time_max=datetime(2018, 12, 1, 12),
        ).to_df(columns=['product.grade.label', 'product.group.label', 'vessels.0.vessel_class'])
        ```

        |    | product.group.label   | product.grade.label             | vessels.0.vessel_class   |
        |---:|:----------------------|:--------------------------------|:-------------------------|
        |  0 | Clean products        | Pygas                           | general_purpose          |
        |  1 | Clean products        | Chemicals                       | tiny_tanker              |
        |  2 | Clean products        | Chemicals                       | tiny_tanker              |
        |  3 | Dirty products        | Low Sulphur VGO (LSVGO)         | general_purpose          |
        |  4 | Clean products        | ULSD (Ultra Low Sulphur Diesel) | general_purpose          |
        |  5 | Clean products        | Chemicals                       | tiny_tanker              |
        |  6 | Clean products        | Finished Gasoline               | handymax                 |

        * _Which VLCC cargoes passed through the Suez canal en route to China?_

        Note here we include vessels.0..., vessels.1..., vessels.2... columns.
        This lets us view all vessels present in any STS operations.

        ```python
        >>> from vortexasdk import CargoMovements
        >>> cols = ['vessels.0.name', 'vessels.0.vessel_class', 'vessels.1.name', 'vessels.1.vessel_class',  'vessels.2.name', 'vessels.2.vessel_class', 'product.group.label', 'quantity']

        >>> df = CargoMovements().search(
            filter_destinations="China",
            filter_activity="loading_state",
            filter_waypoints="suez",
            filter_vessels="vlcc",
            filter_time_min=datetime(2016, 12, 01),
            filter_time_max=datetime(2018, 12, 01),
        ).to_df(columns=cols)
        ```

        |    | vessels.0.name   | vessels.0.vessel_class   | vessels.1.name   | vessels.1.vessel_class   | vessels.2.name   | vessels.2.vessel_class   | product.group.label   |   quantity |
        |---:|:-----------------|:-------------------------|:-----------------|:-------------------------|:-----------------|:-------------------------|:----------------------|-----------:|
        |  0 | MINERVA MARINA   | suezmax                  | COSGLORY LAKE    | vlcc_plus                | nan              | nan                      | Crude                 |     700614 |
        |  1 | BUKHA            | vlcc_plus                | nan              | nan                      | nan              | nan                      | Crude                 |    1896374 |
        |  2 | ATHENIAN FREEDOM | vlcc_plus                | nan              | nan                      | nan              | nan                      | Crude                 |     183537 |
        |  3 | ATINA            | suezmax                  | DONAT            | suezmax                  | DS VISION        | vlcc_plus                | Crude                 |     896773 |
        |  4 | MINERVA MARINA   | suezmax                  | COSGLORY LAKE    | vlcc_plus                | nan              | nan                      | Crude                 |     405724 |
        |  5 | MASAL            | suezmax                  | EKTA             | vlcc_plus                | nan              | nan                      | Crude                 |     997896 |
        |  6 | ATHENIAN FREEDOM | vlcc_plus                | nan              | nan                      | nan              | nan                      | Crude                 |     120812 |

        [Cargo Movements Endpoint Further Documentation](https://docs.vortexa.com/reference/POST/cargo-movements/search)

        """
        params = {
            "filter_activity": filter_activity,
            "filter_time_min": to_ISODate(filter_time_min),
            "filter_time_max": to_ISODate(filter_time_max),
            "cm_unit": cm_unit,
            "size": self._MAX_PAGE_RESULT_SIZE,
            "filter_charterers": convert_to_corporation_ids(filter_charterers),
            "filter_owners": convert_to_corporation_ids(filter_owners),
            "filter_products": convert_to_product_ids(filter_products),
            "filter_vessels": convert_to_vessel_ids(filter_vessels),
            "filter_destinations": convert_to_geography_ids(
                filter_destinations
            ),
            "filter_origins": convert_to_geography_ids(filter_origins),
            "filter_storage_locations": convert_to_geography_ids(
                filter_storage_locations
            ),
            "filter_ship_to_ship_locations": convert_to_geography_ids(
                filter_ship_to_ship_locations
            ),
            "filter_waypoints": convert_to_geography_ids(filter_waypoints),
            "disable_geographic_exclusion_rules": disable_geographic_exclusion_rules,
        }

        return CargoMovementsResult(super().search(**params))
