import csv
import time

def trigger_sensors():
    # Read sensor trigger times from CSV file
    with open('sensor_times.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        sensor_times = list(reader)
        
    # Convert times to float and start timer
    times = [float(sensor_times[i][0]) for i in range(len(sensor_times))]
    start_time = time.time()
    
    # Wait for sensor triggers
    while True:
        # Read sensor values from CSV file
        csvfile.seek(0) # reset the file pointer to the beginning
        sensor_values = list(reader)
        
        # Check if any sensor has been triggered
        for i in range(len(sensor_times)):
            if sensor_values[i][1] == '1':
                # Calculate time elapsed since trigger and create RawSound object
                elapsed_time = time.time() - start_time - times[i]
                raw_sound = RawSound(times, -1, -1, -1)
                
                # Do something with the RawSound object, such as store it in a list or print its data
                print(f"RawSound {i+1}:")
                print(f"  times: {raw_sound.times}")
                print(f"  a: {raw_sound.a}")
                print(f"  b: {raw_sound.b}")
                print(f"  c: {raw_sound.c}")
