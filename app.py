from flask import Flask, request, jsonify
from utils.ai import gerar_resposta
from utils.whatsapp import enviar_mensagem

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json
        print("\n===== 📥 WEBHOOK RECEBIDO =====")
        print(data)

        # Extrai texto da mensagem
        texto = (
            data.get("text")
            or data.get("message")
            or data.get("body")
            or data.get("lastMessage")
            or ""
        )

        # Extrai telefone da mensagem
        phone = (
            data.get("phone")
            or data.get("from")
            or data.get("sender")
            or ""
        )

        if not texto or not phone:
            print("⚠️ JSON ignorado: faltando texto ou telefone")
            return jsonify({"status": "ignored"}), 200

        print(f"📌 Mensagem recebida de {phone}: {texto}")

        # Gera resposta da IA
        resposta = gerar_resposta(texto)
        print(f"🤖 Resposta da IA: {resposta}")

        # Envia resposta pelo WhatsApp
        ZAPI_retorno = enviar_mensagem(phone, resposta)
        print("📤 Retorno da Z-API:", ZAPI_retorno)

        return jsonify({"status": "sent"}), 200

    except Exception as e:
        print("❌ ERRO NO WEBHOOK:", str(e))
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def home():
    return "GMAPS IA ONLINE"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
