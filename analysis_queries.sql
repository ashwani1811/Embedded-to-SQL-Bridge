SELECT * FROM telemetry;

SELECT 
    device_id, 
    MAX(temperature) AS max_temp, 
    MIN(temperature) AS min_temp, 
    AVG(temperature) AS avg_temp
FROM telemetry
GROUP BY device_id;

SELECT * FROM telemetry 
WHERE error_code != 0 
ORDER BY temperature DESC;