```python
import serial

class TelemetryCommunication:
    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate
        self.connection = None

    def connect(self):
        try:
            self.connection = serial.Serial(self.port, self.baud_rate)
            print("Connected to telemetry radio.")
        except Exception as e:
            print(f"Failed to connect to telemetry radio: {e}")

    def send_data(self, data):
        if self.connection is None:
            print("Not connected to telemetry radio.")
            return

        try:
            self.connection.write(data.encode())
            print("Data sent.")
        except Exception as e:
            print(f"Failed to send data: {e}")

    def receive_data(self):
        if self.connection is None:
            print("Not connected to telemetry radio.")
            return

        try:
            data = self.connection.readline().decode()
            print("Data received.")
            return data
        except Exception as e:
            print(f"Failed to receive data: {e}")

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
            print("Disconnected from telemetry radio.")
```