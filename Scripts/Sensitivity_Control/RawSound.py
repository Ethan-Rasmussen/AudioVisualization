import struct

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
        with open(file_path, 'wb') as f:
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
