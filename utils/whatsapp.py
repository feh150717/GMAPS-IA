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

    print("➡️ Enviando para Z-API:", payload)

    try:
        response = requests.post(url, json=payload)
        print("📨 Resposta Z-API:", response.text)
        return response.json()
    except Exception as e:
        print("❌ ERRO AO ENVIAR:", e)
        return {"error": str(e)}
