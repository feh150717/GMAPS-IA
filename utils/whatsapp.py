import requests
import os
from utils.config import API_URL

def enviar_mensagem(telefone, texto):

    # Sanitiza o número
    telefone = str(telefone).replace("+", "").replace(" ", "")
    if telefone.startswith("0"):
        telefone = telefone[1:]

    print("📞 Número sanitizado:", telefone)

    url = f"{API_URL}/send-text"

    payload = {
        "phone": telefone,
        "message": {
            "text": texto
        }
    }

    print("➡️ Enviando para Z-API:", payload)

    try:
        response = requests.post(url, json=payload)
        print("📨 Resposta Z-API:", response.text)
        return response.json()
    except Exception as e:
        print("❌ ERRO AO ENVIAR:", e)
        return {"error": str(e)}
