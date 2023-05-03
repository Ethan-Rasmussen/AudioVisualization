from RawSound import RawSound
import os

def load_raw_sounds_from_file(file_path):
    raw_sounds = []
    print(os.getcwd())
    with open(file_path, 'rb') as f:
        bytes_data = f.read()
        while bytes_data:
            raw_sound = RawSound.from_bytes(bytes_data[:56])
            raw_sounds.append(raw_sound)
            bytes_data = bytes_data[56:]
    return raw_sounds
