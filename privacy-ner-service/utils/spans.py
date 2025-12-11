from typing import List, Dict

PRIORITY = {
    "CREDENTIALS": 3, "CARD": 3, "ID": 3,
    "HEALTH": 2, "FINANCE": 2, "NAME": 2, "LOCATION": 2, "ORG": 2,
    "PHONE": 2, "EMAIL": 2, "DATE": 1
}

def merge_spans(text: str, spans: List[Dict]) -> List[Dict]:
    # Merge overlapping/adjacent spans by priority then length.
    if not spans:
        return []
    spans = sorted(spans, key=lambda x: (x["start"], -PRIORITY.get(x["label"],1), -(x["end"]-x["start"])) )
    merged: List[Dict] = []
    for s in spans:
        if not merged:
            merged.append(s); continue
        last = merged[-1]
        if s["start"] <= last["end"]:
            s_pri = PRIORITY.get(s["label"],1); l_pri = PRIORITY.get(last["label"],1)
            s_len = s["end"]-s["start"]; l_len = last["end"]-last["start"]
            if s_pri > l_pri or (s_pri == l_pri and s_len > l_len):
                merged[-1] = s
        else:
            merged.append(s)
    n = len(text)
    for m in merged:
        m["start"] = max(0, min(m["start"], n))
        m["end"]   = max(m["start"], min(m["end"], n))
    return merged
