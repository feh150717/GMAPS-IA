import os
import requests

ZAPI_INSTANCE = os.getenv("ZAPI_INSTANCE")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

def enviar_mensagem(telefone, texto):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}/send-text"

    payload = {
        "phone": telefone,
        "message": texto
    }

    response = requests.post(url, json=payload)

    try:
        return response.json()
    except:
        return {"error": "Invalid response", "status_code": response.status_code, "text": response.text}
