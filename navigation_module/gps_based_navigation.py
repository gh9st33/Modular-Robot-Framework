```python
import gps
from core_module.sensor_data import SensorData

class GPSNavigation:
    def __init__(self):
        self.session = gps.gps("localhost", "2947")
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
        self.sensor_data = SensorData()

    def get_current_location(self):
        try:
            report = self.session.next()
            if report['class'] == 'TPV':
                latitude = getattr(report, 'lat', "Unknown")
                longitude = getattr(report, 'lon', "Unknown")
                return latitude, longitude
        except KeyError:
            pass
        except KeyboardInterrupt:
            quit()
        except StopIteration:
            self.session = None
            print("GPSD has terminated")

    def navigate_to(self, target_latitude, target_longitude):
        current_latitude, current_longitude = self.get_current_location()
        while (current_latitude != target_latitude) and (current_longitude != target_longitude):
            # Implement navigation algorithm here
            pass

    def update_sensor_data(self):
        latitude, longitude = self.get_current_location()
        self.sensor_data.update_gps_data(latitude, longitude)
```