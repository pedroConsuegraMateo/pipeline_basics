import pandas as pd

# Wrangling methods

def wrangling(df, year):
    df_filtered = df[df['Year'] == year]
    return df_filtered