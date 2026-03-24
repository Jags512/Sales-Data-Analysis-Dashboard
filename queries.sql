-- Total Revenue
SELECT SUM(quantity * price) AS total_revenue FROM sales_data;

-- Revenue by Region
SELECT region, SUM(quantity * price) AS revenue
FROM sales_data
GROUP BY region;

-- Top Product
SELECT product, SUM(quantity * price) AS revenue
FROM sales_data
GROUP BY product
ORDER BY revenue DESC
LIMIT 1;
