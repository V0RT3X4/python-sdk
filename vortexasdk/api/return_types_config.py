from typing import TypeVar

from vortexasdk.api.geography import Geography
from vortexasdk.api.product import Product
from vortexasdk.api.vessel import Vessel
from vortexasdk.api.corporation import Corporation
from vortexasdk.api.cargo_movement import CargoMovement
from vortexasdk.api.entity_flattening import flatten_dictionary
from vortexasdk.api.entity_flattening import (
    convert_cargo_movement_to_flat_dict,
)

ReturnType = TypeVar(
    "ReturnType", Geography, Product, Vessel, Corporation, CargoMovement
)

permitted_return_types = {
    Geography,
    Product,
    Vessel,
    Corporation,
    CargoMovement,
}

default_columns = {
    Geography: ["id", "name", "layer"],
    Product: ["id", "name", "layer.0", "parent.0.name"],
    Vessel: ["id", "name", "imo", "vessel_class"],
    Corporation: ["id", "name", "corporate_entity_type"],
    CargoMovement: [
        "events.cargo_port_load_event.0.label",
        "events.cargo_port_unload_event.0.label",
        "product.group.label",
        "product.grade.label",
        "quantity",
        "vessels.0.name",
        "events.cargo_port_load_event.0.end_timestamp",
        "events.cargo_port_unload_event.0.start_timestamp",
    ],
}

flatten_method_dict = {
    Product: flatten_dictionary,
    CargoMovement: convert_cargo_movement_to_flat_dict,
}
