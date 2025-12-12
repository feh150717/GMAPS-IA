import requests
from utils.config import API_URL

def enviar_mensagem(phone, mensagem):
    url = f"{API_URL}/messages"

    payload = {
        "messages": [
            {
                "whatsappId": phone,
                "text": str(mensagem)
            }
        ]
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    print("Resposta Z-API:", response.text)

    return response.json()
