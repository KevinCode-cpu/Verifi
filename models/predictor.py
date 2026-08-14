from pathlib import Path
import sys

import joblib


PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)


MODEL_DIR = Path(__file__).resolve().parent

MODEL_PATH = MODEL_DIR / "fake_news_model.pkl"
VECTORIZER_PATH = MODEL_DIR / "tfidf_vectorizer.pkl"


model = joblib.load(MODEL_PATH)

vectorizer = joblib.load(VECTORIZER_PATH)


def clean_text(text):

    import re

    text = str(text)

    text = text.lower()

    text = re.sub(
        r"https?://\S+|www\.\S+",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def predict_news(text):

    cleaned_text = clean_text(text)

    vector = vectorizer.transform(
        [cleaned_text]
    )

    prediction = model.predict(
        vector
    )[0]

    if prediction == 0:
        return "Fake"

    return "Real"