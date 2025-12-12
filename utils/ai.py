import openai

def gerar_resposta(texto):

    # RESPOSTA CRUA DA IA
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": texto}
        ]
    )

    # PEGA SOMENTE O TEXTO DA RESPOSTA
    resposta_texto = resposta["choices"][0]["message"]["content"]

    # GARANTE QUE É STRING
    return str(resposta_texto)
