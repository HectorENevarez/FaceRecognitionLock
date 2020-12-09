#Sliding Lock unlock/lock via facial recognition & DCmotor

import RPi.GPIO as gpio
import time
import client_real
import snap


def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    gpio.setup(25, gpio.OUT)


def forward(tf):
    init()
    gpio.output(23, True)
    gpio.output(24, False)
    gpio.output(25, True)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(23, False)
    gpio.output(24, True)
    gpio.output(25, True)
    time.sleep(tf)
    gpio.cleanup()

#DCmotor rotates clockwise & stops

locked = True
while True:
    if locked:
        action = input("Unlock?")
        if action == "unlock":
            snap.snap()
            result = client_real.client_program()
            if result != "Unknown":
                print("Unlock")
                reverse(5.3)
                print("Stop")
                forward(0.1)
                locked = False
            else:
                print("Unknown face. Please try again.")
                continue
        else:
            continue
    else:
        action = input("Lock?")
        if action == "lock":
            print(action)
            forward(5.3)
            print("Stop")
            reverse(0.01)
            locked = True
        else:
            continue







