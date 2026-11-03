# 📊 Superstore Sales Analysis Dashboard

An interactive **Sales Data Analytics Dashboard** built using Python, Streamlit, Pandas and Plotly. This project analyzes Superstore sales data to uncover business insights related to revenue, profitability, products, customers, regions and shipping performance.

🚀 **Live Application:** [Superstore Sales Analysis Dashboard](https://superstore-sales-analysis-am346gmdq9unrua9ocy2yl.streamlit.app/)

---

## 📌 Project Overview

The project combines Python-based exploratory data analysis, SQL queries and Power BI visualization to analyze sales performance and support data-driven business decisions.

The interactive Streamlit application allows users to explore sales data through dynamic filters, KPI metrics and visualizations.

## ✨ Dashboard Features

- **Key Performance Indicators:** Total Revenue, Total Profit, Total Orders, Total Customers and Average Order Value.
- **Interactive Filters:** Filter data by order date, region, category, customer segment and shipping mode.
- **Sales Trends:** Monthly revenue and profit analysis.
- **Product Performance:** Revenue by category and sub-category.
- **Regional Analysis:** Compare revenue and profitability across regions.
- **Customer Insights:** Analyze customer segments and identify top customers.
- **Top 10 Analysis:** Identify the highest-revenue products and customers.
- **Profitability Analysis:** Identify products generating losses.
- **Shipping Analysis:** Evaluate average shipping days by shipping mode.
- **Data Export:** View filtered records and download filtered datasets as CSV.
- **Custom Dataset Upload:** Upload another compatible CSV dataset for analysis.

## 📂 Repository Structure

All project files are stored directly in the main repository.

```text
Sales-Data-Analysis/
│
├── app.py
├── requirements.txt
├── README.md
│
├── Cleaned_Superstore_Sales.csv
├── Sales_Analysis.sql
└── Sales_performance_dashboard.pbix
```

## 📊 Dataset

**File:** `Cleaned_Superstore_Sales.csv`

- 9,994 records
- 27 columns
- Contains order dates, shipping information, customer details, product categories, sales, quantity, discounts, profit and shipping days.

The cleaned dataset is used as the primary data source for the Streamlit dashboard.

## 🗄️ SQL Analysis

**File:** `Sales_Analysis.sql`

SQL queries are included to perform business-oriented analysis, including:

- Sales and profit KPIs
- Category and sub-category performance
- Regional sales analysis
- Top customers and products
- Loss-making product identification
- Yearly and monthly sales trends
- Discount and profit margin analysis
- Year-over-year growth analysis

## 📈 Power BI Dashboard

**File:** `Sales_performance_dashboard.pbix`

An interactive Power BI dashboard created to visualize sales performance and business metrics.

Open the `.pbix` file using **Microsoft Power BI Desktop** to explore the dashboard.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data analysis and application development |
| Pandas | Data cleaning and manipulation |
| Streamlit | Interactive dashboard development |
| Plotly | Data visualization |
| SQL / MySQL | Database querying and analysis |
| Microsoft Power BI | Business intelligence and reporting |
| Git & GitHub | Version control and project hosting |

## 🚀 Run Locally

1. Clone or download this repository.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## ⚙️ Requirements

The project uses:

```text
streamlit
pandas
plotly
```

## 📝 Notes

- The application loads `Cleaned_Superstore_Sales.csv` directly from the main repository.
- The optional CSV uploader expects compatible column names and data types.
- The SQL file is provided for database analysis.
- The Power BI dashboard is included as a `.pbix` project artifact and is not rendered inside Streamlit.
- The live application is hosted using Streamlit Community Cloud.

---

## 👩‍💻 Project

**Superstore Sales Analysis Dashboard**

Built with Python, SQL, Power BI and Streamlit.

🔗 **Live Demo:** [Open Dashboard](https://superstore-sales-analysis-am346gmdq9unrua9ocy2yl.streamlit.app/)

🔗 **Source Code:** [GitHub Repository](https://github.com/)



## Author

**Atrayee Chatterjee**  
Aspiring Data Analyst | Machine Learning


