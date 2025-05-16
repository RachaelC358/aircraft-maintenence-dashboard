import os
import pandas as pd
import sqlite3

# Set paths
script_dir = os.path.dirname(__file__)
output_dir = os.path.abspath(os.path.join(script_dir, '..', 'output'))
db_path = os.path.join(output_dir, 'maintenance.db')

# Connect to SQLite
conn = sqlite3.connect(db_path)

# Query to aggregate task data by month
query = """
SELECT
    strftime('%Y-%m', last_exec_dt) AS month,
    COUNT(*) AS total_tasks,
    SUM(CASE
            WHEN last_exec_dt > limit_exec_dt
                 AND last_exec_dt IS NOT NULL
                 AND limit_exec_dt IS NOT NULL
            THEN 1 ELSE 0
        END) AS delayed_tasks,
    AVG("mxh_est.") AS avg_estimated_hours
FROM tasks
WHERE last_exec_dt IS NOT NULL
GROUP BY month
ORDER BY month;
"""

df = pd.read_sql_query(query, conn)

# Convert 'month' column to datetime 
df['month'] = pd.to_datetime(df['month'], format='%Y-%m')


df.to_csv(os.path.join(output_dir, 'tasks_summary_over_time.csv'), index=False)


conn.close()
