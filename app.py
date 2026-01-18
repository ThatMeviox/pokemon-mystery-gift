from fastapi import FastAPI
from pydantic import BaseModel
import json
import os
from datetime import datetime

app = FastAPI()
NEWS_FILE = "news_data.json"

class NewsItem(BaseModel):
    title: str
    content: str
    color: str

# Funkcja wczytująca newsy z pliku przy starcie
def load_news():
    if os.path.exists(NEWS_FILE):
        with open(NEWS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Funkcja zapisująca newsy do pliku
def save_news(news_list):
    with open(NEWS_FILE, "w", encoding="utf-8") as f:
        json.dump(news_list, f, ensure_ascii=False, indent=4)

news_db = load_news()

@app.get("/news")
def get_news():
    return news_db

@app.post("/add_news")
def add_news(item: NewsItem):
    new_entry = item.dict()
    # AUTOMATYCZNA DATA:
    new_entry["date"] = datetime.now().strftime("%d.%m.%2026") 
    
    news_db.insert(0, new_entry) # Dodaj na początek listy
    save_news(news_db) # Zapisz do pliku
    return {"message": "News added successfully"}
