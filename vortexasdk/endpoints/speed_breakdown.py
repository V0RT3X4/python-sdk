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
    """Speed Breakdown Endpoint."""

    def __init__(self):
        Search.__init__(self, SPEED_BREAKDOWN)

    def search(
        self,
        # check which one to use
        breakdown_unit: str = "b",
        unit: str = "b",
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
        comment
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
            # check which one to use
            "breakdown_unit": unit,
            "unit": unit,
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
