```python
import RPi.GPIO as GPIO
from core_module.basic_sensor_data_reading import SensorData

class ObstacleDetection:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        self.sensor_data = SensorData()

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def send_signal(self):
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)

    def read_echo(self):
        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()

        while GPIO.input(self.echo_pin) == 1:
            end_time = time.time()

        return end_time - start_time

    def calculate_distance(self):
        self.send_signal()
        time_elapsed = self.read_echo()
        return (time_elapsed * 34300) / 2

    def detect_obstacle(self):
        distance = self.calculate_distance()
        return distance < 30

    def avoid_obstacle(self):
        if self.detect_obstacle():
            # Add code here to change robot's direction
            pass
```