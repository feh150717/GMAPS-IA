from flask import Flask, request, jsonify
from utils.ai import gerar_resposta
from utils.whatsapp import enviar_mensagem

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    print("Webhook recebido:", data)

    # JSON REAL da Z-API:
    texto = data.get("text", {}).get("message", "")
    phone = data.get("phone", "")

    # Se não houver texto ou número, ignora
    if not texto or not phone:
        return jsonify({"status": "ignored"})

    # Gera resposta da IA
    resposta = gerar_resposta(texto)

    # Envia ao cliente
    enviar_mensagem(phone, resposta)

    return jsonify({"status": "sent"})

@app.route("/", methods=["GET"])
def home():
    return "GMAPS IA ONLINE"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
