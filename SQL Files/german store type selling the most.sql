-- What German store type is selling the most?

SELECT
	ROUND(SUM(CAST(dim_products.product_price * orders_table.product_quantity AS NUMERIC)), 2) AS total_sales,
	store_type,
	country_code
FROM orders_table
JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
JOIN dim_products ON orders_table.product_code = dim_products.product_code
WHERE country_code = 'DE'
GROUP BY store_type, country_code
ORDER BY total_sales DESC;
