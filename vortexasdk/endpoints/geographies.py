"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/docs-interactive?filepath=docs%2Fexamples%2Ftry_me_out%2Fgeographies.ipynb)
"""
from typing import Dict, List, Union

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

    def search(
        self,
        term: Union[str, List[str]] = None,
        exact_term_match: bool = False,
    ) -> GeographyResult:
        """
        Find all geographies matching given search terms.

        # Arguments
            term: The geography name (or names) we're filtering on

            exact_term_match: Search on only exact term matches, or allow similar matches.
                e.g. When searching for "China" with `exact_term_match=False`, then the SDK will yield geographies named
                ['China', 'South China', 'China Energy Services Ningbo'...] etc. When `exact_term_match=True`,
                the SDK will only yield the geography named `China`.


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
        api_params = convert_values_to_list({"term": term})

        return GeographyResult(
            super().search(exact_term_match=exact_term_match, **api_params)
        )

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
