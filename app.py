from flask import Flask, request, jsonify
from utils.ai import gerar_resposta
from utils.whatsapp import enviar_mensagem

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook recebido:", data)

    # JSON REAL DA Z-API:
    # {
    #     "text": "Olá",
    #     "phone": "5511919588710"
    # }

    texto = data.get("text", "")
    phone = data.get("phone", "")

    if not texto or not phone:
        print("Mensagem ignorada. JSON inválido.")
        return jsonify({"status": "ignored"})

    # GERA A RESPOSTA DA IA
    resposta = gerar_resposta(texto)

    # ENVIA A RESPOSTA PARA O WHATSAPP VIA Z-API
    enviar_mensagem(phone, resposta)

    return jsonify({"status": "sent"})

@app.route("/", methods=["GET"])
def home():
    return "GMaps IA ONLINE"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
