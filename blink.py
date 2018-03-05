import RPi.GPIO as GPIO
import time

# Configure the PIN # 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)

# Blink Interval 
blink_interval = .5 #Time interval in Seconds

# Blinker Loop
while True:
 GPIO.output(17, True)
 time.sleep(blink_interval)
 GPIO.output(17, False)
 time.sleep(blink_interval)

# Release Resources
GPIO.cleanup()
