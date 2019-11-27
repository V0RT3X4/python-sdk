from typing import Dict, TypeVar

import jsons

T = TypeVar("T")


def serialize_to_dict(dataclass) -> Dict:
    """Serialize data class attributes."""
    return jsons.loads(jsons.dumps(dataclass))


class FromDictMixin:
    """Mixin allowing serialization of a dictionary to a dataclass."""

    @classmethod
    def from_dict(cls: T, d: Dict) -> T:
        """Serialize dictionary to dataclass of type T."""
        return jsons.loads(jsons.dumps(d), cls)
