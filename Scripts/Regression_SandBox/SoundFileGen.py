import random
from RawSound import RawSound
from gas import generate_array_size
from SoundGen import generate_raw_sound
from SoundGen2 import generate_raw_sound2
from SoundGen3 import generate_raw_sound3
from SoundGen4 import generate_raw_sound4 #latest

''' TOGGLE-ABLE VALUES '''
######################################
num_sounds = 81                     #
#num_sounds = generate_array_size()   #
destination_file = 'data2.df'       #
#destination_file = 'data1.df'        #
sound_gen_model = 4                  #
######################################

print(f" Generating {num_sounds} sounds in {destination_file}...")
''' PICK AN OPTION FOR THE GENERATOR BRAINS '''
if sound_gen_model == 1:
    raw_sounds = [generate_raw_sound() for _ in range(num_sounds)]
elif sound_gen_model == 2:
    raw_sounds = [generate_raw_sound2() for _ in range(num_sounds)]
elif sound_gen_model == 3:
    raw_sounds = [generate_raw_sound3() for _ in range(num_sounds)]
elif sound_gen_model == 4:
    raw_sounds = [generate_raw_sound4() for _ in range(num_sounds)] #latest
else:
    raise ValueError("Invalid sound_gen_model value")




# Write the list of RawSound objects to a file
with open(destination_file, 'wb') as f:
    for raw_sound in raw_sounds:
        f.write(raw_sound.to_bytes())
        
print(f"    --->Success!")