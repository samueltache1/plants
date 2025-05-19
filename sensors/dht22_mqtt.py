import time
import Adafruit_DHT
import paho.mqtt.client as mqtt

SENSOR = Adafruit_DHT.DHT22
PIN = 4  # GPIO pin number
MQTT_BROKER = 'localhost'
MQTT_TOPIC = 'sensors/dht22'

client = mqtt.Client()
client.connect(MQTT_BROKER)


def read_and_publish():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    if humidity is not None and temperature is not None:
        payload = f"{temperature:.1f},{humidity:.1f}"
        client.publish(MQTT_TOPIC, payload)
        print(f"Published: {payload}")
    else:
        print("Failed to read from sensor")


if __name__ == '__main__':
    while True:
        read_and_publish()
        time.sleep(60)
