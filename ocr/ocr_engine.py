import json
import os

import numpy as np
from PIL import Image

os.environ.setdefault("PADDLE_PDX_EAGER_INIT", "0")

from paddleocr import PaddleOCR


# =========================================================
# PADDLEOCR ENGINE
# =========================================================

ocr = PaddleOCR(
    lang="en"
)


# =========================================================
# EXTRACT TEXT FROM STREAMLIT UPLOAD
# =========================================================

def extract_text_from_image(image_file) -> str:

    if image_file is None:
        return ""

    try:

        # Read Streamlit UploadedFile
        image_file.seek(0)

        image = Image.open(
            image_file
        ).convert("RGB")

        # Convert PIL image to NumPy array
        image_array = np.array(
            image
        )

        # Run PaddleOCR
        results = ocr.predict(
            image_array
        )

        extracted_lines = []

        for result in results:

            data = result.json

            # Handle either dictionary or JSON string
            if isinstance(data, str):
                data = json.loads(data)

            if not isinstance(data, dict):
                continue

            result_data = data.get(
                "res",
                data
            )

            texts = result_data.get(
                "rec_texts",
                []
            )

            for text in texts:

                if text is None:
                    continue

                text = str(
                    text
                ).strip()

                if text:

                    extracted_lines.append(
                        text
                    )

        return "\n".join(
            extracted_lines
        ).strip()

    except Exception as error:

        raise RuntimeError(
            f"OCR failed: {error}"
        )