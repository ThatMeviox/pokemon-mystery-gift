from fastapi import FastAPI
from pydantic import BaseModel
import json, os, time

app = FastAPI()
DB_FILE = "news_storage.json"

class NewsModel(BaseModel):
    title: str
    content: str

def get_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

@app.get("/news")
def list_news():
    return get_db()

@app.post("/add-news")
def create_news(data: NewsModel):
    current_db = get_db()
    
    new_entry = {
        "title": data.title,
        "content": data.content,
        "color": "#5865F2", # Kolor ustawiony na sztywno (PokeNet Blue)
        "timestamp": time.time() # Zapisuje dokładny czas w sekundach
    }
    
    current_db.insert(0, new_entry)
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(current_db, f, ensure_ascii=False, indent=4)
        
    return {"status": "success"}
