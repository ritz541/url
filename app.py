from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from functions import to_base

app = FastAPI()
db = {}
counter = 1


class URLRequest(BaseModel):
    long_url: str


@app.get("/")
def home():
    return {"message": "URL shortener is working. Go to /docs to shorten"}


@app.post("/shorten")
def shorten_url(req: URLRequest):
    global counter
    code = to_base(counter)
    db[code] = req.long_url
    counter += 1
    return {"short_code": code, "short_url": f"https://localhost:8000/{code}"}


@app.get("/{code}")
def redirect_url(code: str):
    long_url = db.get(code)
    if long_url:
        return RedirectResponse(long_url)
    return {"error": "not found"}
