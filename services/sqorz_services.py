import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

def get_sqorz_countries():
    return "countries"

def get_sqorz_comities():
    base_url = os.getenv("SQORZ_API_BASE_ENDPOINT")
    print(base_url)
    return "comities"

def get_sqorz_events():
    return "events"

def get_sqorz_rider():
    return "rider"