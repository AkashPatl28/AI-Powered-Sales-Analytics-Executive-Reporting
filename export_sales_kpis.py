
import pyodbc
import json
from pathlib import Path
from datetime import datetime

SERVER = r".\SQLEXPRESS"  # Use your working server name
DATABASE = "SalesAnalyticsDB"

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

query = """
SELECT
    COUNT(DISTINCT opportunity_id) AS total_opportunities,
    SUM(CASE WHEN deal_stage = 'Won' THEN 1 ELSE 0 END) AS won_deals,
    SUM(CASE WHEN deal_stage = 'Lost' THEN 1 ELSE 0 END) AS lost_deals,
    SUM(CASE WHEN deal_stage = 'Engaging' THEN 1 ELSE 0 END) AS engaging_deals,
    SUM(CASE WHEN deal_stage = 'Prospecting' THEN 1 ELSE 0 END) AS prospecting_deals,
    SUM(CASE WHEN deal_stage = 'Won' THEN close_value ELSE 0 END) AS won_revenue
FROM dbo.sales_pipeline_clean;
"""

try:
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()

    total = int(row.total_opportunities or 0)
    won = int(row.won_deals or 0)
    lost = int(row.lost_deals or 0)
    engaging = int(row.engaging_deals or 0)
    prospecting = int(row.prospecting_deals or 0)
    revenue = float(row.won_revenue or 0)

    kpis = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total_opportunities": total,
        "won_deals": won,
        "lost_deals": lost,
        "engaging_opportunities": engaging,
        "prospecting_opportunities": prospecting,
        "win_rate_percent": round(won / (won + lost) * 100, 2)
            if won + lost else 0,
        "won_revenue": revenue,
        "average_won_deal_value": round(revenue / won, 2)
            if won else 0,
        "currency": "Unconfirmed"
    }

    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    output_file = PROJECT_ROOT / "data" / "sales_kpis.json"

    output_file.write_text(
        json.dumps(kpis, indent=4),
        encoding="utf-8"
    )

    print("KPIs exported successfully!")
    print("File:", output_file)
    print(json.dumps(kpis, indent=4))

except Exception as error:
    print("Export failed:")
    print(error)
