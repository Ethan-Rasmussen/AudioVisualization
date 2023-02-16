import random
from math import sqrt
from RawSound import RawSound

# Define the positions of the sensors in the equilateral triangular pyramid array
positions = [(0, 0, 0), (0.5, sqrt(3)/2, 0), (-0.5, sqrt(3)/2, 0), (0, 0, 1)]

# Define the speed of sound in air (in meters per second)
speed_of_sound = 343.0

def generate_raw_sound():
    # Select a random point inside the cube
    x = random.uniform(-0.5, 0.5)
    y = random.uniform(-0.5, 0.5)
    z = random.uniform(-0.5, 0.5)

    # Calculate the distance from the source point to each sensor
    distances = []
    for position in positions:
        dx = x - position[0]
        dy = y - position[1]
        dz = z - position[2]
        distance = sqrt(dx**2 + dy**2 + dz**2)
        distances.append(distance)

    # Calculate the time of arrival for the sound at each sensor
    times = [distance / speed_of_sound for distance in distances]

    # Add some random noise to each time of arrival
    noise = [random.uniform(-0.001, 0.001) for _ in range(4)]
    times = [time + n for time, n in zip(times, noise)]

    # Generate the RawSound object from the times and random coefficients
    a = random.uniform(-1.0, 1.0)
    b = random.uniform(-1.0, 1.0)
    c = random.uniform(-1.0, 1.0)
    raw_sound = RawSound(times, a, b, c)

    return raw_sound
