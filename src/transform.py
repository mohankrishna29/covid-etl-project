import pandas as pd

def transform(df):
    df = df.fillna(0)
    df.columns = df.columns.str.upper()
    return df