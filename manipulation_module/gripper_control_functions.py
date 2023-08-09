```python
class GripperControl:
    def __init__(self, servo_pin):
        self.servo_pin = servo_pin
        self.gripper_servo = None

    def setup(self):
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.gripper_servo = GPIO.PWM(self.servo_pin, 50)
        self.gripper_servo.start(0)

    def open_gripper(self):
        self.gripper_servo.ChangeDutyCycle(7.5)

    def close_gripper(self):
        self.gripper_servo.ChangeDutyCycle(12.5)

    def cleanup(self):
        import RPi.GPIO as GPIO
        self.gripper_servo.stop()
        GPIO.cleanup()
```