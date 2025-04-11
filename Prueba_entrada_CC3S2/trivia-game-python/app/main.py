# app/main.py
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"mensaje": "Bienvenido al juego de trivia"}
    