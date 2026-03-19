#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <unistd.h>

// This struct represents your data packet
typedef struct {
    char device_id[10];
    float temperature;
    float voltage;
    int error_code;
} SensorPacket;

int main() {
    srand(time(NULL));
    SensorPacket mySensor = {"PUMP_01", 22.5, 3.3, 0};

    printf("Starting C-to-SQL Bridge Emulator...\n");
    printf("Format: DEVICE_ID,TEMP,VOLT,ERROR\n");

    while(1) {
        // Simulate sensor fluctuations
        mySensor.temperature = 20.0 + (rand() % 600) / 10.0;
        mySensor.voltage = 3.0 + (rand() % 5) / 10.0;
        mySensor.error_code = (mySensor.temperature > 75.0) ? 404 : 0;

        // Print to STDOUT so Python can read it
        printf("%s,%.2f,%.2f,%d\n", 
               mySensor.device_id, 
               mySensor.temperature, 
               mySensor.voltage, 
               mySensor.error_code);
        
        fflush(stdout); // Ensure data is sent immediately
        sleep(2);       // Wait 2 seconds
    }
    return 0;
}