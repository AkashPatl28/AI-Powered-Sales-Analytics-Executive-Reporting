
import pyodbc

# Update this if your SSMS server name is different
SERVER = r".\SQLEXPRESS"
DATABASE = "SalesAnalyticsDB"

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

try:
    with pyodbc.connect(connection_string, timeout=5) as conn:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM dbo.sales_pipeline_clean"
        )

        total_rows = cursor.fetchone()[0]

        print("SQL Server connection successful!")
        print("Database:", DATABASE)
        print("Sales records:", total_rows)

except Exception as error:
    print("Connection failed:")
    print(error)
