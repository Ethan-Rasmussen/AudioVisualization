import RawSound
import multiThreading

# Acquire 4 times using the sensor_threading module
times = sensor_threading.acquire_times()

# Create an object of type RawSound
sound = RawSound.RawSound(times[0], times[1], times[2], times[3], 0.0, 0.0, 0.0)

# Save the sound to a datafile
filename = "sound_data.txt"
sound.SaveSound(filename)
