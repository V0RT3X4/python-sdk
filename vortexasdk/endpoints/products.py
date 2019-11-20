"""Products Endpoint."""
from typing import List, Union

import pandas as pd

from vortexasdk.api.product import Product
from vortexasdk.api.search_result import Result
from vortexasdk.api.shared_types import ID
from vortexasdk.endpoints.endpoints import PRODUCTS_REFERENCE
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import convert_values_to_list


class ProductResult(Result):
    """Container class that holds the result obtained from calling the `Product` endpoint."""
    DEFAULT_COLUMNS = ["id", "name", "parent"]

    def to_list(self) -> List[Product]:
        """Represent products as a list."""
        return super().serialize_dataclass(List[Product])

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent products as a `pd.DataFrame`.

        # Arguments
            columns: The product features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'parent']`.

        # Returns
        `pd.DataFrame` of products.

        """
        return super().to_df(columns=columns)


class Products(Reference, Search):
    """Vessels endpoint."""

    def __init__(self):
        """Instantiate endpoint using reference endpoint."""
        Reference.__init__(self, PRODUCTS_REFERENCE)
        Search.__init__(self, PRODUCTS_REFERENCE)

    def reference(self, id: ID):
        """
        Perform a product lookup.

        # Arguments
            id: Product ID to lookup

        # Returns
        Product record matching the ID

        # Further Documentation:
        [VortexaAPI Product Reference](https://docs.vortexa.com/reference/POST/reference/products)

        """
        return super().reference(id)

    def search(self,
               term: Union[str, List[str]] = None,
               ids: Union[str, List[str]] = None,
               product_parent: Union[str, List[str]] = None,
               ) -> ProductResult:
        """
        Find all products matching given search terms.

        # Arguments
            term: The name(s) (or partial name(s)) of a product we'd like to search

            ids: ID or IDs of products we'd like to search

            product_parent: ID, or list of IDs of the immediate product parent. E.g. `product_parent ='12345'` will return all children of product `12345`. 

        # Returns
        List of products matching the search arguments.


        # Examples

        Let's find all the products with 'sul' in their name, or related names.

        ```python
        >>> Products().search(term='sul').to_df()
        ```

        |    | id         |     name   |             parent                     |
        |---:|:-----------|------------|---------------------------------------:|
        |  0 | 'a250444...| Marlim Sul |[{'name': 'Heavy-Sour', 'layer': ['su...|


        Note the `term` search also looks for products with matching `related_names`


        # Further Documentation

        [VortexaAPI Vessel Reference](https://docs.vortexa.com/reference/POST/reference/products)

        """
        search_params = convert_values_to_list({
            "term": term,
            "ids": ids,
            "product_parent": product_parent,
        })

        return ProductResult(super().search(**search_params))
