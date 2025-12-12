from flask import Flask, request, jsonify
from utils.ai import gerar_resposta
from utils.whatsapp import enviar_mensagem

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("===== 📩 WEBHOOK RECEBIDO =====")
    print(data)

    # CAPTURA TEXTO E TELEFONE
    texto = data.get("text", "")
    phone = data.get("phone", "")

    if not texto or not phone:
        print("Mensagem inválida.")
        return jsonify({"status": "ignored"})

    # GERA RESPOSTA DA IA
    resposta = gerar_resposta(texto)

    # GARANTE QUE A RESPOSTA SEJA STRING
    resposta = str(resposta)

    # ENVIA PARA A Z-API
    enviar_mensagem(phone, resposta)

    return jsonify({"status": "sent"})


@app.route("/", methods=["GET"])
def home():
    return "GMAPS IA ONLINE"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

