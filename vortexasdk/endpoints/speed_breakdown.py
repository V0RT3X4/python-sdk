"""Speed Breakdown Endpoint."""
from typing import List, Union
from datetime import datetime

from vortexasdk.api import ID
from vortexasdk.endpoints.timeseries_result import TimeSeriesResult
from vortexasdk.endpoints.endpoints import SPEED_BREAKDOWN
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list
from vortexasdk.api.shared_types import to_ISODate


class SpeedBreakdown(Search):
    """
    Speed Breakdown Endpoint. Used to retreive a vessel speed data as a time series. The aggregation is done
    on the Vessel Movements data hence similar parameters are accepted.

    A detailed explanation of the endpoint can be found [here](https://docs.vortexa.com/reference/speed-breakdown).
    """

    def __init__(self):
        Search.__init__(self, SPEED_BREAKDOWN)

    def search(
        self,
        breakdown_unit: str = "kn",
        breakdown_frequency: str = "day",
        filter_time_min: datetime = datetime(2019, 10, 1, 0),
        filter_time_max: datetime = datetime(2019, 10, 1, 1),
        filter_activity: str = None,
        filter_charterers: Union[ID, List[ID]] = None,
        filter_destinations: Union[ID, List[ID]] = None,
        filter_origins: Union[ID, List[ID]] = None,
        filter_owners: Union[ID, List[ID]] = None,
        filter_products: Union[ID, List[ID]] = None,
        filter_vessels: Union[ID, List[ID]] = None,
        filter_vessel_classes: Union[ID, List[ID]] = None,
        filter_vessel_status: str = None,
        filter_vessel_age_min: int = None,
        filter_vessel_age_max: int = None,
        filter_vessel_scrubbers: str = "disabled",
        filter_vessel_flags: Union[ID, List[ID]] = None,
        filter_vessel_ice_class: Union[ID, List[ID]] = None,
        filter_vessel_propulsion: Union[ID, List[ID]] = None,
        exclude_origins: Union[ID, List[ID]] = None,
        exclude_destinations: Union[ID, List[ID]] = None,
        exclude_products: Union[ID, List[ID]] = None,
        exclude_vessels: Union[ID, List[ID]] = None,
        exclude_vessel_classes: Union[ID, List[ID]] = None,
        exclude_charterers: Union[ID, List[ID]] = None,
        exclude_owners: Union[ID, List[ID]] = None,
        exclude_vessel_flags: Union[ID, List[ID]] = None,
        exclude_vessel_ice_class: Union[ID, List[ID]] = None,
        exclude_vessel_propulsion: Union[ID, List[ID]] = None,
    ) -> TimeSeriesResult:
        """
        Find VesselMovements matching the given search parameters.

        # Arguments
            breakdown_frequency: Must be one of: 'day', 'week', 'doe_week', 'month', 'quarter' or 'year'.

            filter_activity: Movement activity on which to base the time filter. Must be one of ['loading_state',
             'loading_start', 'loading_end', 'identified_for_loading_state', 'unloading_state', 'unloading_start',
              'unloading_end', 'unloaded_state', 'storing_state', 'storing_start', 'storing_end', 'transiting_state',
               'any_activity'].

            filter_time_min: The UTC start date of the time filter.

            filter_time_max: The UTC end date of the time filter.

            breakdown_unit: Unit of speed. Enter 'kn' for knots, 'kmh' for kilometers per hour or `mps` for meters per second.

            filter_charterers: A charterer ID, or list of charterer IDs to filter on.

            filter_destinations: A geography ID, or list of geography IDs to filter on.

            filter_origins: A geography ID, or list of geography IDs to filter on.

            filter_owners: An corporation ID, or list of corporation IDs to filter on.

            filter_products: A product ID, or list of product IDs to filter on.

            filter_vessels: A vessel ID, or list of vessel IDs to filter on.

            filter_vessel_classes: A vessel class, or list of vessel classes to filter on.

            filter_vessel_status: The vessel status on which to base the filter. Enter 'vessel_status_ballast' for ballast vessels, 'vessel_status_laden_known' for laden vessels with known cargo (i.e. a type of cargo that Vortexa currently tracks) or 'vessel_status_laden_unknown' for laden vessels with unknown cargo (i.e. a type of cargo that Vortexa currently does not track).

            filter_vessel_age_min: A number between 1 and 100 (representing years).

            filter_vessel_age_max: A number between 1 and 100 (representing years).

            filter_vessel_scrubbers: Either inactive 'disabled', or included 'inc' or excluded 'exc'.

            filter_vessel_flags: A geography ID, or list of geography IDs to filter on.

            filter_vessel_ice_class: An attribute ID, or list of attribute IDs to filter on.

            filter_vessel_propulsion: An attribute ID, or list of attribute IDs to filter on.

            exclude_origins: A geography ID, or list of geography IDs to exclude.

            exclude_destinations: A geography ID, or list of geography IDs to exclude.

            exclude_products: A product ID, or list of product IDs to exclude.

            exclude_vessels: A vessel ID, or list of vessel IDs to exclude.

            exclude_vessel_classes: A vessel class, or list of vessel classes to exclude.

            exclude_charterers: A charterer ID, or list of charterer IDs to exclude.

            exclude_owners: An owner ID, or list of owner IDs to exclude.

            exclude_vessel_flags: A geography ID, or list of geography IDs to exclude.

            exclude_vessel_ice_class: An attribute ID, or list of attribute IDs to exclude.

            exclude_vessel_propulsion: An attribute ID, or list of attribute IDs to exclude.


        # Returns
        `TimeSeriesResult`

        # Example

        ```python
        >>> from vortexasdk import SpeedBreakdown, Vessels
        >>> new_wisdom = [g.id for g in Vessels().search("NEW WISDOM").to_list()]
        >>> search_result = SpeedBreakdown().search(
        ...    breakdown_unit='kn',
        ...    timeseries_frequency='month',
        ...    filter_vessels=new_wisdom,
        ...    filter_time_min=datetime(2018, 1, 1),
        ...    filter_time_max=datetime(2019, 1, 1))
        >>> df = search_result.to_df()

        ```

        | key           | value              | count |
        | ------------- | ------------------ | ----- |
        | 1509494400000 | 9.323186874389648  | 4     |
        | 1512086400000 | 9.323186874389648  | 31    |
        | 1514764800000 | 8.995147749781609  | 36    |
        | 1517443200000 | 8.874555279226865  | 34    |
        | 1519862400000 | 8.54799539902631   | 34    |
        | 1522540800000 | 11.498196601867676 | 30    |
        | 1525132800000 | 5.749098300933838  | 50    |
        | 1527811200000 | 8.993220090866089  | 36    |
        | 1530403200000 | 9.472143958596622  | 34    |
        | 1533081600000 | 7.8755770010106705 | 34    |
        | 1535760000000 | 9.082356016976492  | 35    |
        | 1538352000000 | 10.909105974085191 | 34    |
        | 1541030400000 | 9.645510704286638  | 31    |
        | 1543622400000 | 8.24781712363748   | 34    |
        | 1546300800000 | 7.937682151794434  | 15    |

        [Ton Miles Breakdown Further Documentation](https://docs.vortexa.com/reference/speed-breakdown)
        """

        exclude_params = {
            "filter_origins": convert_to_list(exclude_origins),
            "filter_destinations": convert_to_list(exclude_destinations),
            "filter_products": convert_to_list(exclude_products),
            "filter_vessels": convert_to_list(exclude_vessels),
            "filter_vessel_classes": convert_to_list(exclude_vessel_classes),
            "filter_charterers": convert_to_list(exclude_charterers),
            "filter_owners": convert_to_list(exclude_owners),
            "filter_vessel_flags": convert_to_list(exclude_vessel_flags),
            "filter_vessel_ice_class": convert_to_list(
                exclude_vessel_ice_class
            ),
            "filter_vessel_propulsion": convert_to_list(
                exclude_vessel_propulsion
            ),
        }

        api_params = {
            "breakdown_frequency": breakdown_frequency,
            "filter_activity": filter_activity,
            "filter_time_min": to_ISODate(filter_time_min),
            "filter_time_max": to_ISODate(filter_time_max),
            "breakdown_unit": breakdown_unit,
            "filter_charterers": convert_to_list(filter_charterers),
            "filter_owners": convert_to_list(filter_owners),
            "filter_destinations": convert_to_list(filter_destinations),
            "filter_origins": convert_to_list(filter_origins),
            "filter_products": convert_to_list(filter_products),
            "filter_vessels": convert_to_list(filter_vessels),
            "filter_vessel_classes": convert_to_list(filter_vessel_classes),
            "filter_vessel_status": filter_vessel_status,
            "filter_vessel_age_min": filter_vessel_age_min,
            "filter_vessel_age_max": filter_vessel_age_max,
            "filter_vessel_scrubbers": filter_vessel_scrubbers,
            "filter_vessel_flags": convert_to_list(filter_vessel_flags),
            "filter_vessel_ice_class": convert_to_list(
                filter_vessel_ice_class
            ),
            "filter_vessel_propulsion": convert_to_list(
                filter_vessel_propulsion
            ),
            "exclude": exclude_params,
        }

        return TimeSeriesResult(super().search(**api_params))
