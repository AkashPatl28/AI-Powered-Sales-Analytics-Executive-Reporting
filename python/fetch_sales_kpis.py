
import pyodbc

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

        total = row.total_opportunities
        won = row.won_deals
        lost = row.lost_deals
        engaging = row.engaging_deals
        prospecting = row.prospecting_deals
        revenue = row.won_revenue or 0

        win_rate = won / (won + lost) * 100 if won + lost else 0
        average_deal_value = revenue / won if won else 0

        print("\nSALES KPI REPORT")
        print("-" * 35)
        print(f"Total Opportunities: {total:,}")
        print(f"Won Deals: {won:,}")
        print(f"Lost Deals: {lost:,}")
        print(f"Engaging Opportunities: {engaging:,}")
        print(f"Prospecting Opportunities: {prospecting:,}")
        print(f"Win Rate: {win_rate:.2f}%")
        print(f"Won Revenue: {revenue:,.2f}")
        print(f"Average Won Deal Value: {average_deal_value:,.2f}")

except Exception as error:
    print("Unable to fetch KPIs:")
    print(error)
