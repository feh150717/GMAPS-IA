@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook recebido:", data)

    # JSON real da Z-API
    message = data.get("message", {})

    texto = message.get("text", {}).get("message", "")
    phone = message.get("phone", "")

    if not texto or not phone:
        return jsonify({"status": "ignored"})

    resposta = gerar_resposta(texto)

    enviar_mensagem(phone, resposta)

    return jsonify({"status": "sent"})
