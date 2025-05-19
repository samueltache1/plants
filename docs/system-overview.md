# System Overview

The project automates common agricultural tasks using local sensors and simple control logic.  It is designed to run fully offline on a Raspberry Pi.

Key subsystems:

1. **Environmental Monitoring** – collect data from sensors in `src/sensors`.
2. **Autonomous Irrigation** – implemented in `src/control/irrigation.py`.
3. **Nutrient Management** – compost tea brewing in `src/control/compost_tea.py`.
4. **Task Scheduling** – handled by `src/scheduler.py`.

This repository currently contains basic stubs for these components which will be expanded over time.
