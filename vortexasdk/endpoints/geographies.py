"""Geographies Endpoint."""
from typing import List, Union, Dict

from vortexasdk.api import ID
from vortexasdk.endpoints.endpoints import GEOGRAPHIES_REFERENCE
from vortexasdk.endpoints.geographies_result import GeographyResult
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import convert_values_to_list


class Geographies(Reference, Search):
    """Geographies endpoint."""

    def __init__(self):
        Reference.__init__(self, GEOGRAPHIES_REFERENCE)
        Search.__init__(self, GEOGRAPHIES_REFERENCE)

    def load_all(self) -> GeographyResult:
        """Load all geographies."""
        return self.search()

    def search(self, term: Union[str, List[str]] = None) -> GeographyResult:
        """
        Find all geographies matching given search terms.

        # Arguments
            term: The geography name (or names) we're filtering on

        # Returns
        List of geographies matching `term`


        # Examples

        Find all geographies with `portsmouth` in the name.
        ```python
        >>> from vortexasdk import Geographies
        >>> [x.name for x in Geographies().search(term="portsmouth").to_list()]
        ['Portsmouth [GB]', 'Portsmouth, NH [US]']

        ```

        Search multiple geography terms
        ```python
        >>> df = Geographies().search(term=["Liverpool", "Southampton"]).to_df()

        ```
        returns

        |    | id                | name                   | layer        |
        |---:|:------------------|:-----------------------|:-------------|
        |  0 | b63d8f625669fd... | Liverpool [GB]         | ['port']     |
        |  1 | 0cb7d4566de0f2... | Southampton [GB]       | ['port']     |
        |  2 | 8b4273e3181f2d... | Liverpool Docks        | ['terminal'] |
        |  3 | 98c50b0d2ee2b1... | Liverpool Bulk Liquids | ['terminal'] |
        """
        params = convert_values_to_list({"term": term})
        return GeographyResult(super().search(**params))

    def reference(self, id: ID) -> Dict:
        """
        Perform a geography lookup.

        # Arguments
            id: Geography ID to lookup

        # Returns
         Geography matching the ID

        # Further Documentation:
        [VortexaAPI Geography Reference](https://docs.vortexa.com/reference/GET/reference/geographies/%7Bid%7D)

        """
        return super().reference(id)
