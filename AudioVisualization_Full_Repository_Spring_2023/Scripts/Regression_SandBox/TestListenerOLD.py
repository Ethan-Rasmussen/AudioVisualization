import sys
import pathlib
import time
from RawSound import RawSound
from RawSoundBuffer import RawSoundBuffer

def print_sound_data(raw_sound):
    print(f"Times:")
    print(f"{raw_sound.times}")
    print(f"A: {raw_sound.a}")
    print(f"B: {raw_sound.b}")
    print(f"C: {raw_sound.c}")

if __name__ == '__main__':
    next_sound = RawSound()
    while True:
        try:
            next_sound = RawSoundBuffer.get_next_sound()
            if next_sound != None:
                print_sound_data(next_sound)
        except KeyboardInterrupt:
            break
