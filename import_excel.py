import pandas as pd
import sqlite3

# Step 1: Load Excel file
excel_file = "CentralReport1762957484389.xlsx"
df = pd.read_excel(excel_file)

# Step 2: Create new SQLite DB
conn = sqlite3.connect("groundwater.db")

# Step 3: Save Excel data to database table
df.to_sql("groundwater_data", conn, if_exists="replace", index=False)

conn.close()

print("Database successfully created from Excel!")