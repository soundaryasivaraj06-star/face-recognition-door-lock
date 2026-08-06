import pandas as pd

df = pd.read_csv("entry_log.csv")

print("\n📋 DAILY ENTRY REPORT\n")
print(df)

df.to_csv("daily_report.csv", index=False)