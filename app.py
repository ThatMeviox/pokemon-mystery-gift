from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import time
from datetime import datetime  # Dodane do formatowania daty
import json
import os

app = FastAPI()

class NewsItem(BaseModel):
    title: str
    content: str
    color: str = "#5865F2"

STORAGE_FILE = "news_storage.json"

def load_news():
    if not os.path.exists(STORAGE_FILE): return []
    with open(STORAGE_FILE, "r", encoding="utf-8") as f:
        try: return json.load(f)
        except: return []

def save_news(news_list):
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(news_list, f, ensure_ascii=False, indent=4)

@app.get("/news")
async def get_news():
    news = load_news()
    # Sortowanie: najnowsze na górze
    sorted_news = sorted(news, key=lambda x: x.get('timestamp', 0), reverse=True)
    return sorted_news

@app.post("/add_news")
async def add_news(item: NewsItem):
    news = load_news()
    
    now = datetime.now()
    timestamp = time.time()
    # Tworzymy ładny format daty: Dzień.Miesiąc.Rok Godzina:Minuta
    readable_date = now.strftime("%d.%碰.%Y %H:%M") 
    
    new_entry = {
        "title": item.title,
        "content": item.content,
        "color": item.color,
        "timestamp": timestamp,
        "date_readable": readable_date  # TO POLE WYKORZYSTASZ W BOTGHOST
    }
    
    news.append(new_entry)
    save_news(news)
    return {"status": "success", "message": "News added!"}
