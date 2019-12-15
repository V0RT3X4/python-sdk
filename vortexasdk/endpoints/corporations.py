"""Corporations Endpoint."""
from typing import List, Union, Dict

from vortexasdk.api import ID
from vortexasdk.endpoints.corporations_result import CorporationsResult
from vortexasdk.endpoints.endpoints import CORPORATIONS_REFERENCE
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import convert_values_to_list


class Corporations(Reference, Search):
    """Corporations Endpoint."""

    def __init__(self):
        Reference.__init__(self, CORPORATIONS_REFERENCE)
        Search.__init__(self, CORPORATIONS_REFERENCE)

    def load_all(self) -> CorporationsResult:
        """Load all corporations."""
        return self.search()

    def search(self, term: Union[str, List[str]] = None) -> CorporationsResult:
        """
        Find all Corporations matching given search terms.

        # Arguments
            term: The corporation name(s) we're filtering on

        # Returns
        List of corporation matching `term`


        # Examples

        Let's load all corporations
        ```python
        >>> from vortexasdk import Corporations
        >>> df = Corporations().search().to_df()

        ```
        returns

        |    | id                                                               | name       | corporate_entity_type   |
        |---:|:-----------------------------------------------------------------|:-----------|:------------------------|
        |  0 | 04f418ee78c1e17744ad653e7815e8e28891ed9ba25a8427030e4478e5c00974 | 3J         | ['commercial_owner']    |
        |  1 | b6384cf17f1639a64bbff04cfd32257bf732a3a13e4b0532802a9ae84a36be34 | 5XJAPANESE | ['commercial_owner']    |


        Let's find all corporations with 'do' in the name.
        ```python
        >>> [x.name for x in Corporations().search(term="do").to_list()]
        [...]

        ```

        # Further Documentation

        [VortexaAPI Corporation Reference](https://docs.vortexa.com/reference/POST/reference/charterers)

        """
        params = convert_values_to_list({"term": term})
        return CorporationsResult(super().search(**params))

    def reference(self, id: ID) -> Dict:
        """
        Perform a corporation lookup.

        # Arguments
            id: Corporation ID to lookup

        # Returns
        Corporation record matching the ID

        # Further Documentation:
        [VortexaAPI Corporation Reference](https://docs.vortexa.com/reference/GET/reference/charterers/%7Bid%7D)

        # Examples
        >>> Corporations().reference(id='12345abcdef') # doctest: +SKIP

        """
        return super().reference(id)
