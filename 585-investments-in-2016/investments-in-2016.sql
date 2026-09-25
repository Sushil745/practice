# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016 
FROM (
    SELECT 
        tiv_2016, 
        COUNT(*) OVER(PARTITION BY tiv_2015) AS cnt_tiv_2015, 
        COUNT(*) OVER(PARTITION BY lat, lon) AS cnt_lat_lon 
    FROM Insurance
) sub 
WHERE cnt_tiv_2015 > 1 AND cnt_lat_lon = 1;
