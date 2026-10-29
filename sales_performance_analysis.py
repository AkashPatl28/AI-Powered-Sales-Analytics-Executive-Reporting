
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
folder = PROJECT_ROOT / "CRM+Sales+Opportunities"

# Load the required files
sales = pd.read_csv(folder / "sales_pipeline.csv")
products = pd.read_csv(folder / "products.csv")
teams = pd.read_csv(folder / "sales_teams.csv")
accounts = pd.read_csv(folder / "accounts.csv")

# Convert date columns
sales["engage_date"] = pd.to_datetime(
    sales["engage_date"], errors="coerce"
)
sales["close_date"] = pd.to_datetime(
    sales["close_date"], errors="coerce"
)

# Only Won deals contribute to won revenue
won = sales[sales["deal_stage"] == "Won"].copy()

print("\n===== 1. REVENUE BY PRODUCT =====")
print(
    won.groupby("product")
    .agg(
        Deals_Won=("opportunity_id", "count"),
        Revenue=("close_value", "sum"),
        Average_Deal_Value=("close_value", "mean")
    )
    .sort_values("Revenue", ascending=False)
    .round(2)
    .to_string()
)

print("\n===== 2. TOP 10 SALES AGENTS =====")
print(
    won.groupby("sales_agent")
    .agg(
        Deals_Won=("opportunity_id", "count"),
        Revenue=("close_value", "sum")
    )
    .sort_values("Revenue", ascending=False)
    .head(10)
    .round(2)
    .to_string()
)

print("\n===== 3. REVENUE BY REGION =====")
sales_with_team = won.merge(
    teams,
    on="sales_agent",
    how="left",
    validate="many_to_one"
)

print(
    sales_with_team.groupby("regional_office")
    .agg(
        Deals_Won=("opportunity_id", "count"),
        Revenue=("close_value", "sum")
    )
    .sort_values("Revenue", ascending=False)
    .round(2)
    .to_string()
)

print("\n===== 4. MONTHLY REVENUE =====")
monthly = (
    won.dropna(subset=["close_date"])
    .assign(
        Month=lambda x: x["close_date"].dt.to_period("M").astype(str)
    )
    .groupby("Month")
    .agg(
        Deals_Won=("opportunity_id", "count"),
        Revenue=("close_value", "sum")
    )
    .sort_index()
)

print(monthly.to_string())

print("\n===== 5. REVENUE BY ACCOUNT SECTOR =====")
sales_with_accounts = won.merge(
    accounts[["account", "sector"]],
    on="account",
    how="left",
    validate="many_to_one"
)

print(
    sales_with_accounts.groupby(
        "sector", dropna=False
    ).agg(
        Deals_Won=("opportunity_id", "count"),
        Revenue=("close_value", "sum")
    )
    .sort_values("Revenue", ascending=False)
    .round(2)
    .to_string()
)
