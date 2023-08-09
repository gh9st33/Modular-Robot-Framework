```python
class PowerManagement:
    def __init__(self):
        self.battery_level = 100
        self.low_power_threshold = 20
        self.is_charging = False

    def get_battery_level(self):
        # Code to read the battery level from the hardware
        return self.battery_level

    def is_low_power(self):
        return self.battery_level <= self.low_power_threshold

    def start_charging(self):
        # Code to start charging the robot
        self.is_charging = True

    def stop_charging(self):
        # Code to stop charging the robot
        self.is_charging = False

    def update_power_status(self):
        # Code to update the power status based on the hardware readings
        self.battery_level = self.get_battery_level()
        if self.is_low_power():
            self.start_charging()
        else:
            self.stop_charging()
```