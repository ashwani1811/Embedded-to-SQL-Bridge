import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect('sensor_data.db')
cursor = conn.cursor()

devices = ['PUMP_01', 'PUMP_02', 'TURBINE_A']

print("Generating simulated IoT data...")

for i in range(100):
    device = random.choice(devices)
    # Simulate a timestamp over the last 24 hours
    time_offset = random.randint(0, 1440) 
    timestamp = (datetime.now() - timedelta(minutes=time_offset)).strftime('%Y-%m-%d %H:%M:%S')
    
    # Simulate realistic sensor fluctuations
    temp = round(random.uniform(20.0, 85.0), 2)
    volts = round(random.uniform(3.1, 3.5), 2)
    
    # Simulate an occasional error (e.g., error 404 if temp > 80)
    error = 404 if temp > 80 else 0

    cursor.execute('''
        INSERT INTO telemetry (device_id, timestamp, temperature, voltage, error_code)
        VALUES (?, ?, ?, ?, ?)
    ''', (device, timestamp, temp, volts, error))

conn.commit()
conn.close()
print("100 rows of telemetry data added to sensor_data.db!")