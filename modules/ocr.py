import easyocr
import numpy as np

# Load OCR model only once
reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image):

    image = np.array(image)

    results = reader.readtext(
        image,
        detail=0,
        paragraph=True,
        contrast_ths=0.05,
        adjust_contrast=0.7
    )

    text = "\n".join(results)

    return text