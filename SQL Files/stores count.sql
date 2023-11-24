-- Count how many stores are in each country

SELECT 
	country_code,
	COUNT(country_code) AS total_stores_count
FROM dim_store_details
GROUP BY country_code
ORDER BY total_stores_count DESC;
