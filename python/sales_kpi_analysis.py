
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
folder = PROJECT_ROOT / "CRM+Sales+Opportunities"
df = pd.read_csv(folder / "sales_pipeline.csv")

# Count opportunities by stage
total = len(df)
won = (df["deal_stage"] == "Won").sum()
lost = (df["deal_stage"] == "Lost").sum()
engaging = (df["deal_stage"] == "Engaging").sum()
prospecting = (df["deal_stage"] == "Prospecting").sum()

# Revenue from won deals only
won_deals = df[df["deal_stage"] == "Won"]
total_revenue = won_deals["close_value"].sum()

# Calculate KPIs
closed_deals = won + lost
win_rate = won / closed_deals * 100 if closed_deals else 0
average_won_deal = (
    total_revenue / won if won else 0
)

print("\n===== SALES KPI REPORT =====")
print(f"Total Opportunities: {total:,}")
print(f"Won Deals: {won:,}")
print(f"Lost Deals: {lost:,}")
print(f"Engaging Opportunities: {engaging:,}")
print(f"Prospecting Opportunities: {prospecting:,}")
print(f"Closed Deals: {closed_deals:,}")
print(f"Win Rate: {win_rate:.2f}%")
print(f"Total Won Deal Value: {total_revenue:,.2f}")
print(f"Average Won Deal Value: {average_won_deal:,.2f}")
