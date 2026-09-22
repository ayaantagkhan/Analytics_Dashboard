from pathlib import Path

import pandas as pd
from cleaning import( 
    remove_duplicates, 
    clean_dates, 
    clean_text, 
    clean_amount
)

from database import(
    insert_expenses
)

def main():
    project_folder = Path(__file__).parent
    input_file =  project_folder / "personal_expenses.xlsx"
    output_file = project_folder / "expenses_cleaned.csv"

    dataframe = pd.read_excel(input_file)

    dataframe = remove_duplicates(dataframe)
    dataframe = clean_dates(dataframe)
    dataframe = clean_amount(dataframe)
    dataframe = clean_text(dataframe)

    dataframe.to_csv(output_file, index =False)

    insert_expenses(dataframe)
    
    print(f"Cleaned file saved to {output_file}")
    print("Expenses inserted into MySQL.")

    
if __name__ == '__main__':
    main()