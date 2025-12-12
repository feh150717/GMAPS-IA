from flask import Flask, request, jsonify
from utils.ai import gerar_resposta
from utils.whatsapp import enviar_mensagem

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    print("Webhook recebido:", data)

    # NOVO PADRÃO da Z-API (correto)
    message = data.get("message", {})
    msg = message.get("text", "")
    phone = message.get("from", "")

    if not msg or not phone:
        return jsonify({"status": "ignored"})

    resposta = gerar_resposta(msg)

    enviar_mensagem(phone, resposta)

    return jsonify({"status": "sent"})

@app.route("/", methods=["GET"])
def home():
    return "GMAPS IA ONLINE"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
