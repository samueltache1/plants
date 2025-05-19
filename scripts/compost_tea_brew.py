"""Simple script to run a compost tea aerator for 24 hours."""
import time
import datetime
import RPi.GPIO as GPIO

AERATOR_PIN = 17  # GPIO pin controlling the relay
BREW_HOURS = 24


def brew_tea():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(AERATOR_PIN, GPIO.OUT)
    GPIO.output(AERATOR_PIN, GPIO.HIGH)
    start = time.time()
    while time.time() - start < BREW_HOURS * 3600:
        time.sleep(60)
    GPIO.output(AERATOR_PIN, GPIO.LOW)
    GPIO.cleanup()
    print(f"Tea brew completed: {datetime.datetime.now()}")


if __name__ == "__main__":
    brew_tea()
