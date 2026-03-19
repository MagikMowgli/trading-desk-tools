import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
        )

cur = conn.cursor()

trade_id = input("Enter trade ID: ")

cur.execute("SELECT * FROM trades WHERE trade_id = %s;", (trade_id,))

trade = cur.fetchone()

if trade:
    print("\nTrade Found:")
    print(f"Trade ID: {trade[0]}")
    print(f"Instrument: {trade[1]}")
    print(f"Quantity: {trade[2]}")
    print(f"Price: {trade[3]}")
else:
    print("\nTrade not found")

cur.close()
conn.close()
