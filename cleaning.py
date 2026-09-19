# importing library

import pandas as pd 

dataframe = pd.read_excel("personal_expenses.xlsx")

def remove_duplicates(dataframe):
    dataframe = dataframe.drop_duplicates()
    return dataframe

def clean_dates(dataframe):
    dataframe = dataframe.copy()
    
    numeric_dates = pd.to_numeric(
        dataframe['Date'], 
        errors = 'coerce')

    is_numeric = numeric_dates.notna()

    dates = pd.to_datetime(
        numeric_dates,
        unit = 'D',
        origin = '1899-12-30',
        errors = 'coerce'
)
    dates.loc[~is_numeric] = pd.to_datetime(
        dataframe.loc[~is_numeric, 'Date'],
        format = 'mixed',
        errors = 'coerce',
)

    dataframe['Date'] = dates
    return dataframe


