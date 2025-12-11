
from typing import List, Dict

def redact(original: str, label: str) -> str:
    if label == "CARD":
        digits = "".join([c for c in original if c.isdigit()])
        tail = digits[-4:] if len(digits) >= 4 else ""
        return f"[CARD_****{tail}]"
    return f"[{label}]"

def sanitize_with_rules(text: str, findings: List[Dict]) -> str:
    # Replace from right to left to keep indices stable
    buf = list(text)
    for f in sorted(findings, key=lambda x: x["start"], reverse=True):
        start, end, label = f["start"], f["end"], f["label"]
        token = "".join(buf[start:end])
        rep = redact(token, label)
        buf[start:end] = list(rep)
    return "".join(buf)
