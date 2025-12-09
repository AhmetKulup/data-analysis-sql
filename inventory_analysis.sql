-- Identify products with low stock
SELECT 
    product_id,
    product_name,
    stock_quantity,
    reorder_level
FROM inventory
WHERE stock_quantity < reorder_level
ORDER BY stock_quantity ASC;

-- Top-selling products by category
SELECT 
    category,
    product_id,
    SUM(quantity_sold) AS total_sold
FROM sales
GROUP BY category, product_id
ORDER BY total_sold DESC;
