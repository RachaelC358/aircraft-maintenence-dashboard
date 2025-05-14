import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("database/maintenance.db")

# === Run SQL Queries ===

# 1. Average Downtime by Maintenance Type
query1 = """
SELECT maintenance_type, AVG(downtime_hours) AS avg_downtime
FROM MaintenanceLogs
GROUP BY maintenance_type
ORDER BY avg_downtime DESC;
"""
df1 = pd.read_sql_query(query1, conn)

# 2. Top 5 Most Frequent Failure Codes
query2 = """
SELECT failure_code, COUNT(*) AS frequency
FROM MaintenanceLogs
GROUP BY failure_code
ORDER BY frequency DESC
LIMIT 5;
"""
df2 = pd.read_sql_query(query2, conn)

# 3. Aircrafts with Highest Total Downtime
query3 = """
SELECT aircraft_id, SUM(downtime_hours) AS total_downtime
FROM MaintenanceLogs
GROUP BY aircraft_id
ORDER BY total_downtime DESC
LIMIT 5;
"""
df3 = pd.read_sql_query(query3, conn)

# Close the DB connection
conn.close()

# === Export to CSV ===
df1.to_csv("excel/avg_downtime.csv", index=False)
df2.to_csv("excel/top_failures.csv", index=False)
df3.to_csv("excel/aircraft_downtime.csv", index=False)

print("CSV exports complete. Files saved in the 'excel/' folder.")

