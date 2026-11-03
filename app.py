
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ---------------- Page configuration ----------------
st.set_page_config(
    page_title="Superstore Sales Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- File paths ----------------
BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "Cleaned_Superstore_Sales.csv"
SQL_PATH = BASE_DIR / "Sales_Analysis.sql"
POWERBI_PATH = BASE_DIR / "Sales_performance_dashboard.pbix"


# ---------------- Styling ----------------
st.markdown("""
<style>

/* Dashboard background */
.stApp {
    background-color: #f7f9fc;
}

/* Headings */
h1, h2, h3, h4 {
    color: #183153 !important;
}

/* General text */
p, label, li {
    color: #334155;
}

/* KPI cards */
[data-testid="stMetric"] {
    background-color: #ffffff !important;
    border: 1px solid #dce3ed;
    padding: 18px;
    border-radius: 12px;
}

/* KPI labels */
[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] * {
    color: #52647a !important;
}

/* KPI numbers */
[data-testid="stMetricValue"],
[data-testid="stMetricValue"] * {
    color: #183153 !important;
}

/* KPI delta values */
[data-testid="stMetricDelta"],
[data-testid="stMetricDelta"] * {
    color: #16803c !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #eef2f7;
}

[data-testid="stSidebar"] * {
    color: #183153;
}

/* Captions */
.stCaption,
[data-testid="stCaption"] {
    color: #64748b !important;
}

</style>
""", unsafe_allow_html=True)


# ---------------- Data loading ----------------
REQUIRED_COLUMNS = [
    "Order Date", "Sales", "Profit", "Order ID",
    "Customer ID", "Region", "Category", "Segment",
    "Ship Mode", "Sub-Category", "Product Name",
    "Customer Name", "Quantity", "Shipping Days"
]

@st.cache_data
def load_data(path):
    data = pd.read_csv(path)

    missing = [col for col in REQUIRED_COLUMNS if col not in data.columns]

    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    data["Order Date"] = pd.to_datetime(
        data["Order Date"], errors="coerce"
    )

    if "Ship Date" in data.columns:
        data["Ship Date"] = pd.to_datetime(
            data["Ship Date"], errors="coerce"
        )

    for col in ["Sales", "Profit", "Quantity", "Discount", "Shipping Days"]:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")

    data = data.dropna(subset=["Order Date", "Sales", "Profit"])

    return data


@st.cache_data
def load_uploaded_data(uploaded_file):
    data = pd.read_csv(uploaded_file)

    data["Order Date"] = pd.to_datetime(
        data["Order Date"], errors="coerce"
    )

    if "Ship Date" in data.columns:
        data["Ship Date"] = pd.to_datetime(
            data["Ship Date"], errors="coerce"
        )

    for col in ["Sales", "Profit", "Quantity", "Discount", "Shipping Days"]:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")

    return data.dropna(subset=["Order Date", "Sales", "Profit"])


# ---------------- Load dataset ----------------
try:
    if not DATA_PATH.exists():
        st.error(
            "Dataset not found. Please ensure "
            "'Cleaned_Superstore_Sales.csv' is uploaded "
            "in the main GitHub repository alongside app.py."
        )
        st.stop()

    df = load_data(str(DATA_PATH))

except Exception as exc:
    st.error(f"Error loading dataset: {exc}")
    st.stop()


# ---------------- Sidebar filters ----------------
st.sidebar.title("📊 Sales Analytics")
st.sidebar.caption("Explore and filter Superstore sales data")

uploaded = st.sidebar.file_uploader(
    "Optional: Upload another CSV",
    type=["csv"]
)

if uploaded is not None:
    try:
        df = load_uploaded_data(uploaded)
    except Exception as exc:
        st.sidebar.error(f"Could not read uploaded CSV: {exc}")

# Date filter
min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

date_range = st.sidebar.date_input(
    "Order date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date


def options_for(column):
    return sorted(df[column].dropna().astype(str).unique().tolist())


regions = st.sidebar.multiselect(
    "Region", options_for("Region"), default=options_for("Region")
)

categories = st.sidebar.multiselect(
    "Category", options_for("Category"), default=options_for("Category")
)

segments = st.sidebar.multiselect(
    "Customer segment", options_for("Segment"), default=options_for("Segment")
)

ship_modes = st.sidebar.multiselect(
    "Ship mode", options_for("Ship Mode"), default=options_for("Ship Mode")
)

filtered = df[
    (df["Order Date"].dt.date >= start_date) &
    (df["Order Date"].dt.date <= end_date) &
    (df["Region"].astype(str).isin(regions)) &
    (df["Category"].astype(str).isin(categories)) &
    (df["Segment"].astype(str).isin(segments)) &
    (df["Ship Mode"].astype(str).isin(ship_modes))
].copy()


# ---------------- Header ----------------
st.title("📈 Superstore Sales Analysis")

st.markdown(
    "An interactive business intelligence dashboard for exploring "
    "sales, profitability, customers and products."
)

st.caption(f"Showing {len(filtered):,} of {len(df):,} records")

if filtered.empty:
    st.warning(
        "No records match the selected filters. "
        "Change or clear some filters in the sidebar."
    )
    st.stop()


# ---------------- KPI calculations ----------------
revenue = filtered["Sales"].sum()
profit = filtered["Profit"].sum()
orders = filtered["Order ID"].nunique()
customers = filtered["Customer ID"].nunique()

aov = revenue / orders if orders else 0
margin = (profit / revenue * 100) if revenue else 0

k1, k2, k3, k4, k5 = st.columns(5)

k1.metric("Total Revenue", f"${revenue:,.2f}")
k2.metric("Total Profit", f"${profit:,.2f}")
k3.metric("Total Orders", f"{orders:,}")
k4.metric("Total Customers", f"{customers:,}")
k5.metric("Average Order Value", f"${aov:,.2f}")

st.divider()


# ---------------- Trends ----------------
st.subheader("Sales and Profit Trends")

trend = filtered.set_index("Order Date").resample("MS").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).reset_index()

left, right = st.columns(2)

with left:
    fig = px.line(
        trend,
        x="Order Date",
        y="Sales",
        markers=True,
        title="Monthly Revenue",
        labels={"Order Date": "Month", "Sales": "Revenue ($)"}
    )
    fig.update_layout(hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)

with right:
    fig = px.line(
        trend,
        x="Order Date",
        y="Profit",
        markers=True,
        title="Monthly Profit",
        labels={"Order Date": "Month", "Profit": "Profit ($)"}
    )
    fig.update_layout(hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)


# ---------------- Category analysis ----------------
st.subheader("Product Performance")

cat = filtered.groupby("Category", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
)

subcat = filtered.groupby("Sub-Category", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).sort_values("Sales", ascending=True)

left, right = st.columns(2)

with left:
    fig = px.bar(
        cat,
        x="Category",
        y="Sales",
        color="Category",
        title="Revenue by Category",
        text_auto=".2s"
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    fig = px.bar(
        subcat,
        x="Sales",
        y="Sub-Category",
        orientation="h",
        color="Profit",
        color_continuous_scale="RdYlGn",
        title="Sub-category Revenue and Profit"
    )
    st.plotly_chart(fig, use_container_width=True)


# ---------------- Regional and segment analysis ----------------
st.subheader("Geographic and Customer Analysis")

region_data = filtered.groupby("Region", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).sort_values("Sales", ascending=False)

segment_data = filtered.groupby("Segment", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Customers=("Customer ID", "nunique")
)

left, right = st.columns(2)

with left:
    fig = px.bar(
        region_data,
        x="Region",
        y="Sales",
        color="Profit",
        title="Revenue by Region",
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    fig = px.pie(
        segment_data,
        names="Segment",
        values="Sales",
        title="Revenue Share by Customer Segment",
        hole=0.45
    )
    st.plotly_chart(fig, use_container_width=True)


# ---------------- Products and customers ----------------
st.subheader("Top Products and Customers")

product_data = filtered.groupby("Product Name", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
)

top_products = product_data.nlargest(10, "Sales")

customer_data = filtered.groupby("Customer Name", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
)

top_customers = customer_data.nlargest(10, "Sales")

left, right = st.columns(2)

with left:
    st.markdown("**Top 10 Products by Revenue**")
    st.dataframe(
        top_products.style.format({
            "Sales": "${:,.2f}",
            "Profit": "${:,.2f}"
        }),
        use_container_width=True,
        hide_index=True
    )

with right:
    st.markdown("**Top 10 Customers by Revenue**")
    st.dataframe(
        top_customers.style.format({
            "Sales": "${:,.2f}",
            "Profit": "${:,.2f}"
        }),
        use_container_width=True,
        hide_index=True
    )


# ---------------- Profitability and shipping ----------------
st.subheader("Profitability and Shipping")

loss_products = product_data[
    product_data["Profit"] < 0
].sort_values("Profit").head(10)

ship_data = filtered.groupby("Ship Mode", as_index=False).agg(
    Orders=("Order ID", "nunique"),
    Average_Shipping_Days=("Shipping Days", "mean")
)

left, right = st.columns(2)

with left:
    st.markdown("**Products with the Largest Losses**")

    if loss_products.empty:
        st.success("No loss-making products in the current filter selection.")
    else:
        st.dataframe(
            loss_products.style.format({
                "Sales": "${:,.2f}",
                "Profit": "${:,.2f}"
            }),
            use_container_width=True,
            hide_index=True
        )

with right:
    fig = px.bar(
        ship_data,
        x="Ship Mode",
        y="Average_Shipping_Days",
        title="Average Shipping Days by Ship Mode",
        text_auto=".1f"
    )
    st.plotly_chart(fig, use_container_width=True)


# ---------------- Detailed data and export ----------------
with st.expander("View filtered sales records"):
    st.dataframe(filtered, use_container_width=True, hide_index=True)

    csv_bytes = filtered.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download filtered data as CSV",
        data=csv_bytes,
        file_name="filtered_superstore_sales.csv",
        mime="text/csv"
    )


# ---------------- Project resources ----------------
st.divider()
st.subheader("Project Resources")

col1, col2 = st.columns(2)

with col1:
    if SQL_PATH.exists():
        st.download_button(
            "⬇️ Download SQL Analysis",
            data=SQL_PATH.read_bytes(),
            file_name="Sales_Analysis.sql",
            mime="text/plain"
        )
    else:
        st.info("SQL file is not available in the repository.")

with col2:
    if POWERBI_PATH.exists():
        st.download_button(
            "⬇️ Download Power BI Dashboard",
            data=POWERBI_PATH.read_bytes(),
            file_name="Sales_performance_dashboard.pbix",
            mime="application/octet-stream"
        )
    else:
        st.info("Power BI dashboard is not available in the repository.")


# ---------------- Summary ----------------
st.divider()
st.subheader("Quick Performance Summary")

st.write(
    f"The selected data contains **${revenue:,.2f}** in revenue and "
    f"**${profit:,.2f}** in profit, with a profit margin of **{margin:.2f}%**. "
    f"It includes **{orders:,} distinct orders** from "
    f"**{customers:,} customers**."
)

st.caption(
    "Built with Python, Streamlit, Pandas and Plotly | "
    "Superstore Sales Analysis"
)

