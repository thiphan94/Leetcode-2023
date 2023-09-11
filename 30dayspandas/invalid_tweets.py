import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # selecting rows based on condition
    rslt_df = tweets[(tweets["content"].str.len() > 15)]

    return rslt_df[["tweet_id"]]