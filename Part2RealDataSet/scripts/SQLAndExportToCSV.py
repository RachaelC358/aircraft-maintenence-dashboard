import os
import pandas as pd
import sqlite3

conn = sqlite3.connect(r"C:\Users\carpr\OneDrive\Desktop\work\aircraft-maintenence-dashboard\Part2RealDataSet\output\maintenance.db")
output_dir = r"C:\Users\carpr\OneDrive\Desktop\work\aircraft-maintenence-dashboard\Part2RealDataSet"


# Run first query
df1 = pd.read_sql_query("""
SELECT skill, SUM([mxh_est.]) AS total_estimated_hours
FROM tasks
GROUP BY skill
ORDER BY total_estimated_hours DESC;
""", conn)
df1.to_csv(os.path.join(output_dir, "output/skill_labor_summary.csv"), index=False)

# Run second query
df2 = pd.read_sql_query("""
SELECT block, COUNT(*) AS task_count
FROM tasks
GROUP BY block
ORDER BY task_count DESC;
""", conn)
df2.to_csv(os.path.join(output_dir, "output/block_task_summary.csv"), index=False)
