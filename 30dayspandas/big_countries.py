import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # selecting rows based on condition
    rslt_df = world[(world["area"] >= 3000000) | (world["population"] >= 25000000)]

    return rslt_df[["name", "population", "area"]]
