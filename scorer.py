# scorer.py

import re


STOP_WORDS = {
    # Articles & Quantifiers
    "a", "an", "the", "all", "any", "both", "each", "few", "more", "most", 
    "other", "some", "such", "no", "nor", "not", "only", "own", "same",

    # Pronouns
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", 
    "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", 
    "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", 
    "their", "theirs", "themselves", "what", "which", "who", "whom", "this", 
    "that", "these", "those",

    # Verbs & Auxiliaries
    "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", 
    "had", "having", "do", "does", "did", "doing", "can", "could", "will", 
    "would", "shall", "should", "may", "might", "must",

    # Prepositions
    "about", "above", "across", "after", "against", "along", "among", "around", 
    "at", "before", "behind", "below", "beneath", "beside", "between", "beyond", 
    "by", "down", "during", "for", "from", "in", "into", "near", "of", "off", 
    "on", "onto", "out", "over", "through", "to", "toward", "under", "until", 
    "up", "upon", "with", "within", "without",

    # Conjunctions & Adverbs
    "and", "but", "if", "or", "because", "as", "while", "of", "at", "by", 
    "for", "with", "about", "against", "between", "into", "through", "during", 
    "before", "after", "above", "below", "to", "from", "up", "down", "in", 
    "out", "on", "off", "over", "under", "again", "further", "then", "once", 
    "here", "there", "when", "where", "why", "how", "so", "than", "too", 
    "very", "just"
}


def _content_words(text: str) -> set[str]:
    """Return lowercase words from text after removing common stop words."""
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {word for word in words if word not in STOP_WORDS}


def judge(question: str, expects: str, answer: str, results) -> bool:
    """
    Return True when every expected content word appears in the answer.

    Stop words are ignored, and the expected words do not need to appear in
    the same order.
    """
    expected_words = _content_words(expects)
    if not expected_words:
        return False

    answer_words = _content_words(answer or "")
    return expected_words <= answer_words
