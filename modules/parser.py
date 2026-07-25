import re

def detect_document(text):

    text = text.upper()

    aadhaar_keywords = [
        "AADHAAR",
        "AAOHAAR",
        "GOVERNMENT OF INDIA",
        "UNIQUE IDENTIFICATION",
        "UIDAI",
        "AADHAAR SERVICES"
    ]

    pan_keywords = [
        "INCOME TAX DEPARTMENT",
        "PERMANENT ACCOUNT NUMBER"
    ]

    passport_keywords = [
        "PASSPORT",
        "REPUBLIC OF INDIA"
    ]

    driving_keywords = [
        "DRIVING LICENCE",
        "DRIVING LICENSE"
    ]

    aadhaar_score = sum(keyword in text for keyword in aadhaar_keywords)
    pan_score = sum(keyword in text for keyword in pan_keywords)
    passport_score = sum(keyword in text for keyword in passport_keywords)
    driving_score = sum(keyword in text for keyword in driving_keywords)

    scores = {
        "Aadhaar Card": aadhaar_score,
        "PAN Card": pan_score,
        "Passport": passport_score,
        "Driving License": driving_score
    }

    document = max(scores, key=scores.get)

    if scores[document] == 0:
        return "Unknown Document"

    return document