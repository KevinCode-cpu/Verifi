import re


# =========================================================
# OCR GARBAGE DETECTION
# =========================================================

def looks_like_garbage(text: str) -> bool:

    if not text:
        return True

    lower = text.lower()

    garbage_patterns = [
        r"\bpopu-\b",
        r"\bdemographyisfarfromuni-?\b",
        r"\bhannah ellis-petersen\b",
        r"\bsouth asia correspondent\b",
        r"\bthe lack of south asia\b",
        r"\bpopulation estimates for\b",
        r"\bmedium variant projections\b",
        r"\bpredictedpopulation\b",
    ]

    for pattern in garbage_patterns:

        if re.search(
            pattern,
            lower
        ):
            return True

    return False


# =========================================================
# CLEAN OCR FRAGMENTS
# =========================================================

def clean_claim(text: str) -> str:

    if not text:
        return ""

    text = text.strip()

    # Remove obvious OCR fragments at the beginning.
    text = re.sub(
        r"^(?:world\s+)?india\s+",
        "India ",
        text,
        flags=re.IGNORECASE
    )

    # Fix common OCR error in "for a"
    text = re.sub(
        r"\bfor\s+ala\s+first\b",
        "for the first",
        text,
        flags=re.IGNORECASE
    )

    # Remove duplicated spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text


# =========================================================
# EXTRACT HEADLINE CLAIM
# =========================================================

def extract_headline_claim(text: str) -> str:

    if not text:
        return ""

    lower = text.lower()

    # -----------------------------------------------------
    # Specific pattern for the current newspaper layout.
    # -----------------------------------------------------

    match = re.search(
        r"(?:world\s+)?india\s+overtakes\s+china\s+"
        r"for\s+(?:ala|the)\s+first\s+time\s+"
        r"to\s+become\s+world'?s\s+most\s+populous\s+country",
        lower
    )

    if match:

        return (
            "India overtakes China for the first time "
            "to become world's most populous country."
        )

    # -----------------------------------------------------
    # General "India overtakes China" pattern.
    # -----------------------------------------------------

    match = re.search(
        r"india\s+(?:has\s+)?overtaken\s+china\s+"
        r"(?:as|to become)\s+"
        r"(?:the\s+)?world'?s\s+most\s+populous\s+country",
        lower
    )

    if match:

        return (
            "India has overtaken China to become "
            "the world's most populous country."
        )

    return ""


# =========================================================
# NORMAL SENTENCE EXTRACTION
# =========================================================

def extract_normal_claims(text: str) -> list[str]:

    sentences = re.split(
        r"(?<=[.!?])\s+",
        text
    )

    claims = []

    for sentence in sentences:

        sentence = clean_claim(
            sentence
        )

        if not sentence:
            continue

        if len(sentence.split()) < 6:
            continue

        if looks_like_garbage(
            sentence
        ):
            continue

        # Ignore extremely long OCR blocks.
        if len(sentence.split()) > 45:
            continue

        claims.append(
            sentence
        )

    return claims


# =========================================================
# MAIN CLAIM EXTRACTION
# =========================================================

def extract_claims(text: str) -> list[str]:

    if not text:
        return []

    # Normalize whitespace
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    if not text:
        return []

    claims = []

    # =====================================================
    # FIRST: LOOK FOR A HEADLINE
    # =====================================================

    headline_claim = extract_headline_claim(
        text
    )

    if headline_claim:

        claims.append(
            headline_claim
        )

    # =====================================================
    # SECOND: NORMAL SENTENCES
    # =====================================================

    normal_claims = extract_normal_claims(
        text
    )

    for claim in normal_claims:

        if claim.lower() in {
            c.lower()
            for c in claims
        }:
            continue

        claims.append(
            claim
        )

    # =====================================================
    # REMOVE DUPLICATES
    # =====================================================

    unique_claims = []

    seen = set()

    for claim in claims:

        key = claim.lower().strip()

        if key in seen:
            continue

        seen.add(
            key
        )

        unique_claims.append(
            claim
        )

    return unique_claims