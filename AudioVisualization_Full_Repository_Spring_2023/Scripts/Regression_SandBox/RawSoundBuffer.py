from RawSound import RawSound
import serial
import psutil
import time

#link = serial.Serial('/dev/ttyACM0', 115200)

# Get the name of the serial port you want to use
serial_port = '/dev/ttyACM0'

# Check if any processes are using the serial port and kill them
for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline'])
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
    else:
        if pinfo['name'] == 'python' and len(pinfo['cmdline']) > 1 and pinfo['cmdline'][1] == serial_port:
            print(f"Killing process {pinfo['pid']} ({pinfo['cmdline']})")
            proc.kill()

# Now you can open the serial port without any processes blocking it
try:
    link = serial.Serial(serial_port, 115200)
    print(f"Connected to ['Audio Visualization Sensor Array']\n"
        f"@{serial_port}(SERIAL_PORT)")
except serial.serialutil.SerialException as e:
    print(f"Error connecting to {serial_port}: {str(e)}")


class RawSoundBuffer:
    def __init__(self):
        self.raw_sounds = []


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
            times = [float(x) / 1000000 for x in data]
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
            
    @classmethod
    def get_next_sound_clean_style(cls):
        buffer = cls()
        count = 0

        # Clear any existing sounds from the buffer
        buffer.raw_sounds = []
        link.reset_input_buffer()

        while True:
            # Check if there are any sounds waiting in the buffer
            if link.in_waiting > 0:
                message = link.readline().decode().strip()
                try:
                    new_buffer = RawSoundBuffer.parse_message(message)
                    buffer.add_raw_sound(new_buffer.raw_sounds[0])
                except Exception as e:
                    print(f"Failed to parse message: {message}\nError: {str(e)}")
                    continue

                # Return the first sound in the buffer and clear it
                if len(buffer.raw_sounds) > 0:
                    sound = buffer.raw_sounds[0]
                    buffer.raw_sounds = []
                    # Find the lowest time value for each sound and subtract it from all times
                    min_time = min(sound.times)
                    sound.times = [t - min_time for t in sound.times]
                    return sound

            # If no sounds are waiting, wait for new sounds
            else:
                time.sleep(0.1)


            
            
