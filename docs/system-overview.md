# System Overview

The goal of this project is to automate common agricultural tasks using locally available resources and open-source hardware and software. Key subsystems:

1. **Environmental Monitoring** – Collect data from soil moisture, temperature, humidity, light, and water level sensors.
2. **Autonomous Irrigation** – Control a drip irrigation system based on sensor data and adaptive scheduling.
3. **Crop Health Monitoring** – Use a camera and on-device machine learning to detect pests and crop stress.
4. **Nutrient Management** – Integrate local resources such as kelp mulch, compost tea, and wood ash.
5. **Offline Operation** – All data is stored locally in SQLite and communication relies on a local MQTT broker.

This repository contains early prototypes. Documentation and software will evolve as functionality grows.
