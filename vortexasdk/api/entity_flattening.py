from itertools import groupby
from typing import Dict, List

# noinspection PyProtectedMember
from flatten_dict import flatten
import copy


def flatten_dictionary(d: Dict) -> Dict:
    """Flatten dictionary, then format keys."""
    return _format_keys(flatten(d, enumerate_types=(list,)))


def _format_keys(dictionary):
    flat_with_formatted_keys = {}
    for k, v in dictionary.items():
        nice_path = ".".join([str(i) for i in k])
        flat_with_formatted_keys[nice_path] = v
    return flat_with_formatted_keys


def convert_cargo_movement_to_flat_dict(cme: Dict, cols="all") -> Dict:
    """Convert nested `CargoMovement` object to flat dictionary, keeping *cols*."""
    as_dict = _group_cargo_movement_attributes_by_layer(cme)

    formatted = flatten_dictionary(as_dict)

    if cols == "all":
        return formatted
    else:
        return {k: v for k, v in formatted.items() if k in cols}


def convert_vessel_movement_to_flat_dict(vm: Dict, cols="all") -> Dict:
    """Convert nested `VesselMovement` dict to flat dictionary, keeping *cols*."""
    as_dict = _group_vessel_movement_attributes_by_layer(vm)

    formatted = flatten_dictionary(as_dict)

    if cols == "all":
        return formatted
    else:
        return {k: v for k, v in formatted.items() if k in cols}


def _group_vessel_movement_attributes_by_layer(vm: Dict) -> Dict:
    """Group relevant `VesselMovement` attributes by `Entity.layer`."""
    if "origin" in vm.keys():
        flat_origin = _flatten_attributes(vm["origin"], "location")
        vm["origin"] = flat_origin

    if "destination" in vm.keys():
        flat_destination = _flatten_attributes(vm["destination"], "location")
        vm["destination"] = flat_destination

    if "cargoes" in vm.keys():
        flat_cargoes = [
            _flatten_attributes(cargo, "product") for cargo in vm["cargoes"]
        ]
        vm["cargoes"] = flat_cargoes

    vm["vessel"] = _flatten_vessel_entity(vm["vessel"])
    return vm


def _group_cargo_movement_attributes_by_layer(cm: Dict) -> Dict:
    """Group relevant `CargoMovement` attributes by `Entity.layer`."""
    vessels = [_flatten_vessel_entity(ve) for ve in cm["vessels"]]

    events = {
        event_type: list(g)
        for event_type, g in groupby(cm["events"], lambda x: x["event_type"])
    }

    events_attributes = {
        event_type: [_flatten_attributes(ce, "location") for ce in es]
        for event_type, es in events.items()
    }

    cm = _flatten_attributes(cm, "product")
    cm["vessels"] = vessels
    cm["events"] = events_attributes
    return cm


def _flatten_vessel_entity(vessel_entity: Dict) -> Dict:
    return _flatten_attributes(vessel_entity, "corporate_entities")


def _flatten_attributes(dictionary: Dict, key: str) -> Dict:
    """Group the key values by layer."""
    copied_dict = copy.deepcopy(dictionary)

    entity_list: List[Dict] = copied_dict[key]

    grouped_by_layer = {e["layer"]: e for e in entity_list}

    copied_dict[key] = grouped_by_layer

    return copied_dict


def _group_by_layer(entity_list: List[Dict]) -> Dict:
    return {e["layer"]: e for e in entity_list}
