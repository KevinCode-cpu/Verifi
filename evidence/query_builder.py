import re


def clean_claim(claim):

    return re.sub(
        r"\s+",
        " ",
        claim.strip()
    )


def build_search_queries(
    claim,
    deep=False
):

    if not claim:
        return []

    claim = clean_claim(claim)

    lower = claim.lower()

    queries = [
        claim,
        f'"{claim}"'
    ]

    # =====================================================
    # SCIENTIFIC / PHYSICAL FACTS
    # =====================================================

    if any(
        word in lower
        for word in [
            "water",
            "temperature",
            "freezes",
            "freezing",
            "earth",
            "sun",
            "moon",
            "gravity",
            "planet",
            "ocean",
            "mount everest"
        ]
    ):

        queries.extend([
            claim + " scientific source",
            claim + " official source",
            claim + " NASA",
            claim + " NOAA"
        ])

    # =====================================================
    # WATER FREEZING
    # =====================================================

    if (
        "water" in lower
        and any(
            word in lower
            for word in [
                "freeze",
                "freezes",
                "freezing"
            ]
        )
    ):

        queries.extend([
            "freezing point of pure water Celsius NIST",
            "water freezing point standard pressure NIST",
            "water freezes 0 Celsius NIST",
            "water freezing point 32 Fahrenheit",
            "water freezing point standard atmospheric pressure",
            "site:nist.gov water freezing point",
            "site:usgs.gov water freezing point"
        ])

    # =====================================================
    # EARTH / SUN
    # =====================================================

    if (
        "earth" in lower
        and "sun" in lower
    ):

        queries.extend([
            "Earth revolves around Sun NASA",
            "Earth orbits the Sun NASA",
            "Earth revolution around Sun scientific source",
            "Earth orbit Sun official"
        ])

    # =====================================================
    # EVEREST
    # =====================================================

    if "everest" in lower:

        queries.extend([
            "Mount Everest highest mountain above sea level NOAA",
            "Mount Everest highest elevation above sea level",
            "Mount Everest highest mountain official",
            "Mount Everest height NOAA",
            "Mount Everest highest point sea level Britannica"
        ])

    # =====================================================
    # OCEANS
    # =====================================================

    if "ocean" in lower:

        queries.extend([
            claim + " NOAA",
            claim + " official source",
            "Pacific Ocean largest ocean NOAA",
            "largest ocean on Earth official"
        ])

    # =====================================================
    # POPULATION
    # =====================================================

    if (
        "population" in lower
        or "populous" in lower
    ):

        queries.extend([
            claim + " UN population",
            claim + " official population",
            claim + " population latest",
            claim + " population ranking"
        ])

    # =====================================================
    # HISTORICAL CLAIMS
    # =====================================================

    if any(
        word in lower
        for word in [
            "founded",
            "established",
            "created",
            "discovered",
            "born",
            "died"
        ]
    ):

        queries.extend([
            claim + " official source",
            claim + " history",
            claim + " historical source"
        ])

    # =====================================================
    # UNITED NATIONS
    # =====================================================

    if "united nations" in lower:

        queries.extend([
            "United Nations founded 1945 official",
            "United Nations established 1945 UN",
            "United Nations Charter 1945",
            "United Nations history founding date"
        ])

    # =====================================================
    # NUMERICAL CLAIMS
    # =====================================================

    if re.search(
        r"\d+(?:\.\d+)?",
        claim
    ):

        queries.extend([
            claim + " official data",
            claim + " authoritative source",
            claim + " fact check"
        ])

    # =====================================================
    # FUTURE / PREDICTION
    # =====================================================

    if any(
        word in lower
        for word in [
            "will",
            "by 2030",
            "by 2040",
            "by 2050",
            "future",
            "prediction",
            "forecast"
        ]
    ):

        queries.extend([
            claim + " projection",
            claim + " forecast",
            claim + " scientific projection",
            claim + " official report"
        ])

    # =====================================================
    # GENERAL
    # =====================================================

    queries.extend([
        claim + " official source",
        claim + " reliable source",
        claim + " evidence",
        claim + " fact check"
    ])

    # =====================================================
    # DEEP MODE
    # =====================================================

    if deep:

        queries.extend([
            claim + " Reuters",
            claim + " AP News",
            claim + " BBC",
            claim + " fact check",
            claim + " official report"
        ])

    # =====================================================
    # REMOVE DUPLICATES
    # =====================================================

    unique = []
    seen = set()

    for query in queries:

        normalized = query.lower().strip()

        if normalized in seen:
            continue

        seen.add(normalized)

        unique.append(query)

    return unique