import sqlite3

# Connect to the database (it creates the file if it doesn't exist)
conn = sqlite3.connect('sensor_data.db')
cursor = conn.cursor()

# Create a table that looks like a firmware data packet
cursor.execute('''
    CREATE TABLE IF NOT EXISTS telemetry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        temperature REAL,
        voltage REAL,
        error_code INTEGER
    )
''')


# Insert a "dummy" sensor reading
# cursor.execute('''
#     INSERT INTO telemetry (device_id, temperature, voltage, error_code)
#     VALUES ('DEV_001', 24.5, 3.3, 0)
# ''')

# conn.commit()

# cursor.execute("SELECT * FROM telemetry")
# for row in cursor.fetchall():
#     print(row)
    

# Create a Metadata table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS device_info (
        device_id TEXT PRIMARY KEY,
        location TEXT,
        firmware_rev TEXT,
        install_date DATE
    )
''')

# Insert details for the devices we used in our generator
devices_metadata = [
    ('PUMP_01', 'Basement-Zone-A', 'v1.0.2', '2025-01-15'),
    ('PUMP_02', 'Roof-Top-North', 'v1.0.4', '2025-02-10'),
    ('TURBINE_A', 'Main-Floor', 'v2.1.0', '2024-11-20')
]

cursor.executemany('''INSERT OR IGNORE INTO device_info VALUES
                   (?, ?, ?, ?)''', devices_metadata)



conn.commit()
conn.close()
print("Database and tables are created successfully!")