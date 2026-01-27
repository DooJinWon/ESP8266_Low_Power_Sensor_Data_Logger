## Repository Structure and Code Description

This repository contains firmware and server-side scripts for building a low-power
temperature logging device using an ESP8266 and an infrared (IR) temperature sensor.
The system supports Deep Sleep operation and CSV-based data logging.

---

## File Overview

### `IRdevice_uploaded_on_esp8266.ino`
This file contains the firmware for the ESP8266 microcontroller.  
It reads temperature data from the IR sensor and transmits the data to a server
over Wi-Fi.

Main functionalities:
- Measurement of ambient and object temperature
- Wi-Fi connection and HTTP communication
- JSON-based data transmission
- Deep Sleep operation for low power consumption

---

### `server.py`
This script implements a lightweight data collection server using Flask.  
It receives temperature data from the ESP8266 device and stores the data in CSV format.

Main functionalities:
- REST API endpoint for receiving sensor data
- Automatic creation and update of CSV log file
- Timestamp and client IP address logging
- API endpoint for retrieving the latest measurement

---

### `data_log.csv`
This file contains logged temperature data collected from the ESP8266 device.  
Each row represents one measurement cycle and is automatically appended by the server.


---

## System Workflow

The overall system workflow is as follows:

1. ESP8266 wakes up from Deep Sleep
2. Temperature data is measured using the IR sensor
3. Measured data is sent to the server via HTTP
4. Server stores the data in a CSV file
5. ESP8266 enters Deep Sleep mode again

This workflow repeats at a predefined interval.

---

## Notes

- Deep Sleep requires a hardware connection between GPIO16 (D0) and RST.
- Server address, Wi-Fi credentials, and sleep intervals must be configured
  in the firmware before deployment.
- File paths and parameters may need to be adjusted depending on the
  target environment and hardware configuration.


