from typing import List, Type, Sequence

import pandas as pd

from vortexasdk.api.return_types_config import (
    default_columns,
    permitted_return_types,
    ReturnType,
    flatten_method_dict,
)
from vortexasdk.utils import run_as_multiprocess


class Result:
    def __init__(self, records: List, return_type: Type[ReturnType]):
        self.records = records
        self.return_type = return_type
        self.default_columns = self._get_default_columns()

    def to_list(self) -> List:
        """Convert results set to list"""
        data = run_as_multiprocess(self.return_type.from_dict, self.records)
        return list(data)

    def to_df(self, columns=None):
        """Convert results set to pandas DataFrame"""
        data = self._flatten_data()
        columns = columns or self.default_columns

        df = pd.DataFrame(data)
        if columns == "all":
            return df
        else:
            return df[columns]

    def _get_default_columns(self) -> List[str]:
        """Get default columns from config dict"""
        return default_columns.get(self.return_type, None)

    def _flatten_data(self) -> Sequence:
        """Optionally flatten return type data"""
        flatten_method = flatten_method_dict.get(self.return_type, None)
        if flatten_method is None:
            data = self.records
        else:
            data = run_as_multiprocess(flatten_method, self.records)
        return data

    @property
    def return_type(self):
        return self.__return_type

    @return_type.setter
    def return_type(self, return_type_value):
        if return_type_value not in permitted_return_types:
            raise ValueError(
                f"{return_type_value} is not a permitted return_type"
            )
        else:
            self.__return_type = return_type_value

    @property
    def default_columns(self):
        return self.__default_columns

    @default_columns.setter
    def default_columns(self, default_col_values):
        self.__default_columns = default_col_values

    def __len__(self):
        return len(self.records)

    def __str__(self):
        return str(self.records)

    def __iter__(self):
        return iter(self.records)

    def __getitem__(self, item):
        return self.records.__getitem__(item)
