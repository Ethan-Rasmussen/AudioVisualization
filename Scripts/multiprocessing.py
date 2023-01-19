import threading

class thread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID
    
    def run(self):
        print(str(self.thread_name) +" "+ str(self.thread_ID))

thread1 = thread("Microphone1", 1000)
thread2 = thread("Microphone2", 2000)
thread3 = thread("Microphone3", 3000)
thread4 = thread("Microphone4", 4000)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

print("Exit")