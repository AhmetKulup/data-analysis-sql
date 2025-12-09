-- Monthly sales summary
SELECT 
    DATE_TRUNC('month', sale_date) AS month,
    SUM(quantity_sold) AS total_units_sold,
    SUM(total_amount) AS total_revenue
FROM sales
GROUP BY DATE_TRUNC('month', sale_date)
ORDER BY month;

-- Top 5 customers by revenue
SELECT 
    customer_id,
    SUM(total_amount) AS total_revenue
FROM sales
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 5;

-- Best-selling product categories
SELECT 
    category,
    SUM(quantity_sold) AS total_units_sold
FROM sales
GROUP BY category
ORDER BY total_units_sold DESC;

-- Average order value per customer
SELECT 
    customer_id,
    AVG(total_amount) AS avg_order_value
FROM sales
GROUP BY customer_id
ORDER BY avg_order_value DESC;
