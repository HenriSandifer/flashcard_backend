from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import requests

app = FastAPI()

# CORS setup so Flutter can talk to this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # loosen later in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

S3_BASE_URL = "https://saudi-arabic-flash-cards.s3.amazonaws.com"

@app.get("/vocab")
def get_vocab():
    try:
        response = requests.get(f"{S3_BASE_URL}/vocab.json")
        return response.json()
    except:
        raise HTTPException(status_code=404, detail="vocab.json not found")

@app.get("/audio/{filename}")
def get_audio(filename: str):
    return {
        "url": f"{S3_BASE_URL}/audio/{filename}"
    }
