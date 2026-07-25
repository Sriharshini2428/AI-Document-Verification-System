def calculate_score(face_found, qr_found, aadhaar_valid, image_quality, ocr_quality):

    score = 0

    # Face Detection (25 Marks)
    if face_found:
        score += 25

    # QR Detection (25 Marks)
    if qr_found:
        score += 25

    # Aadhaar Validation (20 Marks)
    if aadhaar_valid:
        score += 20

    # Image Quality (15 Marks)
    if image_quality == "Excellent":
        score += 15
    elif image_quality == "Good":
        score += 10
    elif image_quality == "Average":
        score += 5

    # OCR Quality (15 Marks)
    if ocr_quality == "Excellent":
        score += 15
    elif ocr_quality == "Good":
        score += 10
    elif ocr_quality == "Average":
        score += 5

    # Final Status
    if score >= 80:
        status = "✅ GENUINE DOCUMENT"

    elif score >= 60:
        status = "🟡 NEEDS MANUAL VERIFICATION"

    else:
        status = "❌ SUSPICIOUS DOCUMENT"

    return score, status