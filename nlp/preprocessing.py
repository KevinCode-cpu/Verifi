import re


def normalize_text(text: str) -> str:

    if not text:
        return ""

    # Convert multiple spaces/newlines into a single space
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text


def remove_urls(text: str) -> str:

    if not text:
        return ""

    text = re.sub(
        r"https?://\S+|www\.\S+",
        "",
        text
    )

    return text


def remove_extra_symbols(text: str) -> str:

    if not text:
        return ""

    # Keep letters, numbers and normal punctuation.
    text = re.sub(
        r"[^\w\s.,!?;:'\"%()\-]",
        " ",
        text
    )

    return text


def clean_text(text: str) -> str:

    if not text:
        return ""

    text = remove_urls(text)

    text = remove_extra_symbols(text)

    text = normalize_text(text)

    return text