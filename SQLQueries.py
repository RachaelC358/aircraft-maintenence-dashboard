import sqlite3
import pandas as pd

conn = sqlite3.connect("database/maintenance.db")
cursor = conn.cursor()

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

conn.close()

# Optional: Print results to console
print("Average Downtime by Maintenance Type:\n", df1, "\n")
print("Top Failure Codes:\n", df2, "\n")
print("Aircrafts with Highest Downtime:\n", df3, "\n")
