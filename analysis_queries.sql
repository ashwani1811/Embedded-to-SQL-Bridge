-- This SQL script contains various queries to analyze the telemetry data collected from devices.

-- Analysis Queries for Telemetry Data
SELECT * FROM telemetry;

-- Calculate average temperature and voltage for each device
SELECT 
    device_id, 
    MAX(temperature) AS max_temp, 
    MIN(temperature) AS min_temp, 
    AVG(temperature) AS avg_temp
FROM telemetry
GROUP BY device_id;

-- Find all records where the error code is not zero and order by temperature
SELECT * FROM telemetry 
WHERE error_code != 0 
ORDER BY temperature DESC;


-- Join telemetry data with device information to get more context
-- This query retrieves the timestamp, device ID, location, and temperature 
-- for each telemetry record by joining the telemetry table with the device_info 
-- table on the device_id field.
SELECT 
    telemetry.timestamp,
    telemetry.device_id,
    device_info.location,
    telemetry.temperature
FROM telemetry
INNER JOIN device_info 
    ON telemetry.device_id = device_info.device_id;

-- Find all devices that have reported an error and their corresponding 
-- firmware version is old which is 'v1.0.2'. This query joins the telemetry 
-- table with the device_info
SELECT 
    t.device_id, 
    t.error_code, 
    i.firmware_rev,
    i.location
FROM telemetry AS t
JOIN device_info AS i ON t.device_id = i.device_id
WHERE t.error_code != 0 AND i.firmware_rev = 'v1.0.2';