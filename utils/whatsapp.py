import requests
from utils.config import API_URL

def enviar_mensagem(telefone, texto):

    url = f"{API_URL}/send-text"

    payload = {
        "phone": telefone,
        "message": texto
    }

    response = requests.post(url, json=payload)

    try:
        return response.json()
    except:
        return {
            "error": "Erro ao interpretar resposta",
            "status_code": response.status_code,
            "text": response.text
        }
