from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from functions import to_base
import json
import os

app = FastAPI()
DB_FILE = "db.json"
counter = 1
db = {}


def load_db():
    global db, counter
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            db = data.get("urls", {})
            counter = data.get("counter", len(db) + 1)
            print(f"Loaded {len(db)} urls from {DB_FILE}, counter={counter}")
    else:
        print("No db file, starting fresh")


def save_db():
    with open(DB_FILE, "w") as f:
        json.dump({"counter": counter, "urls": db}, f, indent=2)


load_db()


class URLRequest(BaseModel):
    long_url: str


@app.get("/")
def home():
    return {"message": "URL shortener is running", "total urls": len(db)}


@app.post("/shorten")
def shorten_url(req: URLRequest):
    global counter
    code = to_base(counter)
    db[code] = req.long_url
    counter += 1
    save_db()
    return {"short_code": code, "short_url": f"https://localhost:8000/{code}"}


@app.get("/{code}")
def redirect_url(code: str):
    long_url = db.get(code)
    if long_url:
        return RedirectResponse(long_url)
    return {"error": "not found"}
