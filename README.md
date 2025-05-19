# Autonomous Agriculture Management System

This repository contains an initial framework for developing an autonomous agriculture management system tailored for Tlell, Haida Gwaii. The goal is to provide DIY-friendly automation for local food production with minimal external inputs.

## Contents
- `sensors/` Python modules for reading sensors and publishing data via MQTT.
- `scripts/` Example automation scripts.
- `hardware/` Hardware wiring guides and component lists.
- `docs/` Additional project documentation.

## Quick Start
1. Ensure Python 3 is installed on your Raspberry Pi.
2. Install dependencies:
   ```bash
   sudo apt-get install python3-pip
   pip3 install paho-mqtt Adafruit_DHT
   ```
3. Run the demo sensor script:
   ```bash
   python3 sensors/dht22_mqtt.py
   ```

This will publish temperature and humidity readings to the local MQTT broker on topic `sensors/dht22` every minute.

Further documentation is under development.

See the [docs](docs/README.md) directory for more details.
