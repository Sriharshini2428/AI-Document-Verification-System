# 🪪 AI Document Verification System

An AI-powered Document Verification System that automates the verification of identity documents using Computer Vision, OCR, and Image Processing techniques. The application detects document authenticity by extracting text, validating document information, detecting faces and QR codes, analyzing image quality, and identifying possible image tampering.

🌐 **Live Demo:** https://ai-document-verification-system-zwkyl3ftyfs9ugnehjn8gb.streamlit.app/

📂 **GitHub Repository:** https://github.com/Sriharshini2428/AI-Document-Verification-System

---

# 📌 Features

- ✅ Supports Aadhaar Card
- ✅ Supports PAN Card
- ✅ Supports Passport
- ✅ Supports Driving License
- ✅ OCR-based Text Extraction
- ✅ Face Detection
- ✅ QR Code Detection
- ✅ Image Quality Analysis
- ✅ Blur Detection
- ✅ Brightness Analysis
- ✅ Image Tampering Detection
- ✅ Copy-Move Forgery Detection
- ✅ AI-Based Authenticity Score
- ✅ Verification Checklist
- ✅ PDF Verification Report Generation
- ✅ SQLite Verification History
- ✅ Interactive Streamlit Dashboard

---

# 🚀 Technologies Used

### Programming Language
- Python

### Libraries & Frameworks

- Streamlit
- OpenCV
- EasyOCR
- NumPy
- Pandas
- Plotly
- Pillow
- ReportLab
- SQLite
- Scikit-image

### AI & Computer Vision

- OCR
- Image Processing
- Face Detection
- QR Code Detection
- Image Quality Assessment
- Fraud Detection
- Image Tampering Detection
- Copy-Move Forgery Detection

---

# 🏗 Project Architecture

```
                Upload Document
                       │
                       ▼
            Image Preprocessing
                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
   OCR Module      Face Detection   QR Detection
      │                │                │
      └────────────────┼────────────────┘
                       ▼
            Document Information
                       │
                       ▼
         Image Quality Analysis
                       │
                       ▼
        Tampering Detection Module
                       │
                       ▼
         Authenticity Score Engine
                       │
                       ▼
        PDF Report + Verification History
```

---

# 📂 Project Structure

```
AI-Document-Verification-System
│
├── app.py
├── requirements.txt
├── README.md
│
├── modules
│   ├── image_processing.py
│   ├── ocr.py
│   ├── parser.py
│   ├── extractor.py
│   ├── validation.py
│   ├── face_detection.py
│   ├── qr_detection.py
│   ├── fraud_detection.py
│   ├── fraud_image.py
│   ├── advanced_tampering.py
│   ├── quality_analysis.py
│   ├── database.py
│   └── report.py
│
├── database
├── uploads
├── reports
└── utils
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Sriharshini2428/AI-Document-Verification-System.git
```

Move into the project

```bash
cd AI-Document-Verification-System
```

Create a virtual environment

### Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🖥 How It Works

### Step 1

Upload an identity document.

Supported formats:

- JPG
- JPEG
- PNG

---

### Step 2

The system preprocesses the image by applying:

- Grayscale Conversion
- Gaussian Blur
- Thresholding

---

### Step 3

OCR extracts important information such as:

- Aadhaar Number
- Gender
- Date of Birth

---

### Step 4

Computer Vision modules perform:

- Face Detection
- QR Code Detection

---

### Step 5

Image Quality Analysis checks:

- Resolution
- Blur
- Brightness
- OCR Quality

---

### Step 6

Fraud Detection performs:

- Image Tampering Detection
- Copy-Move Forgery Detection
- Authenticity Score Calculation

---

### Step 7

The system generates:

- Verification Dashboard
- PDF Verification Report
- SQLite Verification History

---

# 📊 Output

The application displays:

- Document Type
- Authenticity Score
- Verification Checklist
- OCR Text
- Face Detection Result
- QR Detection Result
- Blur Analysis
- Brightness Analysis
- Tampering Detection
- AI Decision
- Downloadable PDF Report

---

# 📈 Future Enhancements

- Support for PDF documents
- Digital Signature Verification
- Deep Learning-based Forgery Detection
- Vision Language Model (VLM) Integration
- LLM-powered Document Understanding
- Cloud Database Integration
- User Authentication
- Batch Document Verification
- REST API Support

---

# 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

- Computer Vision
- OCR
- Image Processing
- Fraud Detection
- Document Intelligence
- Streamlit Application Development
- SQLite Database Management
- Python Programming
- AI-powered Verification Systems

---

# 👩‍💻 Author

**Sriharshini Ragini**

📧 Email: raginisriharshini@gmail.com

🔗 LinkedIn:
https://linkedin.com/in/sriharshini-ragini-1baaa9309

💻 GitHub:
https://github.com/Sriharshini2428

---

# ⭐ If you found this project useful, please consider giving it a Star on GitHub!
