from typing import List, Dict

try:
    import spacy
    _SPACY_OK = True
except Exception:
    spacy = None
    _SPACY_OK = False

_nlp_en = None
_nlp_zh = None

LABEL_MAP = {
    "PERSON": "NAME",
    "GPE": "LOCATION",
    "LOC": "LOCATION",
    "ORG": "ORG",
    "DATE": "DATE",
}

def _load():
    global _nlp_en, _nlp_zh
    if not _SPACY_OK:
        return
    if _nlp_en is None:
        try:
            _nlp_en = spacy.load("en_core_web_sm")
        except Exception:
            _nlp_en = None
    if _nlp_zh is None:
        try:
            _nlp_zh = spacy.load("zh_core_web_sm")
        except Exception:
            _nlp_zh = None

def _has_cjk(text: str) -> bool:
    return any('\u4e00' <= ch <= '\u9fff' for ch in text)

def ner_detect(text: str) -> List[Dict]:
    if not _SPACY_OK:
        return []
    _load()
    use_zh = _has_cjk(text) and (_nlp_zh is not None)
    nlp = _nlp_zh if use_zh else _nlp_en
    if nlp is None:
        return []
    doc = nlp(text)
    out: List[Dict] = []
    for ent in doc.ents:
        mapped = LABEL_MAP.get(ent.label_, None)
        if mapped:
            out.append({
                "start": ent.start_char,
                "end": ent.end_char,
                "label": mapped,
                "confidence": 0.9
            })
    return out
