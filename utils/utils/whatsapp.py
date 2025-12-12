import requests
from config import ZAPI_TOKEN, ZAPI_PHONE

BASE_URL = f"https://api.z-api.io/instances/{ZAPI_PHONE}/token/{ZAPI_TOKEN}"

def enviar_mensagem(numero, mensagem):
    try:
        url = f"{BASE_URL}/send-text"
        payload = {
            "phone": numero,
            "message": mensagem
        }
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
