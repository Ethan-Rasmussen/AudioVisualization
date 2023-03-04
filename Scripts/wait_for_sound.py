import threading
import time
import RPi.GPIO as GPIO

######################################################################################
def record_input(mic_pin):
    start_time = time.time()
    return start_time
######################################################################################
def handle_input(mic_pin, mic_index):
    input_time = record_input(mic_pin)
    print("Microphone {}: {}".format(mic_index, input_time))
######################################################################################
def timing(pin, index):
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    
    mic_input = False
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=handle_input, bouncetime=200)#, args=(pin, index))
    while mic_input is False:
        if GPIO.event_detected(pin):
            mic_input = True
            handle_input(pin, index)
######################################################################################
class MyThread(threading.Thread):
    def __init__(self, name, index, pin):
        threading.Thread.__init__(self)
        self.name = name
        self.index = index
        self.pin = pin
    
    def run(self):
        timing(self.pin, self.index)
        ##print(str(self.name) + ' is running, index: ' + str(self.index))
######################################################################################
mic1 = MyThread('Microphone 1', 1, 4)
mic2 = MyThread('Microphone 2', 2, 17)
mic3 = MyThread('Microphone 3', 3, 22)
mic4 = MyThread('Microphone 4', 4, 27)

mic1.start()
mic2.start()
mic3.start()
mic4.start()

    
    
