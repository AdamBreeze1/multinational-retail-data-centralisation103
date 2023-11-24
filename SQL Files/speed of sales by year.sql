-- Speed of sales separated by year

WITH time_dif AS (
	SELECT 
		year,
		(LEAD(datetime) OVER (ORDER BY datetime)) - datetime AS actual_time_taken
	FROM dim_date_time
)

SELECT
	year,
	AVG(actual_time_taken) AS avg_actual_time_taken 
FROM time_dif
GROUP BY year
ORDER BY avg_actual_time_taken DESC
LIMIT 5;


