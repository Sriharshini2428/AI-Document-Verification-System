import cv2
import numpy as np

def detect_qr(image):
    """
    Detect QR Code in the uploaded document.
    Returns:
        image_with_box,
        qr_found
    """

    image = np.array(image)

    detector = cv2.QRCodeDetector()

    data, points, _ = detector.detectAndDecode(image)

    if points is not None:

        points = points.astype(int)

        for i in range(len(points[0])):
            pt1 = tuple(points[0][i])
            pt2 = tuple(points[0][(i + 1) % len(points[0])])

            cv2.line(image, pt1, pt2, (0,255,0), 3)

        return image, True

    return image, False