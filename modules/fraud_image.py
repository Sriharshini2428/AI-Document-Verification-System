from PIL import Image
import imagehash


def detect_image_tampering(image):
    """
    Detect possible image manipulation using perceptual hash.
    """

    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)

    phash = imagehash.phash(image)

    hash_value = str(phash)

    suspicious = hash_value.count("f") > 8

    return hash_value, suspicious