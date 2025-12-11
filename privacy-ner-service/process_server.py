# process_server.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Local Processor")

class Req(BaseModel):
    text: str

@app.post("/process")
def process(req: Req):
    # 这里写你的逻辑：可以打分、存档、再调模型等
    # 先返回一个简单回显看看管道是否畅通
    return {
        "ok": True,
        "length": len(req.text),
        "preview": req.text[:80]
    }
