@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json
        print("==== RECEBI WEBHOOK ====")
        print(data)

        # Se não veio JSON, registra mesmo assim
        if data is None:
            print("ERRO: request.json veio vazio")
            return jsonify({"status": "invalid"}), 200

        # Captura todos os campos possíveis (Z-API às vezes muda o formato)
        texto = ""
        phone = ""

        # Opção 1: estrutura padrão
        if "text" in data:
            texto = data.get("text", {}).get("message", "")
        if "phone" in data:
            phone = data.get("phone", "")

        # Opção 2: estrutura alternativa
        if "message" in data:
            texto = data.get("message", "")
        if "from" in data:
            phone = data.get("from", "")

        print("Texto extraído:", texto)
        print("Phone extraído:", phone)

        if not texto or not phone:
            print("⚠ JSON inválido ou incompleto")
            return jsonify({"status": "ignored"}), 200

        # Gera resposta da IA
        resposta = gerar_resposta(texto)

        # Envia resposta ao WhatsApp
        enviar_mensagem(phone, resposta)

        return jsonify({"status": "sent"}), 200

    except Exception as e:
        print("ERRO NO WEBHOOK:", str(e))
        return jsonify({"error": str(e)}), 500
