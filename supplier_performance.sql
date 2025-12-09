-- Supplier on-time delivery rate
SELECT 
    supplier_id,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN delivery_date <= expected_delivery_date THEN 1 ELSE 0 END) AS on_time_deliveries,
    ROUND(
        SUM(CASE WHEN delivery_date <= expected_delivery_date THEN 1 ELSE 0 END)::numeric 
        / COUNT(*) * 100, 
    2) AS on_time_rate_percentage
FROM purchase_orders
GROUP BY supplier_id
ORDER BY on_time_rate_percentage DESC;


-- Average delivery delay by supplier
SELECT 
    supplier_id,
    AVG(EXTRACT(DAY FROM (delivery_date - expected_delivery_date))) AS avg_delay_days
FROM purchase_orders
WHERE delivery_date > expected_delivery_date
GROUP BY supplier_id
ORDER BY avg_delay_days ASC;


-- Supplier cost comparison (average unit cost per product)
SELECT 
    supplier_id,
    product_id,
    AVG(unit_cost) AS avg_unit_cost
FROM purchase_orders
GROUP BY supplier_id, product_id
ORDER BY product_id, avg_unit_cost;
