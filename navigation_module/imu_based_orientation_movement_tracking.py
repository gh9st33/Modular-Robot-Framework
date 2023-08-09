```python
import math
from core_module.basic_sensor_data_reading import SensorData

class IMUTracking:
    def __init__(self):
        self.sensor_data = SensorData()
        self.orientation = [0, 0, 0]  # roll, pitch, yaw
        self.position = [0, 0, 0]  # x, y, z

    def update_orientation(self):
        # Assuming the sensor data provides Euler angles in degrees
        euler_angles = self.sensor_data.read_imu_euler_angles()
        self.orientation = [math.radians(angle) for angle in euler_angles]

    def update_position(self):
        # Assuming the sensor data provides displacement in meters
        displacement = self.sensor_data.read_imu_displacement()
        self.position = [self.position[i] + displacement[i] for i in range(3)]

    def get_orientation(self):
        return self.orientation

    def get_position(self):
        return self.position
```