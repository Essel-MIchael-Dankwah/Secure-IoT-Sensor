# IoT Sensor

class IoTSensor:

    def __init__(self, device_id, __current_temp, __calibration_value):
        self.device_id = device_id
        self.__current_temp = __current_temp
        self.__calibration_value = __calibration_value

# Updating the current temperatue internally with @proerty and Setters
    
    @property
    def current_temp(self):
        return self.__current_temp

    @current_temp.setter
    def current_temp(self, temp):
        if -50 <= float(temp) and float(temp) <= 150:
            self.__current_temp = temp

        else:
            print(" Invalid temperature")

# Updating the calibration value from authorized individuals
    def update_calibration(self,new):
        admin_passcode = input("Enter Stats")
        if admin_passcode == "UMaT2026": # Checking if the user is offered access to current data update
            self.__calibration_value = new
        else:
            print(" Access Denied")
'''
# Code Functionality Logic
# Instantiating the sensor
sensor = IoTSensor("id001", 30, 500)

# Updating temperature (Triggers validation logic)
sensor.current_temp = 87  # Success
sensor.current_temp = 200 # Fails: "Invalid temperature"

# Updating secure calibration
sensor.update_calibration(4030) # Requires Admin Passcode
'''