import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

def get_sqorz_countries():
    base_url = os.getenv("SQORZ_API_BASE_ENDPOINT")
    api_route = "orgs"
    print("[DEBUG] - ", base_url+api_route)
    result = requests.get(base_url + api_route)
    return result._content

def get_sqorz_comities():
    base_url = os.getenv("SQORZ_API_BASE_ENDPOINT")
    print(base_url)
    return "comities"

def get_sqorz_events():
    return "events"

def get_sqorz_rider():
    return "rider"