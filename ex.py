from time import *
from threading import Thread

def myBox():
    while True:
        print('My box is open:')
        sleep(5)
        print('My box is closed:')
        sleep(5)

def myLED():
    while True:
        print('LED on')
        sleep(1)
        print('LED off')
        sleep(1)

boxThread = Thread(target=myBox)
LEDThread = Thread(target=myLED)

boxThread.daemon = True
LEDThread.daemon = True

boxThread.start()
LEDThread.start()
j=0
while True:
    print(j)
    j=j+1
    sleep(0.1)
