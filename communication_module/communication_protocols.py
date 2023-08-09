```python
class CommunicationProtocol:
    def __init__(self):
        self.connected_devices = []

    def connect(self, device):
        if device not in self.connected_devices:
            self.connected_devices.append(device)
            return True
        return False

    def disconnect(self, device):
        if device in self.connected_devices:
            self.connected_devices.remove(device)
            return True
        return False

    def send_data(self, device, data):
        if device in self.connected_devices:
            # Here we would have the actual code to send the data
            # For the sake of this example, we will just print it
            print(f"Sending {data} to {device}")
            return True
        return False

    def receive_data(self, device):
        if device in self.connected_devices:
            # Here we would have the actual code to receive the data
            # For the sake of this example, we will just simulate it
            received_data = "Simulated data"
            print(f"Received {received_data} from {device}")
            return received_data
        return None
```