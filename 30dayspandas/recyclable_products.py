import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # selecting rows based on condition
    rslt_df = products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")]

    return rslt_df[["product_id"]]
