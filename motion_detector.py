# motion_detector.py

import RPi.GPIO as GPIO
import time

PIR_PIN = 17 # make sure you put your corresponding pin you have used
LED_PIN = 27 # same again, check which pin you are using

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

print("### Initializing PIR sensor ###")
time.sleep(10) # giving some time to stabilize the sensor before it initiates
print("Ready to detect motion.")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected! Turning on LED.")
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(LED_PIN, GPIO.LOW)
            print("LED off. Waiting 2 seconds.") # wait time before the sensor starts again
            time.sleep(2)
        else:
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
