import cv2
import numpy as np


def blur_score(gray):

    variance = cv2.Laplacian(gray, cv2.CV_64F).var()

    if variance > 150:
        return variance, "Excellent"

    elif variance > 80:
        return variance, "Good"

    elif variance > 40:
        return variance, "Average"

    else:
        return variance, "Blurry"


def brightness_score(gray):

    brightness = np.mean(gray)

    if brightness > 180:
        status = "Too Bright"

    elif brightness < 70:
        status = "Too Dark"

    else:
        status = "Normal"

    return brightness, status