```python
class MotorControl:
    def __init__(self, motor_pins):
        self.motor_pins = motor_pins

    def setup_motors(self):
        for pin in self.motor_pins:
            # setup motor pin here
            pass

    def move_forward(self, speed):
        for pin in self.motor_pins:
            # code to move motor forward
            pass

    def move_backward(self, speed):
        for pin in self.motor_pins:
            # code to move motor backward
            pass

    def stop_motors(self):
        for pin in self.motor_pins:
            # code to stop motors
            pass

    def turn_left(self, speed):
        # code to turn left
        pass

    def turn_right(self, speed):
        # code to turn right
        pass
```