from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
from detectors.regex_detector import regex_detect
from detectors.ner_detector import ner_detect
from utils.spans import merge_spans
from sanitizer import sanitize_with_rules

class AnalyzeReq(BaseModel):
    text: str

class Finding(BaseModel):
    start: int
    end: int
    label: str
    confidence: float

class SanitizeResp(BaseModel):
    sanitized: str
    findings: List[Finding]

app = FastAPI(title="Local PII NER Service", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    # "http://localhost", "http://127.0.0.1",
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health() -> Dict[str, Any]:
    return {"status": "ok"}

@app.post("/analyze", response_model=List[Finding])
def analyze(req: AnalyzeReq):
    text = req.text or ""
    rx = regex_detect(text)
    ner = ner_detect(text)
    merged = merge_spans(text, rx + ner)
    return [Finding(**m) for m in merged]

@app.post("/sanitize", response_model=SanitizeResp)
def sanitize(req: AnalyzeReq):
    findings = analyze(req)  # reuse
    sanitized = sanitize_with_rules(req.text, [f.model_dump() for f in findings])
    return SanitizeResp(sanitized=sanitized, findings=findings)
