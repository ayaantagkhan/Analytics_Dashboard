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

def clean_amount(dataframe):
    dataframe = dataframe.copy()

    amounts = dataframe['Amount']
    amounts = amounts.astype(str)
    amounts = amounts.str.replace(r'[$,\s]', '', regex=True)

    dataframe['Amount'] = pd.to_numeric(
        amounts,
        errors = 'coerce'
    )
    
    return dataframe

def clean_text(dataframe):
    dataframe = dataframe.copy()

    text_columns = dataframe.select_dtypes(
        include=['object', 'string']).columns

    for column in text_columns:
        dataframe[column] = dataframe[column].str.strip().str.title()

    return dataframe
