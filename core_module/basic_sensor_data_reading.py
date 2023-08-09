```python
class SensorData:
    def __init__(self):
        self.sensor_data = {}

    def read_sensor(self, sensor_name):
        """
        This function reads data from the specified sensor.
        """
        # Code to read data from the sensor
        # This is a placeholder and should be replaced with actual code
        data = 0
        self.sensor_data[sensor_name] = data
        return data

    def get_all_sensor_data(self):
        """
        This function returns data from all sensors.
        """
        return self.sensor_data

    def clear_sensor_data(self):
        """
        This function clears all sensor data.
        """
        self.sensor_data = {}
```