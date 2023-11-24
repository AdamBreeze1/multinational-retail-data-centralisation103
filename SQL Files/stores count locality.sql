-- Count how many stores are in each locality

SELECT 
	locality,
	COUNT(locality) AS total_locality_stores_count
FROM dim_store_details
GROUP BY locality
HAVING COUNT(locality) >= 10
ORDER BY total_locality_stores_count DESC;
