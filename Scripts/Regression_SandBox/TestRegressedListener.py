import sys
import pathlib
import time
from RawSound import RawSound
from RegressedSoundBuffer import RegressedSoundBuffer
from RawSoundBuffer import RawSoundBuffer

def print_sound_data(regressed_sound):
    print(f"Times:")
    print(f"{regressed_sound.times}")
    print(f"A (predicted): {regressed_sound.a}")
    print(f"        mean_sq_error: {regressed_sound.error_a}")
    print(f"B (predicted): {regressed_sound.b}")
    print(f"        mean_sq_error: {regressed_sound.error_a}")
    print(f"C (predicted): {regressed_sound.c}")
    print(f"        mean_sq_error: {regressed_sound.error_a}")
#     print(f"A (actual): {regressed_sound.actual_a}")
#     print(f"B (actual): {regressed_sound.actual_b}")
#     print(f"C (actual): {regressed_sound.actual_c}")

if __name__ == '__main__':
    next_sound = RawSound()
    regressed_sound_buffer = RegressedSoundBuffer()
    while True:
        try:
            next_sound = RawSoundBuffer.get_next_sound()
            if next_sound != None:
                regressed_sound_buffer.add_raw_sound(next_sound)
                regressed_sound = regressed_sound_buffer.get_regressed_sound()
                if regressed_sound != None:
                    print_sound_data(regressed_sound)
        except KeyboardInterrupt:
            break
