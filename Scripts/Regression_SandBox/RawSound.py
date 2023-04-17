import serial
import struct
from typing import List

class RawSound:
    def __init__(self, times=None, a=None, b=None, c=None):
        self.times = times or [0.0, 0.0, 0.0, 0.0]
        self.a = a or 0.0
        self.b = b or 0.0
        self.c = c or 0.0

    def to_bytes(self):
        time_bytes = struct.pack('4d', *self.times)
        abc_bytes = struct.pack('3d', self.a, self.b, self.c)
        return time_bytes + abc_bytes

    @classmethod
    def from_bytes(cls, bytes_data):
        time_bytes = bytes_data[:32]
        abc_bytes = bytes_data[32:]
        times = struct.unpack('4d', time_bytes)
        if len(abc_bytes) != 24:
            raise ValueError(f"Invalid byte string length: expected 24 bytes, got {len(abc_bytes)}")
        a, b, c = struct.unpack('3d', abc_bytes)
        return cls(times, a, b, c)

    def write_to_file(self, file_path):
        with open(file_path, 'ab') as f:
            f.write(self.to_bytes())

    @classmethod
    def read_from_file(cls, file_path):
        raw_sounds = []
        with open(file_path, 'rb') as f:
            bytes_data = f.read()
            while bytes_data:
                raw_sound = RawSound.from_bytes(bytes_data[:56])
                raw_sounds.append(raw_sound)
                bytes_data = bytes_data[56:]
        return raw_sounds


    @classmethod
    def get_next_sound(cls):
        buffer = cls()

        while True:
            # Read messages from serial and parse them
            if buffer.link.in_waiting > 0:
                message = buffer.link.readline().decode().strip()
                try:
                    new_buffer = RawSoundBuffer.parse_message(message)
                    buffer.raw_sounds.extend(new_buffer.raw_sounds)
                except Exception as e:
                    print(f"Failed to parse message: {message}\nError: {str(e)}")
                    continue

                if len(buffer.raw_sounds) > 0:
                    # Return the first raw sound in the buffer
                    return buffer.raw_sounds.pop(0)

            # Wait before checking for more messages
            time.sleep(0.1)

class RawSoundBuffer:
    def __init__(self):
        self.raw_sounds = []
        self.link = serial.Serial('/dev/ttyACM0', 115200)

    def add_raw_sound(self, raw_sound):
        self.raw_sounds.append(raw_sound)

    def to_bytes(self):
        return b''.join(raw_sound.to_bytes() for raw_sound in self.raw_sounds)

    @classmethod
    def from_bytes(cls, bytes_data):
        buffer = cls()
        i = 0
        while i < len(bytes_data):
            raw_sound = RawSound.from_bytes(bytes_data[i:i+56])
            buffer.add_raw_sound(raw_sound)
            i += 56
        return buffer

    def write_to_file(self, file_path):
        with open(file_path, 'ab') as f:
            f.write(self.to_bytes())

    @classmethod
    def read_from_file(cls, file_path):
        buffer = cls()
        with open(file_path, 'rb') as f:
            bytes_data = f.read()
            buffer = cls.from_bytes(bytes_data)
        return buffer

    @classmethod
    def parse_message(cls, message: str) -> 'RawSoundBuffer':
        buffer = cls()
        lines = message.strip().split('\n')
        for line in lines:
            data = line.split(',')
            times = [float(x) / 1000000.0 for x in data]
            raw_sound = RawSound(times=times)
            buffer.add_raw_sound(raw_sound)
        return buffer

    @classmethod
    def get_next_sound(cls):
        buffer = cls()

        while True:
            # Read messages from serial and parse them
            if link.in_waiting > 0:
                message = link.readline().decode().strip()
                try:
                    new_buffer = RawSoundBuffer.parse_message(message)
                    buffer.raw_sounds.extend(new_buffer.raw_sounds)
                except Exception as e:
                    print(f"Failed to parse message: {message}\nError: {str(e)}")
                    continue

                if len(buffer.raw_sounds) > 0:
                    # Return the first raw sound in the buffer
                    return buffer.raw_sounds.pop(0)

            # Wait before checking for more messages
            time.sleep(0.1)
