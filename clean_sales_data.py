
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

folder = PROJECT_ROOT / "CRM+Sales+Opportunities"
output_folder = PROJECT_ROOT / "cleaned_data"
output_folder.mkdir(exist_ok=True)

# Load source data
sales = pd.read_csv(folder / "sales_pipeline.csv")
accounts = pd.read_csv(folder / "accounts.csv")
teams = pd.read_csv(folder / "sales_teams.csv")
products = pd.read_csv(folder / "products.csv")

# Clean sector spelling and whitespace
accounts["sector"] = accounts["sector"].str.strip().str.lower()
accounts["sector"] = accounts["sector"].replace({
    "technolgy": "technology"
})

# Standardize text columns
for df in [sales, accounts, teams, products]:
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

# Convert dates safely
sales["engage_date"] = pd.to_datetime(
    sales["engage_date"], errors="coerce"
)
sales["close_date"] = pd.to_datetime(
    sales["close_date"], errors="coerce"
)

# Keep missing values as missing; do not invent dates or revenue
# Save cleaned tables for SQL Server and Power BI
sales.to_csv(output_folder / "sales_pipeline_clean.csv", index=False)
accounts.to_csv(output_folder / "accounts_clean.csv", index=False)
teams.to_csv(output_folder / "sales_teams_clean.csv", index=False)
products.to_csv(output_folder / "products_clean.csv", index=False)

print("Cleaning completed.")
print("Files saved to:", output_folder)
print("Sales rows:", len(sales))
print("Account rows:", len(accounts))
print("Team rows:", len(teams))
print("Product rows:", len(products))
print("Corrected technology sector rows:",
      (accounts["sector"] == "technology").sum())
print("Duplicate opportunity IDs:",
      sales["opportunity_id"].duplicated().sum())
print("Missing close values:", sales["close_value"].isna().sum())
