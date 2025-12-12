import requests
import os
from utils.config import API_URL, INSTANCE_TOKEN

def enviar_mensagem(phone, mensagem):
    url = f"{API_URL}/send-text"

    payload = {
        "phone": phone,
        "message": mensagem
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {INSTANCE_TOKEN}"
    }

    response = requests.post(url, json=payload, headers=headers)

    print("Resposta Z-API:", response.text)

    return response.json()
