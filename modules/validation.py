import re


def validate_aadhaar(aadhaar_number):
    """
    Validate Aadhaar format.
    """

    pattern = r"^\d{4}\s\d{4}\s\d{4}$"

    if re.match(pattern, aadhaar_number):
        return True

    return False


def image_quality(height, width):
    """
    Basic image quality check.
    """

    if height >= 600 and width >= 600:
        return "Good"

    return "Poor"


def ocr_quality(text):
    """
    Estimate OCR quality.
    """

    words = text.split()

    if len(words) > 50:
        return "Excellent"

    elif len(words) > 20:
        return "Good"

    elif len(words) > 10:
        return "Average"

    else:
        return "Poor"