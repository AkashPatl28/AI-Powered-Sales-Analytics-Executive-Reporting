
import os
import json
from pathlib import Path
from google import genai

# Project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

KPI_FILE = PROJECT_ROOT / "data" / "sales_kpis.json"
REPORT_FILE = PROJECT_ROOT / "reports" / "Executive_Sales_Performance_Report.md"

# Connect to Gemini
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. Configure it in PowerShell first."
    )

client = genai.Client(api_key=api_key)

# Load verified KPIs
with open(KPI_FILE, "r", encoding="utf-8") as file:
    kpis = json.load(file)

# Generate an evidence-based report
prompt = f"""
You are a business intelligence analyst preparing an executive sales report.

Use only the verified KPI data provided below.

VERIFIED DATA:
{json.dumps(kpis, indent=2)}

Write a professional report in Markdown with these sections:
1. Executive Summary
2. Key Performance Indicators
3. Sales Performance Findings
4. Risks and Opportunities
5. Recommended Actions
6. Data Limitations

Rules:
- Do not invent figures, trends, causes, or explanations.
- Clearly distinguish verified findings from hypotheses.
- State that the currency is unconfirmed; do not assume INR or USD.
- Explain the win rate using the available won and lost deal counts.
- Make recommendations that can be supported by the supplied data.
- If the JSON does not contain enough information for a section,
  explicitly state what additional data is needed.
- Keep the report concise and suitable for business executives.
"""

print("Sending KPI data to Gemini...")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
)

if not response.text:
    raise RuntimeError("Gemini returned an empty report.")

REPORT_FILE.write_text(response.text, encoding="utf-8")

print("\nReport generated successfully!")
print(f"Saved to: {REPORT_FILE}")
