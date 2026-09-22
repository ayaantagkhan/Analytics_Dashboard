import os
import mysql.connector
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def mysql_value(value):
    return None if pd.isna(value) else value

def insert_expenses(dataframe):
    connection = mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME"),
    )

    cursor = connection.cursor()

    insert_query = """
        INSERT INTO expenses (
            expense_date,
            amount,
            merchant,
            payment_method,
            category
        )
        VALUES (%s, %s, %s, %s, %s)
    """

    rows = []

    for _, row in dataframe.iterrows():
        expense_date = (
            row["Date"].date()
            if pd.notna(row["Date"])
            else None
        )

        amount = (
            float(row["Amount"])
            if pd.notna(row["Amount"])
            else None
        )

        rows.append(
            (
                expense_date,
                amount,
                mysql_value(row["Merchant"]),
                mysql_value(row["Payment Method"]),
                mysql_value(row["Category"]),
            )
        )

    cursor.executemany(insert_query, rows)
    connection.commit()




