import time
import threading
from RawSound import RawSound

class SoundTrigger:
    def __init__(self):
        self.triggered = False
        self.trigger_time = None

    def wait(self):
        while not self.triggered:
            time.sleep(0.000001)  # Sleep for 1 microsecond

    def set(self):
        self.triggered = True
        self.trigger_time = time.monotonic()  # Get current time with microsecond precision

class SoundThread(threading.Thread):
    def __init__(self, trigger):
        super().__init__()
        self.trigger = trigger

    def run(self):
        self.trigger.wait()  # Wait for the trigger
        trigger_time = self.trigger.trigger_time
        times = [0.0, 0.0, 0.0, 0.0]
        for i in range(4):
            times[i] = time.monotonic() - trigger_time
            time.sleep(0.000001)  # Sleep for 1 microsecond to minimize error
        a = 0.0
        b = 0.0
        c = 0.0
        raw_sound = RawSound(times, a, b, c)
        print(f"RawSound: {raw_sound}")

def main():
    trigger = SoundTrigger()
    threads = [SoundThread(trigger) for _ in range(3)]
    while True:
        # Reset trigger
        trigger.triggered = False
        trigger.trigger_time = None
        # Start threads
        for thread in threads:
            thread.start()
        # Wait for all threads to finish
        for thread in threads:
            thread.join()
        # Create RawSound object and store in list
        raw_sound = RawSound(times=trigger.trigger_time, a=0.0, b=0.0, c=0.0)
        print(f"New RawSound: {raw_sound}")
        # Restart threads
        threads = [SoundThread(trigger) for _ in range(3)]

if __name__ == "__main__":
    main()
