"""Control logic for compost tea brewer."""
import time
import datetime
import RPi.GPIO as GPIO

AERATOR_PIN = 17  # GPIO pin controlling the relay
BREW_HOURS = 24


def start_brew():
    """Begin aerating compost tea."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(AERATOR_PIN, GPIO.OUT)
    GPIO.output(AERATOR_PIN, GPIO.HIGH)
    return time.time()


def stop_brew(start_time: float):
    """Stop aeration after the desired time."""
    while time.time() - start_time < BREW_HOURS * 3600:
        time.sleep(60)
    GPIO.output(AERATOR_PIN, GPIO.LOW)
    GPIO.cleanup()
    print(f"Tea brew completed: {datetime.datetime.now()}")


if __name__ == "__main__":
    t0 = start_brew()
    stop_brew(t0)
