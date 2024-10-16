import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, override=True)

TOKEN = str(os.environ.get("TOKEN"))
WEATHER_API_KEY = str(os.environ.get("WEATHER_API_KEY"))
