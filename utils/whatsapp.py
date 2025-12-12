import requests
from .config import API_URL, API_ID, API_TOKEN

def enviar_mensagem(phone, mensagem):
    url = f"{API_URL}/send-text"

    payload = {
        "phone": phone,
        "message": mensagem
    }

    headers = {
        "Content-Type": "application/json",
        "Client-Token": API_TOKEN,
        "Instance-Id": API_ID
    }

    response = requests.post(url, json=payload, headers=headers)

    print("Resposta Z-API:", response.text)

    return response.json()
