import openai

def gerar_resposta(texto):

    # Se for objeto {"message": "..."} pega só o texto
    if isinstance(texto, dict):
        texto = texto.get("message", "")

    # Garante que é string
    texto = str(texto)

    # RESPOSTA CRUA DA IA
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": texto}
        ]
    )

    # PEGA SOMENTE O TEXTO DA RESPOSTA
    resposta_texto = resposta["choices"][0]["message"]["content"]

    return str(resposta_texto)
