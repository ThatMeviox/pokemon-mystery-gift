from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import time
import json
import os

app = FastAPI()

# Model danych newsa
class NewsItem(BaseModel):
    title: str
    content: str
    color: str = "#5865F2"

# Ścieżka do pliku z danymi
STORAGE_FILE = "news_storage.json"

def load_news():
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def save_news(news_list):
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(news_list, f, ensure_ascii=False, indent=4)

@app.get("/news")
async def get_news():
    news = load_news()
    # SORTOWANIE: Najnowsze newsy (wyższy timestamp) będą PIERWSZE na liście
    # Dzięki temu BotGhost widzi najnowszego newsa pod indeksem .1
    sorted_news = sorted(news, key=lambda x: x.get('timestamp', 0), reverse=True)
    return sorted_news

@app.post("/add_news")
async def add_news(item: NewsItem):
    news = load_news()
    
    new_entry = {
        "title": item.title,
        "content": item.content,
        "color": item.color,
        "timestamp": time.time()  # Automatyczne dodawanie czasu
    }
    
    news.append(new_entry)
    save_news(news)
    return {"status": "success", "message": "News added!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
