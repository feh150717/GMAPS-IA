from flask import Flask, request, jsonify
from utils.ai import gerar_resposta
from utils.whatsapp import enviar_mensagem

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("===== 📩 WEBHOOK RECEBIDO =====")
    print(data)

    texto = data.get("text", "")
    telefone = data.get("phone", "")

    if not texto or not telefone:
        print("❌ Dados incompletos no webhook")
        return jsonify({"status": "ignored"})

    # 🔥 GERA A RESPOSTA DA IA
    resposta = gerar_resposta(texto)
    print("🤖 IA respondeu:", resposta)

    # 🔥 ENVIA A RESPOSTA PARA O WHATSAPP
    retorno = enviar_mensagem(telefone, resposta)
    print("📤 Retorno do envio Z-API:", retorno)

    return jsonify({"status": "sent"})

@app.route("/", methods=["GET"])
def home():
    return "GMAPS IA ONLINE"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
