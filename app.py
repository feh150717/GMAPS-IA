from flask import Flask, request, jsonify
from utils.whatsapp import enviar_mensagem
import os

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("\n📩 WEBHOOK RECEBIDO =>", data)

    # Tenta extrair o texto da mensagem
    try:
        texto = data.get("text", {}).get("message", "")
        telefone = data.get("phone", "")

        if not telefone:
            return jsonify({"error": "phone missing"}), 400

        print("📞 Telefone:", telefone)
        print("💬 Texto:", texto)

    except Exception as e:
        print("❌ Erro ao ler webhook:", e)
        return jsonify({"error": "invalid payload"}), 400

    # Resposta automática para teste
    if texto.lower() == "/teste":
        enviar_mensagem(telefone, "🧪 Teste recebido com sucesso! A integração está funcionando.")
        return jsonify({"status": "ok"})

    # Resposta padrão
    enviar_mensagem(telefone, "Olá! Sua mensagem foi recebida.")
    return jsonify({"status": "ok"})


@app.route("/")
def home():
    return "GMAPS-IA rodando!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
