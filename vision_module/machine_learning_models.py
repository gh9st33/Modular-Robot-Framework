```python
import tensorflow as tf
from tensorflow.keras.models import load_model
from core_module.basic_sensor_data_reading import SensorData

class MLModels:
    def __init__(self, model_path):
        self.model = load_model(model_path)
        self.sensor_data = SensorData()

    def predict(self, image):
        processed_image = self.preprocess_image(image)
        prediction = self.model.predict(processed_image)
        return prediction

    def preprocess_image(self, image):
        # Image preprocessing steps can be added here
        return image

    def capture_and_predict(self):
        image = self.sensor_data.capture_image()
        prediction = self.predict(image)
        return prediction
```