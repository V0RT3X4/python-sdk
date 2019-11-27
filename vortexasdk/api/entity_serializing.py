from itertools import groupby
from typing import Dict, List

# noinspection PyProtectedMember
from flatten_dict import flatten


def _group_by_layer(entity_list: List[Dict]) -> Dict:
    return {e["layer"]: e for e in entity_list}


def _format_keys(dictionary):
    flat_with_formatted_keys = {}
    for k, v in dictionary.items():
        nice_path = ".".join([str(i) for i in k])
        flat_with_formatted_keys[nice_path] = v
    return flat_with_formatted_keys


def _serialize_ve_layer(ve: Dict) -> Dict:
    ve["corporate_entities"] = _group_by_layer(ve["corporate_entities"])
    return ve


def _serialize_ce_layer(ce: Dict) -> Dict:
    ce["location"] = _group_by_layer(ce["location"])
    return ce


def _group_cme_attributes_by_layer(cme: Dict) -> Dict:
    """Group relevant CargoMovementEntity attributes by `Entity.layer`."""
    vessels = [_serialize_ve_layer(ve) for ve in cme["vessels"]]
    products = _group_by_layer(cme["product"])

    events = {
        event_type: list(g)
        for event_type, g in groupby(cme["events"], lambda x: x["event_type"])
    }

    events_attributes = {
        event_type: [_serialize_ce_layer(ce) for ce in es]
        for event_type, es in events.items()
    }

    cme["product"] = products
    cme["vessels"] = vessels
    cme["events"] = events_attributes
    return cme


def convert_cme_to_flat_dict(cme: Dict, cols="all") -> Dict:
    """Convert nested `CargoMovementEntity` object to flat dictionary, keeping *cols*."""
    as_dict = _group_cme_attributes_by_layer(cme)

    formatted = flatten_dictionary(as_dict)

    if cols == "all":
        return formatted
    else:
        return {k: v for k, v in formatted.items() if k in cols}


def flatten_dictionary(d: Dict) -> Dict:
    """Flatten dictionary, then format keys."""
    return _format_keys(flatten(d, enumerate_types=(list,)))
