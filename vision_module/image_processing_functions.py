```python
import cv2
import numpy as np

class ImageProcessing:
    def __init__(self):
        pass

    def convert_to_grayscale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def blur_image(self, image, kernel_size=5):
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    def detect_edges(self, image, low_threshold=50, high_threshold=150):
        return cv2.Canny(image, low_threshold, high_threshold)

    def dilate(self, image, kernel=None, iterations=1):
        if kernel is None:
            kernel = np.ones((5,5),np.uint8)
        return cv2.dilate(image, kernel, iterations)

    def erode(self, image, kernel=None, iterations=1):
        if kernel is None:
            kernel = np.ones((5,5),np.uint8)
        return cv2.erode(image, kernel, iterations)

    def resize_image(self, image, width=None, height=None, inter=cv2.INTER_AREA):
        dim = None
        (h, w) = image.shape[:2]

        if width is None and height is None:
            return image

        if width is None:
            r = height / float(h)
            dim = (int(w * r), height)
        else:
            r = width / float(w)
            dim = (width, int(h * r))

        return cv2.resize(image, dim, interpolation=inter)
```