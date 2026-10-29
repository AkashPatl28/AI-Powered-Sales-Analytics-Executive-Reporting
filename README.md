# AI-Powered Sales Analytics & Executive Reporting

An end-to-end sales analytics project that combines Python, SQL Server, Power BI, and Gemini AI to transform CRM sales data into actionable business insights and executive reporting.

## Project Overview

This project analyzes CRM sales opportunities to understand deal performance, win rates, product revenue, and sales trends. Python supports data cleaning and KPI calculations, SQL Server stores and queries structured data, Power BI presents interactive dashboards, and Gemini AI generates an executive report from calculated KPIs.

## Tools & Technologies

- **Python:** Pandas, data cleaning, KPI calculations, Gemini API integration
- **SQL Server:** Data storage, SQL queries, aggregations, and KPI analysis
- **Power BI:** Interactive dashboards, DAX measures, data modeling, and executive insights
- **Gemini AI:** AI-assisted executive reporting
- **Git & GitHub:** Version control and project documentation

## Key Business Metrics

| Metric | Result |
|---|---:|
| Total opportunities | 8,800 |
| Won deals | 4,238 |
| Lost deals | 2,473 |
| Closed deals | 6,711 |
| Win rate | 63.15% |
| Total value of won deals | 10,005,534 |
| Average value per won deal | 2,360.91 |

*Note: The dataset's currency is unconfirmed, so monetary figures are presented without a currency symbol. Win rate is calculated as won deals divided by won plus lost deals.*

## Project Structure

```text
## Project Structure

```text
├── data/
│   └── sales_kpis.json
├── python/
│   ├── clean_sales_data.py
│   ├── export_sales_kpis.py
│   ├── fetch_sales_kpis.py
│   ├── generate_ai_report.py
│   ├── inspect_dataset.py
│   ├── sales_kpi_analysis.py
│   ├── sales_performance_analysis.py
│   ├── test_gemini_api.py
│   └── test_sql_connection.py
├── reports/
│   └── Executive_Sales_Performance_Report.md
├── .gitignore
├── requirements.txt
└── README.md
```

**Note:** The Power BI `.pbix` report and raw/cleaned datasets are not included in this public repository because the report contains imported data and dataset redistribution permissions have not been confirmed.
```

## Dataset

This project uses the CRM Sales Opportunities dataset for sales performance analysis.

For licensing and redistribution considerations, the raw and cleaned CSV files are excluded from this public repository.

To reproduce the analysis:

1. Obtain the dataset from its original provider, Maven Analytics, subject to its applicable terms.
2. Place the original CSV files in the `CRM+Sales+Opportunities/` folder.
3. Run the data-cleaning script to generate the files in `cleaned_data/`.
4. Configure SQL Server and follow the project workflow described above.

The dataset files are not included in this repository. KPI results and reports are provided for demonstration purposes.


## Workflow

1. **Data inspection:** Examine source files, data quality, missing values, and duplicates.
2. **Data cleaning:** Standardize text, correct sector spelling, convert date columns safely, and export cleaned tables.
3. **SQL analysis:** Query sales records and calculate business KPIs using SQL Server.
4. **Python analysis:** Calculate sales metrics and export results to JSON.
5. **Power BI reporting:** Present sales performance and executive insights through interactive report pages.
6. **AI-assisted reporting:** Use Gemini AI to generate a written executive report based on calculated KPIs.

## Data Quality Practices

- Standardized text fields and corrected the `technolgy` sector spelling to `technology`.
- Converted date columns using safe parsing.
- Preserved missing values instead of inventing dates or deal values.
- Checked opportunity identifiers for duplicates.

## How to Run

1. Install Python 3.11 or a compatible Python version.
2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Obtain the source dataset from its original provider and place the CSV files in `CRM+Sales+Opportunities/`, following the expected filenames in the scripts.
4. Configure SQL Server and create or import the required cleaned tables.
5. Update the SQL Server instance name in the relevant scripts if necessary.
6. Run the data-cleaning and KPI scripts from the project setup described in the code.
7. Open the Power BI report in Power BI Desktop.

### Gemini API Configuration

To generate the AI-assisted report, configure your Gemini API key as an environment variable named `GEMINI_API_KEY`. Never commit API keys or other credentials to GitHub.

## Limitations

- The analysis describes the supplied dataset and does not guarantee future sales performance.
- Currency is not confirmed in the source data.
- AI-generated commentary should be reviewed for accuracy before being used for business decisions.
- Data availability and missing values can affect interpretation.

## Author

**Akash Patil**

GitHub: (https://github.com/AkashPatl28)

LinkedIn: (https://linkedin.com/in/akash-patil-ap2842004)
