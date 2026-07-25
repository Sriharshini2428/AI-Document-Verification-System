import sqlite3

DB_NAME = "verification_history.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document TEXT,
        aadhaar TEXT,
        gender TEXT,
        dob TEXT,
        score INTEGER,
        status TEXT,
        face_found TEXT,
        qr_found TEXT,
        image_quality TEXT,
        ocr_quality TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_history(
    document,
    aadhaar,
    gender,
    dob,
    score,
    status,
    face_found,
    qr_found,
    image_quality,
    ocr_quality
):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO history(
        document,
        aadhaar,
        gender,
        dob,
        score,
        status,
        face_found,
        qr_found,
        image_quality,
        ocr_quality
    )
    VALUES(?,?,?,?,?,?,?,?,?,?)
    """, (
        document,
        aadhaar,
        gender,
        dob,
        score,
        status,
        str(face_found),
        str(qr_found),
        image_quality,
        ocr_quality
    ))

    conn.commit()
    conn.close()


def load_history():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history ORDER BY id DESC")

    rows = cursor.fetchall()

    conn.close()

    return rows