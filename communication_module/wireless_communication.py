```python
import nrf24

class WirelessCommunication:
    def __init__(self):
        self.radio = nrf24.NRF24()
        self.radio.begin(0, 0, 17, 18) # configure the NRF24 module

    def send_data(self, address, data):
        self.radio.openWritingPipe(address)
        self.radio.write(data)

    def receive_data(self, address):
        self.radio.openReadingPipe(1, address)
        self.radio.startListening()

        while not self.radio.available():
            pass

        received_message = []
        self.radio.read(received_message, self.radio.getDynamicPayloadSize())
        print(f"Received: {received_message}")

    def close(self):
        self.radio.stopListening()
        self.radio.powerDown()
```