import random
import math
from RawSound import RawSound

# Define the positions of the sensors in the array (in feet)
SENSOR_POSITIONS = [
    (0, 0, 0),
    (1, 0, 0),
    (0.5, math.sqrt(3) / 2, 0),
    (0.5, math.sqrt(3) / 6, math.sqrt(6) / 3),
]

def generate_raw_sound2():
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

#    # Add noise to the times to simulate measurement error
#    #noise = [random.uniform(-0.99, 0.99) for _ in range(4)]
#    noise = [random.uniform(-5.1, 5.1) for _ in range(4)]
#    #noise = [random.uniform(-0.05, 0.05) for _ in range(4)]
#    times = [t + n for t, n in zip(times, noise)]
    
    
    # Create a new RawSound object with the calculated times and parameters
    raw_sound = RawSound(times, a, b, c)

    return raw_sound
