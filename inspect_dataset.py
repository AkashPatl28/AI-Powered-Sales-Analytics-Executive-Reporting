
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
folder = PROJECT_ROOT / "CRM+Sales+Opportunities"
df = pd.read_csv(folder / "sales_pipeline.csv")

print("\n===== DEAL STAGE SUMMARY =====")
print(df["deal_stage"].value_counts(dropna=False))

print("\n===== MISSING VALUES BY DEAL STAGE =====")
print(
    df.groupby("deal_stage")
    .agg(
        Total_Opportunities=("opportunity_id", "count"),
        Missing_Account=("account", lambda x: x.isna().sum()),
        Missing_Engage_Date=("engage_date", lambda x: x.isna().sum()),
        Missing_Close_Date=("close_date", lambda x: x.isna().sum()),
        Missing_Close_Value=("close_value", lambda x: x.isna().sum())
    )
    .to_string()
)

print("\n===== CLOSE VALUE SUMMARY =====")
print(df.groupby("deal_stage")["close_value"].agg(
    ["count", "sum", "mean", "median"]
).to_string())
