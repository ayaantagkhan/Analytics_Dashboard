# importing library

import pandas as pd 

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
        dataframe[column] = dataframe[column].str.strip()

        if column in ["Category", "Payment Method"]:
            dataframe[column] = dataframe[column].str.title()

    return dataframe

def clean_recurring(dataframe):
    dataframe = dataframe.copy()

    dataframe["Recurring"] = (
        dataframe["Recurring"]
        .astype("string")
        .str.strip()
        .str.lower()
        .map({
            "yes": "Yes",
            "y": "Yes",
            "no": "No",
            "n": "No",
        })
    )

    return dataframe

def clean_merchants(dataframe):
    dataframe = dataframe.copy()

    dataframe["Merchant"] = (
        dataframe["Merchant"]
        .str.strip()
        .str.title()
        .replace({
            "Cvs Pharmacy": "CVS Pharmacy",
            "At&t": "AT&T",
            "Doordash": "DoorDash",
            "Quiktrip": "QuikTrip",
            "La Fitness": "LA Fitness",
            "Txu Energy": "TXU Energy",
            "Amc Theatres": "AMC Theatres",
        })
    )

    return dataframe

def clean_categories(dataframe):
    dataframe = dataframe.copy()

    dataframe["Category"] = (
        dataframe["Category"]
        .str.strip()
        .str.title()
        .replace("", pd.NA)
        .fillna("Uncategorized")
    )

    return dataframe

def clean_payment_methods(dataframe):
    dataframe = dataframe.copy()

    dataframe["Payment Method"] = (
        dataframe["Payment Method"]
        .str.strip()
        .str.title()
        .replace("", pd.NA)
        .fillna("Uncategorized")
    )
    
    return dataframe

def clean_locations(dataframe):
    dataframe = dataframe.copy()

    dataframe["Location"] = (
        dataframe["Location"]
        .str.strip()
        .str.title()
        .str.replace(
            r",\s*([A-Za-z]{2})$",
            lambda match: ", " + match.group(1).upper(),
            regex = True
        )
        .replace("", pd.NA)
        .fillna("Unknown")
    )

    return dataframe

def clean_descriptions(dataframe):
    dataframe = dataframe.copy()

    dataframe["Description"] = (
        dataframe["Description"]
        .str.strip()
        .str.replace(r"\s+"," ", regex=True)
        .fillna("")
    )
    
    return dataframe

def validate_expenses(dataframe):
    dataframe = dataframe.copy()

    dataframe["Missing Date"] = dataframe["Date"].isna()
    dataframe["Missing Amount"] = dataframe["Amount"].isna()
    dataframe["Possible Refund"] = dataframe["Amount"] < 0

    return dataframe

def clean_expenses(dataframe):
    steps = [
        clean_dates,
        clean_amount,
        clean_text,
        clean_recurring,
        clean_merchants,
        clean_categories,
        clean_payment_methods,
        clean_locations,
        clean_descriptions,
        remove_duplicates,
        validate_expenses,
    ]

    for step in steps:
        dataframe = step(dataframe)

    return dataframe

