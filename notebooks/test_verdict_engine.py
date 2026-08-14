import sys
from pathlib import Path


PROJECT_ROOT = (
    Path(__file__).resolve().parent.parent
)

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)


from evidence.verdict_engine import (
    calculate_claim_verdict,
    calculate_overall_verdict
)


# =========================================================
# TEST 1 — STRONG SUPPORT
# =========================================================

supporting_evidence = [

    {
        "domain": "reuters.com",
        "publisher_id": "reuters",
        "source_score": 98,
        "relevance_score": 0.90,
        "relationship": "entailment",
        "nli_confidence": 0.95
    },

    {
        "domain": "bbc.com",
        "publisher_id": "bbc",
        "source_score": 96,
        "relevance_score": 0.85,
        "relationship": "entailment",
        "nli_confidence": 0.93
    },

    {
        "domain": "apnews.com",
        "publisher_id": "associated_press",
        "source_score": 98,
        "relevance_score": 0.80,
        "relationship": "entailment",
        "nli_confidence": 0.91
    }
]


# =========================================================
# TEST 2 — STRONG CONTRADICTION
# =========================================================

contradicting_evidence = [

    {
        "domain": "reuters.com",
        "publisher_id": "reuters",
        "source_score": 98,
        "relevance_score": 0.90,
        "relationship": "contradiction",
        "nli_confidence": 0.96
    },

    {
        "domain": "bbc.com",
        "publisher_id": "bbc",
        "source_score": 96,
        "relevance_score": 0.85,
        "relationship": "contradiction",
        "nli_confidence": 0.94
    },

    {
        "domain": "apnews.com",
        "publisher_id": "associated_press",
        "source_score": 98,
        "relevance_score": 0.80,
        "relationship": "contradiction",
        "nli_confidence": 0.92
    }
]


# =========================================================
# TEST 3 — MIXED EVIDENCE
# =========================================================

mixed_evidence = [

    {
        "domain": "reuters.com",
        "publisher_id": "reuters",
        "source_score": 98,
        "relevance_score": 0.90,
        "relationship": "entailment",
        "nli_confidence": 0.90
    },

    {
        "domain": "bbc.com",
        "publisher_id": "bbc",
        "source_score": 96,
        "relevance_score": 0.90,
        "relationship": "contradiction",
        "nli_confidence": 0.90
    }
]


print("=" * 70)
print("VERIFI VERDICT ENGINE TEST")
print("=" * 70)


for name, evidence in [
    ("STRONG SUPPORT", supporting_evidence),
    ("STRONG CONTRADICTION", contradicting_evidence),
    ("MIXED EVIDENCE", mixed_evidence)
]:

    print(
        "\n" + "=" * 70
    )

    print(
        name
    )

    result = calculate_claim_verdict(
        evidence
    )

    print(
        "Verdict:",
        result["verdict"]
    )

    print(
        "Confidence:",
        result["confidence"]
    )

    print(
        "Support:",
        result["support_score"]
    )

    print(
        "Contradiction:",
        result["contradiction_score"]
    )

    print(
        "Supporting sources:",
        result["supporting_sources"]
    )

    print(
        "Contradicting sources:",
        result["contradicting_sources"]
    )


# =========================================================
# OVERALL TEST
# =========================================================

print(
    "\n" + "=" * 70
)

print(
    "OVERALL VERDICT TEST"
)

claim_results = [

    {
        "verdict": "Supported",
        "confidence": 0.91,
        "support_score": 2.5,
        "contradiction_score": 0.0
    },

    {
        "verdict": "Supported",
        "confidence": 0.88,
        "support_score": 2.1,
        "contradiction_score": 0.0
    }

]


overall = calculate_overall_verdict(
    claim_results
)

print(
    "Final verdict:",
    overall["verdict"]
)

print(
    "Confidence:",
    overall["confidence"]
)