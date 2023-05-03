from RawSound import RawSound

# Read the list of RawSound objects from the file
raw_sounds = []
with open('cal_data.df', 'rb') as f:
    bytes_data = f.read()
    while bytes_data:
        raw_sound = RawSound.from_bytes(bytes_data[:56])
        raw_sounds.append(raw_sound)
        bytes_data = bytes_data[56:]
        
# Print the data immediateley after loading it
for raw_sound in raw_sounds:    
    # Print the modified RawSound object
    print(f"RawSound:")
    print(f"  times: {raw_sound.times}")
    print(f"  a: {raw_sound.a}")
    print(f"  b: {raw_sound.b}")
    print(f"  c: {raw_sound.c}")
print(f"------------------------------------------------------------------------------------------------------")


# # Find the lowest time value for each sound and subtract it from all times
# for raw_sound in raw_sounds:
#     min_time = min(raw_sound.times)
#     raw_sound.times = [t - min_time for t in raw_sound.times]
    
# Find the lowest time value for each sound
for raw_sound in raw_sounds:    
    # Print the modified RawSound object
    print(f"RawSound:")
    print(f"  times: {raw_sound.times}")
    print(f"  a: {raw_sound.a}")
    print(f"  b: {raw_sound.b}")
    print(f"  c: {raw_sound.c}")


# Write the modified RawSound objects back to the file
with open('cal_data.df', 'wb') as f:
    for raw_sound in raw_sounds:
        f.write(raw_sound.to_bytes())


# # Find the lowest time value for each sound
# for raw_sound in raw_sounds:    
#     # Print the modified RawSound object
#     print(f"RawSound:")
#     print(f"  times: {raw_sound.times}")
#     print(f"  a: {raw_sound.a}")
#     print(f"  b: {raw_sound.b}")
#     print(f"  c: {raw_sound.c}")
