import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # selecting rows based on condition
    rslt_df = customers[~customers["id"].isin(orders["customerId"])]
    return rslt_df[["name"]].rename(columns={"name": "Customers"})
