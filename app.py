from flask import Flask, request, jsonify
from utils.ai import gerar_resposta
from utils.whatsapp import enviar_mensagem

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    # Padrão que a Z-API envia:
    msg = data.get("data", {}).get("message", {}).get("text", "")
    phone = data.get("data", {}).get("phone", "")

    if not msg or not phone:
        return jsonify({"status": "ignored"})

    resposta = gerar_resposta(msg)
    enviar_mensagem(phone, resposta)

    return jsonify({"status": "sent"})

@app.route("/", methods=["GET"])
def home():
    return "GMAPS IA ONLINE"
