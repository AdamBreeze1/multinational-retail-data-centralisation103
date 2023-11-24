-- What percentage of sales come through each store type?

WITH total_sales_cte AS (
    SELECT
        store_type,
        ROUND(SUM(CAST(dim_products.product_price * orders_table.product_quantity AS NUMERIC)), 2) AS total_sales
    FROM
        orders_table
    JOIN
        dim_store_details ON orders_table.store_code = dim_store_details.store_code
    JOIN
        dim_products ON orders_table.product_code = dim_products.product_code
    GROUP BY
        store_type
)

SELECT
    store_type,
    total_sales,
    ROUND((total_sales / (SELECT SUM(total_sales) FROM total_sales_cte)) * 100, 2) AS "percentage_total(%)"
FROM
    total_sales_cte
ORDER BY
    total_sales DESC;