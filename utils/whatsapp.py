import requests
from utils.config import API_URL

def enviar_mensagem(phone, mensagem):
    # O endpoint correto da sua instância é /send-text
    url = f"{API_URL}/send-text"

    payload = {
        "phone": phone,
        "message": str(mensagem)
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    print("Resposta Z-API:", response.text)

    return response.json()
