import cv2
import numpy as np

def preprocess_image(image, blur_size=5):

    img = np.array(image)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Light Gaussian Blur
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    # Otsu Threshold
    _, threshold = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return img, gray, blur, threshold