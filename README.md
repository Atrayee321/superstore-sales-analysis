# 📊 Superstore Sales Analysis Dashboard

An interactive sales analytics application built with **Python, Streamlit, Pandas and Plotly**. It uses the cleaned Superstore dataset and complements the SQL and Power BI analysis included in this repository.

**Live app:** ``

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

**Atrayee Chatterjee**  
Aspiring Data Analyst | Machine Learning


