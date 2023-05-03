import random
import math
from RawSound import RawSound

# Define the positions of the sensors in the array (in feet)
SENSOR_POSITIONS = [
    (0.5, math.sqrt(3) / 2, 0),  # Sensor 3 (back left)
    (1, 0, 0),  # Sensor 2 (front)
    (0, 0, 0),  # Sensor 1 (back right)
    (0.5, math.sqrt(3) / 6, math.sqrt(6) / 3),  # Sensor 4 (top)
]

def generate_raw_sound4():
    # Define the position of the sound source (in feet)
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    z = random.uniform(-10, 10)

    # Calculate the distances from the sound source to each sensor (in feet)
    distances = [
        math.sqrt((x - sx) ** 2 + (y - sy) ** 2 + (z - sz) ** 2)
        for (sx, sy, sz) in SENSOR_POSITIONS
    ]

    # Calculate the times of arrival of the sound at each sensor (in seconds)
    speed_of_sound = 1125.33  # feet per second (at 70 degrees F)
    times = [d / speed_of_sound for d in distances]

    # Calculate the parameters a, b, and c using the differences between the times
    # of arrival and the time of arrival at the center of the array (assuming the
    # sound source is at the center of the array)
    t_center = sum(times) / len(times)
    a = (times[1] - times[0]) - (t_center - times[0])
    b = (times[2] - times[0]) - (t_center - times[0])
    c = (times[3] - times[0]) - (t_center - times[0])

    # Create a new RawSound object with the calculated times and parameters
    raw_sound = RawSound(times, a, b, c)

    return raw_sound
