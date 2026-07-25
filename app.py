import cv2
import streamlit as st

st.write("OpenCV Version:", cv2.__version__)
st.write("Has CascadeClassifier:", hasattr(cv2, "CascadeClassifier"))
st.write("OpenCV Path:", cv2.__file__)

st.stop()

import streamlit as st
from PIL import Image

from modules.image_processing import preprocess_image
from modules.ocr import extract_text
from modules.parser import detect_document
from modules.qr_detection import detect_qr
from modules.face_detection import detect_face
from modules.fraud_detection import calculate_score
from modules.fraud_image import detect_image_tampering
from modules.advanced_tampering import detect_copy_move
import plotly.express as px
import pandas as pd
from modules.report import generate_report
from modules.database import (
    create_database,
    save_history,
    load_history
)
from modules.extractor import (
    extract_aadhaar,
    extract_gender,
    extract_dob
)
from modules.validation import (
    validate_aadhaar,
    image_quality,
    ocr_quality
)
from modules.quality_analysis import (
    blur_score,
    brightness_score
)

# ------------------------------------
# Page Configuration
# ------------------------------------

st.set_page_config(
    page_title="AI Document Verification System",
    page_icon="🪪",
    layout="wide"
)
create_database()

# ------------------------------------
# Header
# ------------------------------------

st.title("🪪 AI Document Verification System")

st.markdown("""
Verify identity documents using **Artificial Intelligence**, **Computer Vision**, and **OCR**.
""")

st.divider()

# ------------------------------------
# Sidebar
# ------------------------------------

with st.sidebar:

    st.header("Supported Documents")

    st.write("✅ Aadhaar Card")
    st.write("✅ PAN Card")
    st.write("✅ Passport")
    st.write("✅ Driving License")

    st.divider()

    st.info("Version 1.0")

# ------------------------------------
# Upload Section
# ------------------------------------

uploaded_file = st.file_uploader(
    "Upload an Identity Document",
    type=["jpg", "jpeg", "png"]
)

# ==========================================
# Main Processing
# ==========================================

if uploaded_file is not None:

    # ----------------------------
    # Load Image
    # ----------------------------

    image = Image.open(uploaded_file)

    original_image, gray_image, blur_image, threshold_image = preprocess_image(
        image,
        blur_size=5
    )

    # ----------------------------
    # Face Detection
    # ----------------------------

    face_image, face_count = detect_face(image)
    face_found = face_count > 0

    # ----------------------------
    # QR Detection
    # ----------------------------

    qr_image, qr_found = detect_qr(image)

    # ----------------------------
    # Display Images
    # ----------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Original Image")
        st.image(image, use_container_width=True)

        st.subheader("Grayscale")
        st.image(gray_image, use_container_width=True)

    with col2:

        st.subheader("Gaussian Blur")
        st.image(blur_image, use_container_width=True)

        st.subheader("Threshold Image")
        st.image(threshold_image, use_container_width=True)

    st.divider()

    # ----------------------------
    # Image Properties
    # ----------------------------

    height, width = gray_image.shape

    st.subheader("Image Properties")

    st.write(f"**Width:** {width} pixels")
    st.write(f"**Height:** {height} pixels")
    st.write("**Channels:** 1 (Grayscale)")

    st.divider()

    # ----------------------------
    # OCR
    # ----------------------------

    texts = [
        extract_text(gray_image),
        extract_text(blur_image),
        extract_text(threshold_image)
    ]

    text = max(texts, key=len)

    # ----------------------------
    # Information Extraction
    # ----------------------------

    document = detect_document(text)

    aadhaar = extract_aadhaar(text)

    gender = extract_gender(text)

    dob = extract_dob(text)

    # ----------------------------
    # Validation
    # ----------------------------

    aadhaar_valid = validate_aadhaar(aadhaar)

    quality = image_quality(height, width)

    ocr_score = ocr_quality(text)

    blur_value, blur_status = blur_score(gray_image)

    brightness_value, brightness_status = brightness_score(gray_image)

    # ----------------------------
    # AI Fraud Score
    # ----------------------------

    score, status = calculate_score(
        face_found,
        qr_found,
        aadhaar_valid,
        quality,
        ocr_score
    )

    save_history(
    document,
    aadhaar,
    gender,
    dob,
    score,
    status,
    face_found,
    qr_found,
    quality,
    ocr_score
     )

    # ----------------------------
    # Generate PDF
    # ----------------------------

    report_file = "verification_report.pdf"

    generate_report(
        report_file,
        document,
        score,
        status,
        aadhaar,
        gender,
        dob,
        face_found,
        qr_found,
        aadhaar_valid,
        quality,
        ocr_score
    )

    # ----------------------------
    # Results
    # ----------------------------
    st.subheader("📊 Verification Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
      st.metric("Document", document)

    with col2:
      st.metric("Authenticity", f"{score}%")

    with col3:
      st.metric("Faces", face_count)

    st.progress(score / 100)

    st.metric("Confidence Level", f"{score}%")

    st.divider()

    st.subheader("Extracted Information")

    st.write(f"**Aadhaar Number:** {aadhaar}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Date of Birth:** {dob}")

    st.divider()

    # ----------------------------
    # Validation
    # ----------------------------

    st.subheader("✅ Verification Checklist")

    checks = {
    "Aadhaar Number": aadhaar_valid,
    "Face Detected": face_found,
    "QR Code Found": qr_found
    }

    for name, result in checks.items():
     if result:
        st.success(name)
    else:
        st.error(name)

    st.write(f"**Image Quality:** {quality}")

    if ocr_score == "Excellent":
       st.success("OCR Quality : Excellent")

    elif ocr_score == "Good":
       st.info("OCR Quality : Good")

    else:
       st.warning("OCR Quality : Poor")

    st.divider()

    st.subheader("🛡 Document Quality Analysis")

    st.write(f"**Blur Score:** {blur_value:.2f}")
    st.write(f"**Blur Status:** {blur_status}")

    st.write(f"**Brightness:** {brightness_value:.2f}")
    st.write(f"**Brightness Status:** {brightness_status}")

    st.divider()

    # ----------------------------
    # Face Detection
    # ----------------------------

    st.subheader("Face Detection")

    st.image(face_image, use_container_width=True)

    if face_found:
        st.success(f"Face Detected ({face_count})")
    else:
        st.error("No Face Detected")

    st.divider()

    # ----------------------------
    # QR Detection
    # ----------------------------

    st.subheader("QR Code Detection")

    st.image(qr_image, use_container_width=True)

    if qr_found:
        st.success("QR Code Detected")
    else:
        st.error("QR Code Not Found")

    hash_value, suspicious = detect_image_tampering(image)

    keypoints, copy_move, kp_image = detect_copy_move(image)

    st.divider()
    # ----------------------------
    # Fraud Detection
    # ----------------------------
    # 
    st.subheader("🛡 AI Fraud Detection Report")

    st.metric("Authenticity Score", f"{score}%")

    if score >= 90:
      st.success("🟢 Genuine Document")

    elif score >= 70:
       st.warning("🟡 Needs Manual Verification")

    else:
        st.error("🔴 Possible Fraud")

    st.divider()
    st.subheader("📊 Verification Analytics")

    verification_data = pd.DataFrame({
    "Check": [
        "Face",
        "QR",
        "Aadhaar",
        "Image Quality"
    ],
    "Status": [
        int(face_found),
        int(qr_found),
        int(aadhaar_valid),
        1 if quality == "Good" else 0
    ]
   })

    fig = px.bar(
    verification_data,
    x="Check",
    y="Status",
    color="Status",
    text="Status",
    title="Verification Checks"
   )

    st.plotly_chart(fig, use_container_width=True)

    passed = verification_data["Status"].sum()
    failed = len(verification_data) - passed

    pie = px.pie(
    values=[passed, failed],
    names=["Passed", "Failed"],
    title="Verification Result"
  )

    st.plotly_chart(pie, use_container_width=True)

    import plotly.graph_objects as go

    fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=score,
    title={"text": "Authenticity Score"},
    gauge={
        "axis": {"range": [0, 100]},
        "bar": {"color": "green"},
        "steps": [
            {"range": [0, 50], "color": "red"},
            {"range": [50, 80], "color": "orange"},
            {"range": [80, 100], "color": "lightgreen"}
           ]
         }
    ))

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ----------------------------
    # OCR Output
    # ----------------------------

    with st.expander("📄 View OCR Text"):

        st.text_area(
        "OCR Output",
        text,
        height=250 
    )
    st.divider()

    # ----------------------------
    # Download PDF
    # ----------------------------

    st.subheader("📄 Download Verification Report")

    with open(report_file, "rb") as pdf_file:

        st.download_button(
            label="⬇ Download PDF Report",
            data=pdf_file,
            file_name="AI_Verification_Report.pdf",
            mime="application/pdf"
        )

    st.divider()

    # ----------------------------
    # Image Tampering
    # ----------------------------

    st.subheader("🧬 Image Tampering Detection")

    st.write("Perceptual Hash:")

    st.code(hash_value)

    if suspicious:
        st.error("⚠ Possible Image Manipulation Detected")
    else:
        st.success("✔ No Obvious Image Tampering")

    st.divider()

    # ----------------------------
    # Advanced Tampering
    # ----------------------------

    st.subheader("🧠 Advanced Tampering Analysis")

    st.image(kp_image, use_container_width=True)

    st.write(f"Detected Keypoints: {keypoints}")

    if copy_move:
       st.error("⚠ Possible Copy-Move Manipulation")
    else:
       st.success("✔ No Copy-Move Manipulation Found")

    st.divider()

    st.subheader("🤖 Final AI Decision")

    if score >= 90:
      st.success("""
       ### ✅ VERIFIED

      This document passed all major verification checks.

       Risk Level: LOW
      """)

    elif score >= 70:
       st.warning("""
         ### ⚠ MANUAL REVIEW REQUIRED

          Some verification checks need attention.

          Risk Level: MEDIUM
        """)

    else:
      st.error("""
      ### ❌ DOCUMENT REJECTED

       High probability of tampering or invalid document.

       Risk Level: HIGH 
      """)
      st.divider()

st.subheader("📚 Verification History")

history = load_history()

if history:

    import pandas as pd

    df = pd.DataFrame(
        history,
        columns=[
            "ID",
            "Document",
            "Aadhaar",
            "Gender",
            "DOB",
            "Score",
            "Status",
            "Face",
            "QR",
            "Image Quality",
            "OCR Quality"
        ]
    )

    st.dataframe(df, use_container_width=True)

else:
    st.info("No verification history available.")
