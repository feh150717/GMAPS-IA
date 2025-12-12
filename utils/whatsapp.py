import os
import requests

ZAPI_INSTANCE = os.getenv("ZAPI_INSTANCE")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

API_URL = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}"

def enviar_mensagem(telefone, texto):
    url = f"{API_URL}/send-text"

    payload = {
        "phone": telefone,
        "message": texto
    }

    try:
        response = requests.post(url, json=payload)
        print("➡️ Enviando mensagem para:", telefone)
        print("➡️ Texto:", texto)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
