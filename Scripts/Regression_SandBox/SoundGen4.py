import random
from RawSound import RawSound

def generate_raw_sound4():
    # Source position located anywhere within 10 feet of the array center
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    z = random.uniform(-5, 5)
    
    # Distance from each sensor to source
    d1 = ((x - 0.5)**2 + (y - 0.5)**2 + (z - 0.5)**2)**0.5
    d2 = ((x - 0.5)**2 + (y + 0.5)**2 + (z - 0.5)**2)**0.5
    d3 = ((x + 0.5)**2 + (y - 0.5)**2 + (z - 0.5)**2)**0.5
    d4 = ((x + 0.5)**2 + (y + 0.5)**2 + (z + 0.5)**2)**0.5
    
    # Calculate times for each sensor
    speed_of_sound = 343  # m/s
    t1 = int(d1 / speed_of_sound * 1e6)
    t2 = int(d2 / speed_of_sound * 1e6)
    t3 = int(d3 / speed_of_sound * 1e6)
    t4 = int(d4 / speed_of_sound * 1e6)
    
    # Add a random offset to each time
    t1 += random.randint(-5, 5)
    t2 += random.randint(-5, 5)
    t3 += random.randint(-5, 5)
    t4 += random.randint(-5, 5)
    
    # Calculate average time and differences between each time and average
    avg_t = (t1 + t2 + t3 + t4) // 4
    d_t1 = t1 - avg_t
    d_t2 = t2 - avg_t
    d_t3 = t3 - avg_t
    d_t4 = t4 - avg_t
    
    # Calculate a, b, and c parameters using the differences between each time and average
    a = (d_t2 - d_t1) / 0.2
    b = (d_t3 - d_t1) / 0.2
    c = (d_t4 - d_t1) / 0.2
    
    # Create and return RawSound instance
    times = [t1, t2, t3, t4]
    return RawSound(times, a, b, c)
