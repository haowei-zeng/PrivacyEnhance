import re
from typing import List, Dict

RULES = {
    "PHONE": re.compile(r"\b(\+?\d{1,3}[-.\s]?)?(\d{3}[-.\s]?){2}\d{4}\b"),
    "EMAIL": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "CARD": re.compile(r"\b(?:\d[ -]*?){13,19}\b"),
    "ID": re.compile(r"\b\d{17}[\dXx]\b"),
    "CREDENTIALS": re.compile(r"\b(pass(word)?|token|api[_-]?key|secret)\b[:= ]", re.I),
}

def regex_detect(text: str) -> List[Dict]:
    out: List[Dict] = []
    for label, pat in RULES.items():
        for m in pat.finditer(text):
            out.append({
                "start": m.start(),
                "end": m.end(),
                "label": label,
                "confidence": 1.0
            })
    return out
