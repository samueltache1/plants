# Autonomous Agriculture Management System

This project aims to provide a self-contained automation toolkit for small farms in Tlell, Haida Gwaii.  It focuses on low-cost hardware, offline operation and clear documentation so that anyone can replicate the setup.

## Repository layout

- `src/` – Python source code
  - `sensors/` – sensor interfaces such as `dht22.py`
  - `control/` – actuator control logic including irrigation and compost tea
  - `scheduler.py` – task scheduler
  - `main.py` – application entry point
- `docs/` – background documentation and hardware notes

## Quick start
1. Install Python 3 on your Raspberry Pi.
2. Install dependencies:
   ```bash
   sudo apt-get install python3-pip
   pip3 install paho-mqtt Adafruit_DHT schedule RPi.GPIO
   ```
3. Run the system:
   ```bash
   python3 src/main.py
   ```

The scheduler will periodically read sensors and run irrigation or compost tea tasks based on the rules in `src/config.yaml`.

See `docs/` for more details.  Contributions are welcome.
