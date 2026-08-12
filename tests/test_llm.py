"""
Tests LLM-as-a-Judge très simples.
Version basée sur des règles (facilement remplaçable par un vrai LLM).
"""


def simple_llm_judge(text: str, prediction: int) -> bool:
    """
    Juge très basique (règles + mots-clés).
    En production on utiliserait un vrai LLM-as-a-Judge.
    """
    positive_words = ["excellent", "super", "parfait", "recommande", "satisfait", "conforme"]
    negative_words = ["médiocre", "déçu", "horrible", "cassé", "mauvaise", "ne recommande pas"]

    text_lower = text.lower()
    if prediction == 1:
        return any(w in text_lower for w in positive_words) or not any(w in text_lower for w in negative_words)
    else:
        return any(w in text_lower for w in negative_words) or not any(w in text_lower for w in positive_words)


def test_llm_judge_consistency():
    samples = [
        ("Ce produit est excellent", 1),
        ("Qualité médiocre, je suis déçu", 0),
        ("Je rachèterai sans hésiter", 1),
        ("Je ne recommande pas du tout", 0),
    ]
    for text, label in samples:
        assert simple_llm_judge(text, label), f"Échec du juge sur : {text}"
