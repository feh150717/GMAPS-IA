import requests
from config import ZAPI_INSTANCE, ZAPI_TOKEN

BASE_URL = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}"

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
