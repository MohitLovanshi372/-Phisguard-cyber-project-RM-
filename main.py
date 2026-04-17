
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

HF_TOKEN = os.getenv("HF_TOKEN")
VT_API_KEY = os.getenv("VT_API_KEY")

class InputData(BaseModel):
    input_text: str

def ai_check(text):
    API_URL = "https://api-inference.huggingface.co/models/mrm8488/bert-tiny-finetuned-sms-spam-detection"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    res = requests.post(API_URL, headers=headers, json={"inputs": text})
    return res.json()

def vt_check(url):
    headers = {"x-apikey": VT_API_KEY}
    res = requests.post(
        "https://www.virustotal.com/api/v3/urls",
        headers=headers,
        data={"url": url}
    )
    return res.status_code

@app.post("/analyze")
def analyze(data: InputData):
    text = data.input_text
    words = text.split()
    urls = [w for w in words if "http" in w]

    vt_result = None
    if urls:
        vt_result = vt_check(urls[0])

    ai_result = ai_check(text)

    return {
        "ai_result": ai_result,
        "virustotal_status": vt_result
    }
