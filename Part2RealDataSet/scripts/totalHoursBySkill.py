import pandas as pd
import os

output_dir = os.path.join("..", "output")

os.makedirs(output_dir, exist_ok=True)  

xlsx_path = r"C:\Users\carpr\OneDrive\Desktop\work\aircraft-maintenence-dashboard\Part2RealDataSet\data\Task Allocation Input 2018-2021.xlsx"

df = pd.read_excel(xlsx_path, sheet_name="Tasks")

# Clean column names
df.columns = df.columns.str.strip()

# Convert maintenance hours to numeric
df['Mxh EST.'] = pd.to_numeric(df['Mxh EST.'], errors='coerce')

# Group by SKILL and sum the maintenance hours
maintenance_by_skill = df.groupby('SKILL')['Mxh EST.'].sum().reset_index()

# Rename columns
maintenance_by_skill.columns = ['Skill', 'Total Maintenance Hours']

maintenance_by_skill.to_csv(os.path.join(output_dir, "maintenance_by_skill.csv"), index=False)


