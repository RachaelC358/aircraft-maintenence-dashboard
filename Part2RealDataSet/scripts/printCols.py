import sqlite3

conn = sqlite3.connect(r"C:\Users\carpr\OneDrive\Desktop\work\aircraft-maintenence-dashboard\Part2RealDataSet\output\maintenance.db")
cursor = conn.cursor()

# Show column names
cursor.execute("PRAGMA table_info(tasks);")
for col in cursor.fetchall():
    print(col)
