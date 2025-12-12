from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_resposta(texto):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": texto}
            ]
        )

        resposta = response.choices[0].message["content"]
        return resposta

    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"
