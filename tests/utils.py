import pandas as pd
import tabulate


def to_markdown(df: pd.DataFrame) -> str:
    return tabulate.tabulate(df, headers=df.columns, tablefmt="pipe")
