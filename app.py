from flask import Flask, request, jsonify
from utils.whatsapp import enviar_mensagem

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("📩 WEBHOOK RECEBIDO =>", data)

    try:
        texto = data["text"]["message"]
        telefone = data["phone"]
    except:
        return jsonify({"error": "invalid payload"}), 400

    # 🔥 LOG para confirmar que pegou tudo certo
    print("📞 Telefone:", telefone)
    print("📝 Texto:", texto)

    # === RESPOSTA AUTOMÁTICA ===
    if texto.lower() == "/teste":
        enviar_mensagem(telefone, "🔥 Teste recebido com sucesso! A integração está funcionando.")
        return jsonify({"status": "ok"})

    # Resposta padrão
    enviar_mensagem(telefone, "Olá! Sua mensagem foi recebida.")
    return jsonify({"status": "ok"})

@app.route("/")
def home():
    return "GMAPS-IA rodando!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
