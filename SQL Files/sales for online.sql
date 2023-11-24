-- How many sales are coming from online?

SELECT
	COUNT(orders_table.index) AS number_of_sales,
	SUM(orders_table.product_quantity) AS product_quantity_count,
    CASE 
        WHEN dim_store_details.store_type IN ('Web Portal') THEN 'Web'
        WHEN dim_store_details.store_type IN ('Super Store', 'Local', 'Outlet', 'Mall Kiosk') THEN 'Offline'
        ELSE 'Unknown'
    END AS location
FROM orders_table
JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
GROUP BY location;


