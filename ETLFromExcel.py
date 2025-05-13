import pandas as pd
import sqlite3

# Load Excel data
df = pd.read_excel("excel/maintenance_input.xlsx")

# Connect to SQLite DB (creates file if not exists)
conn = sqlite3.connect("database/maintenance.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS MaintenanceLogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aircraft_id TEXT,
    date TEXT,
    maintenance_type TEXT,
    failure_code TEXT,
    part_replaced TEXT,
    downtime_hours REAL
)
""")

# Insert data
df.to_sql("MaintenanceLogs", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("Data loaded into SQLite database at: database/maintenance.db")
