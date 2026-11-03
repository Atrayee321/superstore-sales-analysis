# 📊 Superstore Sales Analysis Dashboard

An interactive sales analytics application built with **Python, Streamlit, Pandas and Plotly**. It uses the cleaned Superstore dataset and complements the SQL and Power BI analysis included in this repository.

## Live application

After deployment, add your Streamlit Community Cloud URL here:

**Live app:** `https://your-app-name.streamlit.app`

## Project overview

The dashboard helps explore sales performance, profitability, product performance, customer segments, regions and shipping.

### Dashboard features

- KPI cards: revenue, profit, distinct orders, distinct customers and average order value
- Date, region, category, customer segment and ship mode filters
- Monthly revenue and profit trends
- Revenue by category and sub-category
- Regional sales and customer segment analysis
- Top 10 products and customers by revenue
- Loss-making product analysis
- Average shipping days by ship mode
- Filtered record table and CSV download
- Optional CSV upload to analyze another compatible dataset

## Repository structure

```text
superstore-sales-analysis/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── Cleaned_Superstore_Sales.csv
│
├── sql/
│   └── Sales_Analysis.sql
│
├── powerbi/
│   └── Sales_performance_dashboard.pbix
│
└── .streamlit/
    └── config.toml
```

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/superstore-sales-analysis.git
cd superstore-sales-analysis
```

### 2. Create a virtual environment (recommended)

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the application

```bash
streamlit run app.py
```

The app will open in your browser, usually at `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. Push this repository to your GitHub account.
2. Sign in at [Streamlit Community Cloud](https://share.streamlit.io/).
3. Select **Create app** and connect your GitHub repository.
4. Select the repository, branch (`main`) and main file path (`app.py`).
5. Select **Deploy**.
6. Wait for the build to finish and open the generated app URL.

No API key or secrets are required for this application.

## Dataset

`data/Cleaned_Superstore_Sales.csv` contains 9,994 records and 27 columns, including order dates, shipping information, customer details, product categories, sales, quantity, discount, profit and shipping days.

## SQL analysis

The `sql/Sales_Analysis.sql` file contains the SQL queries used for sales KPIs, category and regional analysis, top customers and products, loss-making products, yearly/monthly trends, discount analysis, profit margins and year-over-year growth.

## Power BI

The `powerbi/` folder contains the supplied Power BI dashboard (`.pbix`) file. Open it with Power BI Desktop.

## Technology stack

- Python
- Streamlit
- Pandas
- Plotly
- SQL / MySQL
- Microsoft Power BI
- Git and GitHub

## Notes

- The dashboard reads its default dataset from `data/Cleaned_Superstore_Sales.csv`.
- The optional CSV uploader expects compatible column names, including `Order Date`, `Sales`, `Profit`, `Order ID`, `Customer ID`, `Region`, `Category`, `Segment`, `Ship Mode`, `Sub-Category`, `Product Name`, `Quantity` and `Shipping Days`.
- The Power BI `.pbix` file is included as a project artifact; it is not rendered inside the Streamlit app.

## Author

**Your Name**  
Aspiring Data Analyst | Data Analytics | Machine Learning

Add your LinkedIn and GitHub profile links here.
