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

conn.commit()

# cursor.execute("SELECT * FROM telemetry")
# for row in cursor.fetchall():
#     print(row)
    
conn.close()
print("Database and table created successfully!")