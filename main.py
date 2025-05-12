from fastapi import FastAPI
import requests
import os
from services.ai_services import *
from services.sqorz_services import *
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()

@app.get("/")
async def basic():
    print(os.getenv('AZURE_OPENAI_ENDPOINT'))
    #response = sqorz_api_chain.run("récupère les infos pour le comité ffc")
    # get_sqorz_comities()
    # print(response)
    return test("Ferenc")

@app.get("/event/test")
async def root():
    result = requests.get("https://our.sqorz.com/json/event/6453634f979fbdc2a0a63db8")
    return {"result": result.content}