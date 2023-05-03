from RawSound import RawSound

# Read the list of RawSound objects from the file
raw_sounds = []
with open('cal_data.df', 'rb') as f:
    bytes_data = f.read()
    while bytes_data:
        raw_sound = RawSound.from_bytes(bytes_data[:56])
        raw_sounds.append(raw_sound)
        bytes_data = bytes_data[56:]

# Print information about each RawSound object
for i, raw_sound in enumerate(raw_sounds):
    print(f"RawSound {i+1}:")
    print(f"  times: {raw_sound.times}")
    print(f"  a: {raw_sound.a}")
    print(f"  b: {raw_sound.b}")
    print(f"  c: {raw_sound.c}")
