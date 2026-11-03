USE Sales_Data_Analysis;

SELECT * FROM superstore LIMIT 10;

SELECT COUNT(*) AS Total_Records
FROM superstore;
SELECT SUM(Sales) AS Total_Revenue
FROM superstore;
SELECT SUM(Profit) AS Total_Profit
FROM superstore;
SELECT COUNT(DISTINCT `Order ID`) AS Total_Orders
FROM superstore;
SELECT COUNT(DISTINCT `Customer ID`) AS Total_Customers
FROM superstore;
SELECT
    SUM(Sales) /
    COUNT(DISTINCT `Order ID`) AS Average_Order_Value
FROM superstore;
SELECT
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Sales DESC;
SELECT
    `Sub-Category`,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY `Sub-Category`
ORDER BY Total_Sales DESC;
SELECT
    Region,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;
SELECT
    `Customer Name`,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10;
SELECT
    `Product Name`,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 10;
SELECT
    `Product Name`,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY `Product Name`
HAVING SUM(Profit) < 0
ORDER BY Total_Profit ASC;
SELECT
    YEAR(`Order Date`) AS Sales_Year,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY YEAR(`Order Date`)
ORDER BY Sales_Year;
SELECT
    DATE_FORMAT(`Order Date`, '%Y-%m') AS Sales_Month,
    SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY DATE_FORMAT(`Order Date`, '%Y-%m')
ORDER BY Sales_Month;
SELECT
    Discount,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    AVG(Profit) AS Average_Profit
FROM superstore
GROUP BY Discount
ORDER BY Discount;
SELECT
    Segment,
    COUNT(DISTINCT `Customer ID`) AS Customers,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Segment
ORDER BY Total_Sales DESC;
SELECT
    State,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY State
ORDER BY Total_Sales DESC
LIMIT 10;
SELECT
    `Ship Mode`,
    COUNT(DISTINCT `Order ID`) AS Total_Orders,
    AVG(`Shipping Days`) AS Average_Shipping_Days
FROM superstore
GROUP BY `Ship Mode`
ORDER BY Total_Orders DESC;
SELECT
    Category,
    SUM(Sales) AS Revenue,
    SUM(Profit) AS Profit,
    ROUND(
        SUM(Profit) / NULLIF(SUM(Sales), 0) * 100,
        2
    ) AS Profit_Margin_Percentage
FROM superstore
GROUP BY Category;
WITH yearly_sales AS (
    SELECT
        YEAR(`Order Date`) AS Sales_Year,
        SUM(Sales) AS Revenue
    FROM superstore
    GROUP BY YEAR(`Order Date`)
),
growth AS (
    SELECT
        Sales_Year,
        Revenue,
        LAG(Revenue) OVER (
            ORDER BY Sales_Year
        ) AS Previous_Year_Revenue
    FROM yearly_sales
)
SELECT
    Sales_Year,
    Revenue,
    Previous_Year_Revenue,
    ROUND(
        (Revenue - Previous_Year_Revenue) /
        NULLIF(Previous_Year_Revenue, 0) * 100,
        2
    ) AS Growth_Percentage
FROM growth;
WITH yearly_sales AS (
    SELECT
        YEAR(`Order Date`) AS Sales_Year,
        SUM(Sales) AS Revenue
    FROM superstore
    GROUP BY YEAR(`Order Date`)
),
growth AS (
    SELECT
        Sales_Year,
        Revenue,
        LAG(Revenue) OVER (
            ORDER BY Sales_Year
        ) AS Previous_Year_Revenue
    FROM yearly_sales
)
SELECT
    Sales_Year,
    Revenue,
    Previous_Year_Revenue,
    ROUND(
        (Revenue - Previous_Year_Revenue) /
        NULLIF(Previous_Year_Revenue, 0) * 100,
        2
    ) AS Growth_Percentage
FROM growth;
SELECT
    `Order ID`,
    `Customer Name`,
    Category,
    Sales,
    Profit
FROM superstore
WHERE Profit < 0
ORDER BY Profit ASC;