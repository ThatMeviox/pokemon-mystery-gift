from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()
DB_FILE = "database.json"

# Model danych dla Newsów
class NewsItem(BaseModel):
    title: str
    content: str
    date: str
    color: str

# Inicjalizacja prostej bazy danych w pliku
def load_db():
    if not os.path.exists(DB_FILE):
        return {"news": []}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

@app.get("/news", response_model=List[NewsItem])
async def get_news():
    db = load_db()
    return db["news"]

@app.post("/add_news")
async def add_news(item: NewsItem):
    db = load_db()
    db["news"].insert(0, item.dict()) # Dodaj na początek listy
    save_db(db)
    return {"message": "News added successfully!"}

# Endpoint testowy, żebyś widział czy serwer żyje
@app.get("/")
async def root():
    return {"status": "PokeNet API Online", "version": "0.1.0"}
