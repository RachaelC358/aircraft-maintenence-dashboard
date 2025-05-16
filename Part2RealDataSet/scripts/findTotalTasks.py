import pandas as pd

xlsx_path = r"C:\Users\carpr\OneDrive\Desktop\work\aircraft-maintenence-dashboard\Part2RealDataSet\data\Task Allocation Input 2018-2021.xlsx"

df = pd.read_excel(xlsx_path, sheet_name="Tasks") 

# Count total number of tasks (rows)
total_tasks = len(df)

print(f"Total number of recorded maintenance tasks: {total_tasks}")