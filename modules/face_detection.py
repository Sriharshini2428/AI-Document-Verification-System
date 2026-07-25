import cv2
import numpy as np

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_face(image):
    """
    Detect face in the document.
    Returns:
        image_with_face, number_of_faces = detect_face(image)

        face_found = number_of_faces > 0
    """

    image = np.array(image)

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            3
        )

    return image, len(faces)