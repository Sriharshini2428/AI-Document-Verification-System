import re


def extract_aadhaar(text):

    pattern = r"\d{4}\s\d{4}\s\d{4}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_gender(text):

    text = text.upper()

    if "MALE" in text:
        return "Male"

    elif "FEMALE" in text:
        return "Female"

    return "Not Found"


def extract_dob(text):

    pattern = r"\d{2}/\d{2}/\d{4}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"