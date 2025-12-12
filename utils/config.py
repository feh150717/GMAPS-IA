import os

API_ID = os.getenv("ZAPI_INSTANCE")
API_TOKEN = os.getenv("ZAPI_TOKEN")

API_URL = f"https://api.z-api.io/instances/{API_ID}/token/{API_TOKEN}"
