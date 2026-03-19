import subprocess
import sqlite3

# Connect to the database we made yesterday
conn = sqlite3.connect('sensor_data.db')
cursor = conn.cursor()

# Start the C program as a subprocess
process = subprocess.Popen(['./sensor_emulator'], stdout=subprocess.PIPE, text=True)

print("Python is now listening to the C-Emulator...")

try:
    for line in process.stdout:
        if "," in line:
            # Parse the comma-separated string from C
            parts = line.strip().split(',')
            device_id, temp, volt, err = parts
            
            try:
                # Validate that we actually have numbers before inserting
                cursor.execute('''
                    INSERT INTO telemetry (device_id, temperature, voltage, error_code)
                    VALUES (?, ?, ?, ?)
                ''', (device_id, float(temp), float(volt), int(err)))
                
                conn.commit()
                print(f"Logged to SQL: {device_id} at {temp}C")
            except ValueError:
                # This catches the "TEMP" header or any other non-numeric junk
                print(f"Skipping non-data line: {line.strip()}")

except KeyboardInterrupt:
    print("Stopping bridge...")
finally:
    process.terminate()
    conn.close()