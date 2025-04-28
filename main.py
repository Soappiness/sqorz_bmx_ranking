from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def root():
    result = requests.get("https://our.sqorz.com/json/event/6453634f979fbdc2a0a63db8")
    return {"result": result.content}