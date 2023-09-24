import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # selecting rows based on condition
    rslt_df = views[(views["author_id"] == views["viewer_id"])]

    return (
        rslt_df[["author_id"]]
        .rename(columns={"author_id": "id"})
        .drop_duplicates()
        .sort_values(["id"], ascending=True)
    )
