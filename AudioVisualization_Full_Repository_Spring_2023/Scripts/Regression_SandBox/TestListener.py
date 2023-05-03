import sys
import pathlib
import time
from RawSound import RawSound
from RawSoundBuffer import RawSoundBuffer

#define a list of raw sounds


def print_sound_data(raw_sound):
#     print(f"Times:")
    print(f"{raw_sound.times}")
#     print(f"A: {raw_sound.a}")
#     print(f"B: {raw_sound.b}")
#     print(f"C: {raw_sound.c}")

def listen_and_append():
    gotten_one = False
    next_sound = RawSound()
    while(gotten_one == False):
        try:
            next_sound = RawSoundBuffer.get_next_sound_clean_style()
            if next_sound != None:
                print_sound_data(next_sound)
                gotten_one = True
                #addit to the list
        except KeyboardInterrupt:
            break
    return next_sound


# main script for this file
#listen_and_append()

