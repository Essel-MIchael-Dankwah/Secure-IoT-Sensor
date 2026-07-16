# Secure IoT Temperature Sensor

## 📌 Project Overview
This repository contains a Python-based simulation of an IoT Temperature Sensor designed for a research laboratory. The primary focus of this project is to implement strict **Object-Oriented Programming (OOP) Encapsulation** to protect sensitive device configurations from unauthorized or accidental modifications.

## 🚀 Features & Implementation

### 1. Robust Data Protection (Encapsulation)
* **Public Attributes:** The `device_id` is publicly accessible for standard network identification.
* **Private Attributes:** Critical internal states, specifically `__current_temp` and `__calibration_value`, are secured using Python's name mangling to prevent direct external overrides.

### 2. Data Validation via Properties
* **Getter Methods:** Utilizes the `@property` decorator to allow client systems to safely read the current temperature without exposing the underlying private variable.
* **Setter Methods:** Implements strict validation logic on the temperature setter (`@current_temp.setter`). The system rejects any temperature input outside the physical operational range of **-50°C to 150°C**.

### 3. Secure Configuration Access
* Includes an `update_calibration()` method that acts as a gatekeeper for sensitive device settings. 
* Requires an authorized administrative passcode before allowing any modifications to the internal calibration data.

## 💻 Code Example
```python
# Instantiating the sensor
sensor = IoTSensor("id001", 30, 500)

# Updating temperature (Triggers validation logic)
sensor.current_temp = 87  # Success
sensor.current_temp = 200 # Fails: "Invalid temperature"

# Updating secure calibration
sensor.update_calibration(4030) # Requires Admin Passcode
