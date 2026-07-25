import cv2
import numpy as np


def detect_copy_move(image):
    """
    Detect suspicious duplicated regions using ORB features.
    Returns:
        keypoints,
        suspicious_matches,
        image_with_keypoints
    """

    image = np.array(image)

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    orb = cv2.ORB_create(1000)

    keypoints, descriptors = orb.detectAndCompute(gray, None)

    output = cv2.drawKeypoints(
        image,
        keypoints,
        None,
        color=(0, 255, 0)
    )

    suspicious = False

    if descriptors is not None:

        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        matches = matcher.match(descriptors, descriptors)

        if len(matches) > 200:
            suspicious = True

    return len(keypoints), suspicious, output