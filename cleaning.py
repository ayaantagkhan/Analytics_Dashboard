# importing library

import pandas as pd 

dataframe = pd.read_excel("personal_expenses.xlsx")

dataframe = dataframe.drop_duplicates()

# fixing the date column
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

