from pathlib import Path

import pandas as pd

from cleaning import remove_duplicates, clean_dates, clean_text, clean_amount

def main():
    input_file = Path(__file__).parent / 'personal_expenses.xlsx'

    dataframe = pd.read_excel(input_file)
    dataframe = remove_duplicates(dataframe)
    dataframe = clean_dates(dataframe)
    dataframe = clean_amount(dataframe)
    dataframe = clean_text(dataframe)

    print(dataframe.head())
    print(dataframe['Amount'].head())

if __name__ == '__main__':
    main()