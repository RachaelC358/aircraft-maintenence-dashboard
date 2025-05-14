import pandas as pd


with pd.ExcelWriter("excel/maintenance_summary.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Avg Downtime", index=False)
    df2.to_excel(writer, sheet_name="Top Failures", index=False)
    df3.to_excel(writer, sheet_name="Aircraft Downtime", index=False)

print("Summary report saved to: excel/maintenance_summary.xlsx")
