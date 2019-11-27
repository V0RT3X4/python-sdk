import functools
import os
from multiprocessing.pool import Pool
from typing import List

import pandas as pd

from vortexasdk.api import VesselMovement
from vortexasdk.api.entity_flattening import (
    convert_vessel_movement_to_flat_dict,
)
from vortexasdk.api.search_result import Result


class VesselMovementsResult(Result):
    """
    Container class holdings search results returns from the vessel movements endpoint.

    This class has two methods, `to_list()`, and `to_df()`, allowing search results to be represented as a list of `VesselMovement`s,
     or as a `pd.DataFrame` , respectively.
    """

    def to_list(self) -> List[VesselMovement]:
        """Represent vessel movements as a list of `VesselMovementEntity`s."""
        list_of_dicts = super().to_list()

        with Pool(os.cpu_count()) as pool:
            return list(pool.map(VesselMovement.from_dict, list_of_dicts))

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent vessel movements as a `pd.DataFrame`.

        # Arguments
            columns: Output columns present in the `pd.DataFrame`.
            Enter `columns='all'` to return all available columns.
            Enter `columns=None` to use `vessel_movements.DEFAULT_COLUMNS`.

        # Returns
        `pd.DataFrame`, one row per `VesselMovement`.


        ## Notes


        By default, the columns returned are something along the lines of.
        ```python
        DEFAULT_COLUMNS = [
            'vessel.imo',
            'vessel.name',
            'vessel.vessel_class',
            'origin.event_type',
            'origin.location.port.label',
            'origin.location.country.label',
            'destination.event_type',
            'destination.location.port.label',
            'destination.location.country.label',
            'cargoes.0.product.group_product.label,'
            'cargoes.0.product.category.label',
            'cargoes.0.product.grade.label',
            'cargoes.0.quantity',
            'start_timestamp',
            'end_timestamp',
        ]
        ```
        The exact default columns used can be found at `vessel_movements.DEFAULT_COLUMNS`

        A near complete list of columns is given below
        ```
        [
            cargoes.0.cargo_movement_id,
            cargoes.0.product.category.id,
            cargoes.0.product.category.label,
            cargoes.0.product.category.layer,
            cargoes.0.product.category.probability,
            cargoes.0.product.category.source,
            cargoes.0.product.grade.id,
            cargoes.0.product.grade.label,
            cargoes.0.product.grade.layer,
            cargoes.0.product.grade.probability,
            cargoes.0.product.grade.source,
            cargoes.0.product.group.id,
            cargoes.0.product.group.label,
            cargoes.0.product.group.layer,
            cargoes.0.product.group.probability,
            cargoes.0.product.group.source,
            cargoes.0.product.group_product.id,
            cargoes.0.product.group_product.label,
            cargoes.0.product.group_product.layer,
            cargoes.0.product.group_product.probability,
            cargoes.0.product.group_product.source,
            cargoes.0.quantity,
            cargoes.1.cargo_movement_id,
            cargoes.1.product.category.id,
            cargoes.1.product.category.label,
            cargoes.1.product.category.layer,
            cargoes.1.product.category.probability,
            cargoes.1.product.category.source,
            cargoes.1.product.grade.id,
            cargoes.1.product.grade.label,
            cargoes.1.product.grade.layer,
            cargoes.1.product.grade.probability,
            cargoes.1.product.grade.source,
            cargoes.1.product.group.id,
            cargoes.1.product.group.label,
            cargoes.1.product.group.layer,
            cargoes.1.product.group.probability,
            cargoes.1.product.group.source,
            cargoes.1.product.group_product.id,
            cargoes.1.product.group_product.label,
            cargoes.1.product.group_product.layer,
            cargoes.1.product.group_product.probability,
            cargoes.1.product.group_product.source,
            cargoes.1.quantity,
            cargoes.2.cargo_movement_id,
            cargoes.2.product.category.id,
            cargoes.2.product.category.label,
            cargoes.2.product.category.layer,
            cargoes.2.product.category.probability,
            cargoes.2.product.category.source,
            cargoes.2.product.grade.id,
            cargoes.2.product.grade.label,
            cargoes.2.product.grade.layer,
            cargoes.2.product.grade.probability,
            cargoes.2.product.grade.source,
            cargoes.2.product.group.id,
            cargoes.2.product.group.label,
            cargoes.2.product.group.layer,
            cargoes.2.product.group.probability,
            cargoes.2.product.group.source,
            cargoes.2.product.group_product.id,
            cargoes.2.product.group_product.label,
            cargoes.2.product.group_product.layer,
            cargoes.2.product.group_product.probability,
            cargoes.2.product.group_product.source,
            cargoes.2.quantity,
            cargoes.3.cargo_movement_id,
            cargoes.3.product.category.id,
            cargoes.3.product.category.label,
            cargoes.3.product.category.layer,
            cargoes.3.product.category.probability,
            cargoes.3.product.category.source,
            cargoes.3.product.grade.id,
            cargoes.3.product.grade.label,
            cargoes.3.product.grade.layer,
            cargoes.3.product.grade.probability,
            cargoes.3.product.grade.source,
            cargoes.3.product.group.id,
            cargoes.3.product.group.label,
            cargoes.3.product.group.layer,
            cargoes.3.product.group.probability,
            cargoes.3.product.group.source,
            cargoes.3.product.group_product.id,
            cargoes.3.product.group_product.label,
            cargoes.3.product.group_product.layer,
            cargoes.3.product.group_product.probability,
            cargoes.3.product.group_product.source,
            cargoes.3.quantity,
            cargoes.4.cargo_movement_id,
            cargoes.4.product.grade.id,
            cargoes.4.product.grade.label,
            cargoes.4.product.grade.layer,
            cargoes.4.product.grade.probability,
            cargoes.4.product.grade.source,
            cargoes.4.product.group.id,
            cargoes.4.product.group.label,
            cargoes.4.product.group.layer,
            cargoes.4.product.group.probability,
            cargoes.4.product.group.source,
            cargoes.4.product.group_product.id,
            cargoes.4.product.group_product.label,
            cargoes.4.product.group_product.layer,
            cargoes.4.product.group_product.probability,
            cargoes.4.product.group_product.source,
            cargoes.4.quantity,
            destination.end_timestamp,
            destination.event_id,
            destination.event_type,
            destination.from_vessel.id,
            destination.from_vessel.label,
            destination.location.country.id,
            destination.location.country.label,
            destination.location.country.layer,
            destination.location.country.probability,
            destination.location.country.source,
            destination.location.port.id,
            destination.location.port.label,
            destination.location.port.layer,
            destination.location.port.probability,
            destination.location.port.source,
            destination.location.region.id,
            destination.location.region.label,
            destination.location.region.layer,
            destination.location.region.probability,
            destination.location.region.source,
            destination.location.shipping_region.id,
            destination.location.shipping_region.label,
            destination.location.shipping_region.layer,
            destination.location.shipping_region.probability,
            destination.location.shipping_region.source,
            destination.location.sts_zone.id,
            destination.location.sts_zone.label,
            destination.location.sts_zone.layer,
            destination.location.sts_zone.probability,
            destination.location.sts_zone.source,
            destination.location.terminal.id,
            destination.location.terminal.label,
            destination.location.terminal.layer,
            destination.location.terminal.probability,
            destination.location.terminal.source,
            destination.location.trading_block.id,
            destination.location.trading_block.label,
            destination.location.trading_block.layer,
            destination.location.trading_block.probability,
            destination.location.trading_block.source,
            destination.location.trading_region.id,
            destination.location.trading_region.label,
            destination.location.trading_region.layer,
            destination.location.trading_region.probability,
            destination.location.trading_region.source,
            destination.location.trading_subregion.id,
            destination.location.trading_subregion.label,
            destination.location.trading_subregion.layer,
            destination.location.trading_subregion.probability,
            destination.location.trading_subregion.source,
            destination.pos.0,
            destination.pos.1,
            destination.start_timestamp,
            destination.to_vessel.id,
            destination.to_vessel.label,
            destination.to_vessel.tags.0,
            end_timestamp,
            origin.end_timestamp,
            origin.event_id,
            origin.event_type,
            origin.location.country.id,
            origin.location.country.label,
            origin.location.country.layer,
            origin.location.country.probability,
            origin.location.country.source,
            origin.location.port.id,
            origin.location.port.label,
            origin.location.port.layer,
            origin.location.port.probability,
            origin.location.port.source,
            origin.location.region.id,
            origin.location.region.label,
            origin.location.region.layer,
            origin.location.region.probability,
            origin.location.region.source,
            origin.location.shipping_region.id,
            origin.location.shipping_region.label,
            origin.location.shipping_region.layer,
            origin.location.shipping_region.probability,
            origin.location.shipping_region.source,
            origin.location.terminal.id,
            origin.location.terminal.label,
            origin.location.terminal.layer,
            origin.location.terminal.probability,
            origin.location.terminal.source,
            origin.location.trading_region.id,
            origin.location.trading_region.label,
            origin.location.trading_region.layer,
            origin.location.trading_region.probability,
            origin.location.trading_region.source,
            origin.location.trading_subregion.id,
            origin.location.trading_subregion.label,
            origin.location.trading_subregion.layer,
            origin.location.trading_subregion.probability,
            origin.location.trading_subregion.source,
            origin.pos.0,
            origin.pos.1,
            origin.start_timestamp,
            start_timestamp,
            vessel.corporate_entities.0.id,
            vessel.corporate_entities.0.label,
            vessel.corporate_entities.0.layer,
            vessel.corporate_entities.0.probability,
            vessel.corporate_entities.0.source,
            vessel.corporate_entities.1.end_timestamp,
            vessel.corporate_entities.1.id,
            vessel.corporate_entities.1.label,
            vessel.corporate_entities.1.layer,
            vessel.corporate_entities.1.probability,
            vessel.corporate_entities.1.source,
            vessel.corporate_entities.1.start_timestamp,
            vessel.corporate_entities.2.id,
            vessel.corporate_entities.2.label,
            vessel.corporate_entities.2.layer,
            vessel.corporate_entities.2.probability,
            vessel.corporate_entities.2.source,
            vessel.cubic_capacity,
            vessel.dwt,
            vessel.id,
            vessel.imo,
            vessel.mmsi,
            vessel.name,
            vessel.status,
            vessel.vessel_class,
            vessel_movement_id,
            vessels.corporate_entities.charterer.id,
            vessels.corporate_entities.charterer.label,
            vessels.corporate_entities.charterer.layer,
            vessels.corporate_entities.charterer.probability,
            vessels.corporate_entities.charterer.source,
            vessels.corporate_entities.commercial_owner.id,
            vessels.corporate_entities.commercial_owner.label,
            vessels.corporate_entities.commercial_owner.layer,
            vessels.corporate_entities.commercial_owner.probability,
            vessels.corporate_entities.commercial_owner.source,
            vessels.corporate_entities.time_charterer.end_timestamp,
            vessels.corporate_entities.time_charterer.id,
            vessels.corporate_entities.time_charterer.label,
            vessels.corporate_entities.time_charterer.layer,
            vessels.corporate_entities.time_charterer.probability,
            vessels.corporate_entities.time_charterer.source,
            vessels.corporate_entities.time_charterer.start_timestamp,
            vessels.cubic_capacity,
            vessels.dwt,
            vessels.id,
            vessels.imo,
            vessels.mmsi,
            vessels.name,
            vessels.status,
            vessels.vessel_class,
            voyage_id,
        ]
        ```

        """
        if columns is None:
            columns = DEFAULT_COLUMNS

        flatten = functools.partial(
            convert_vessel_movement_to_flat_dict, cols=columns
        )

        with Pool(os.cpu_count()) as pool:
            records = pool.map(flatten, super().to_list())

        return pd.DataFrame(data=records, columns=columns)


DEFAULT_COLUMNS = [
    "vessel.imo",
    "vessel.name",
    "vessel.vessel_class",
    "origin.event_type",
    "origin.location.port.label",
    "origin.location.country.label",
    "destination.event_type",
    "destination.location.port.label",
    "destination.location.country.label",
    "cargoes.0.product.group_product.label,"
    "cargoes.0.product.category.label",
    "cargoes.0.product.grade.label",
    "cargoes.0.quantity",
    "start_timestamp",
    "end_timestamp",
]
