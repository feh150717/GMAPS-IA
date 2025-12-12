@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    print("Webhook recebido:", data)

    # A Z-API envia a mensagem neste formato:
    message = data.get("message", {})

    msg = message.get("text", "")
    phone = message.get("from", "")

    if not msg or not phone:
        return jsonify({"status": "ignored"})

    resposta = gerar_resposta(msg)

    enviar_mensagem(phone, resposta)

    return jsonify({"status": "sent"})
