from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_resposta(texto):

    if isinstance(texto, dict):
        texto = texto.get("message", "")

    texto = str(texto)

    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": texto}
        ]
    )

    # ACESSO CORRETO NA NOVA SDK
    return resposta.choices[0].message.content
