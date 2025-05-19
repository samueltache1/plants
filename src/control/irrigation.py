"""Simple rule-based irrigation control."""
import datetime
from typing import Optional

from sensors import dht22

MOISTURE_THRESHOLD = 30  # percentage
SCHEDULE = ["06:00", "18:00"]  # times of day
DURATION_MINUTES = 5


def read_soil_moisture() -> Optional[float]:
    """Placeholder for soil moisture reading."""
    # TODO: implement actual soil sensor
    return 25.0


def activate_valve(duration: int):
    """Placeholder for hardware control."""
    print(f"[IRRIGATION] Valve open for {duration} minutes")
    # TODO: implement GPIO control


def check_and_water():
    moisture = read_soil_moisture()
    now = datetime.datetime.now().strftime("%H:%M")
    if moisture is not None and moisture < MOISTURE_THRESHOLD and now in SCHEDULE:
        activate_valve(DURATION_MINUTES)
    else:
        print("[IRRIGATION] No watering needed")
