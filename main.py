from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import HttpUrl
import requests
from bs4 import BeautifulSoup
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[  "https://email-extractor-ui.vercel.app/",
    "http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_emails_from_url(url: str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))

    soup = BeautifulSoup(response.text, 'html.parser')

    # Remove script and style tags before getting text
    for tag in soup(['script', 'style']):
        tag.decompose()

    clean_text = soup.get_text(separator=' ', strip=True)
    
    # Optionally limit to 254 chars (max email length)
    possible_emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", clean_text)
    return list(set(possible_emails))

@app.get("/extract-emails")
def get_emails(url: HttpUrl = Query(..., description="The webpage URL to extract emails from")):
    emails = extract_emails_from_url(str(url))
    return {"emails": emails}
