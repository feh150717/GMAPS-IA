from flask import Flask, request, jsonify
from utils.ai import gerar_resposta
from utils.whatsapp import enviar_mensagem

# Criar servidor Flask
app = Flask(__name__)

# Rota Webhook da Z-API
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook recebido:", data)

    # Extrair conteúdo conforme o novo padrão da Z-API
    message = data.get("message", {})

    texto = message.get("text", {}).get("message", "")
    phone = message.get("phone", "")

    print("Texto recebido:", texto)
    print("Telefone:", phone)

    # Ignorar mensagens sem texto ou sem phone
    if not texto or not phone:
        return jsonify({"status": "ignored"})

    # Gerar resposta IA
    resposta = gerar_resposta(texto)

    # Enviar resposta pelo WhatsApp
    enviar_mensagem(phone, resposta)

    return jsonify({"status": "sent"})


# Rota principal (apenas para teste)
@app.route("/", methods=["GET"])
def home():
    return "GMAPS IA ONLINE"


# Rodar servidor (necessário para Render)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
