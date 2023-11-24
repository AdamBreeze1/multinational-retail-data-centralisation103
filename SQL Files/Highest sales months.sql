-- Which month has the highest sales?

SELECT 
	ROUND(SUM(CAST(dim_products.product_price * orders_table.product_quantity AS NUMERIC)), 2) AS total_sales,
	dim_date_time.month
FROM orders_table
JOIN dim_products ON orders_table.product_code = dim_products.product_code
JOIN dim_date_time ON orders_table.date_uuid = dim_date_time.date_uuid
GROUP BY dim_date_time.month
ORDER BY total_sales DESC
LIMIT 6;
