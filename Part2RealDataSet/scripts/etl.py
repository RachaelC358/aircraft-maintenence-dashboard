import pandas as pd
import sqlite3

xlsx_path = r"C:\Users\carpr\OneDrive\Desktop\work\aircraft-maintenence-dashboard\Part2RealDataSet\data\Task Allocation Input 2018-2021.xlsx"

# Print sheet names to verify
#xls = pd.ExcelFile(xlsx_path)
#print("Available sheets:", xls.sheet_names)

# Load individual sheets
tasks_df = pd.read_excel(xlsx_path, sheet_name="Tasks")
skills_df = pd.read_excel(xlsx_path, sheet_name="Skill_Type")
techs_df = pd.read_excel(xlsx_path, sheet_name="Number_of_Technicians")

# === Clean column names ===
tasks_df.columns = tasks_df.columns.str.strip().str.lower().str.replace(' ', '_')
skills_df.columns = skills_df.columns.str.strip().str.lower().str.replace(' ', '_')
techs_df.columns = techs_df.columns.str.strip().str.lower().str.replace(' ', '_')

# === Open SQLite connection ===
conn = sqlite3.connect(r"C:\Users\carpr\OneDrive\Desktop\work\aircraft-maintenence-dashboard\Part2RealDataSet\output\maintenance.db")

# Save DataFrames to SQLite
tasks_df.to_sql("tasks", conn, if_exists="replace", index=False)
skills_df.to_sql("skill_type", conn, if_exists="replace", index=False)
techs_df.to_sql("technicians", conn, if_exists="replace", index=False)

print("Data loaded into SQLite")
