import pandas as pd
from faker import Faker
import random

fake = Faker()

# Simulate 100 rows of maintenance data
rows = []
maintenance_types = ['Engine', 'Avionics', 'Hydraulics', 'Electrical', 'Software']
failure_codes = ['F203', 'F110', 'F401', 'F999', 'F120']
parts = ['Turbine Blade', 'Sensor Board', 'Hydraulic Pump', 'Power Unit', 'Main CPU']

for _ in range(100):
    row = {
        "aircraft_id": f"A-{random.randint(1000, 1100)}",
        "date": fake.date_between(start_date='-1y', end_date='today'),
        "maintenance_type": random.choice(maintenance_types),
        "failure_code": random.choice(failure_codes),
        "part_replaced": random.choice(parts),
        "downtime_hours": round(random.uniform(1, 48), 1)
    }
    rows.append(row)

df = pd.DataFrame(rows)
df.to_excel("excel/maintenance_input.xlsx", index=False)

print("Excel file generated at: excel/maintenance_input.xlsx")
