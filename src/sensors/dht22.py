"""DHT22 sensor interface and optional MQTT publisher."""
import time
from typing import Tuple, Optional

import Adafruit_DHT
import paho.mqtt.client as mqtt

SENSOR = Adafruit_DHT.DHT22
PIN = 4  # BCM pin number
MQTT_BROKER = 'localhost'
MQTT_TOPIC = 'sensors/dht22'

_client = mqtt.Client()
_client.connect(MQTT_BROKER)


def read() -> Tuple[Optional[float], Optional[float]]:
    """Read temperature and humidity from the sensor."""
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    if humidity is not None and temperature is not None:
        return float(temperature), float(humidity)
    return None, None


def publish_mqtt():
    """Publish a reading to the configured MQTT topic."""
    temperature, humidity = read()
    if temperature is None or humidity is None:
        print("Failed to read from DHT22")
        return
    payload = f"{temperature:.1f},{humidity:.1f}"
    _client.publish(MQTT_TOPIC, payload)
    print(f"Published: {payload}")


if __name__ == '__main__':
    while True:
        publish_mqtt()
        time.sleep(60)
