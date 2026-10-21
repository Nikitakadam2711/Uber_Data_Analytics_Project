SELECT COUNT(*) AS total_rides
FROM rides;

SELECT AVG(fare_amount) AS average_fare
FROM rides;

SELECT MAX(fare_amount) AS max_fare
FROM rides;

SELECT MIN(fare_amount) AS min_fare
FROM rides;

SELECT SUM(fare_amount) AS total_revenue
FROM rides;

SELECT
strftime('%H', pickup_datetime) AS hour,
COUNT(*) AS total_rides
FROM rides
GROUP BY hour
ORDER BY total_rides DESC;

SELECT
strftime('%m', pickup_datetime) AS month,
SUM(fare_amount) AS revenue
FROM rides
GROUP BY month;