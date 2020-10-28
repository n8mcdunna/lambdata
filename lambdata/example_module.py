'''Lamdata - collection of data science functions'''

# access libraries through pipenv
import pandas as pd
import numpy as np
import random

FAVORITE_NUMS = [9, 14, 43]

def number_of_nulls(df):
    """Checks a dataframe for nulls and returns number of nulls"""
    return df.isnull().values.sum()


def add_list_to_df(list, df):
    df['new col'] = pd.Series(list)
    return df

class MyDataFrame(pd.DataFrame):
    def num_nulls(self):
        return self.isnull().values.sum()