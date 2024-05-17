import openai

class Resumentexto:
    model_openai = "gpt-3.5-turbo"

    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def resumen(self, texto, idioma="es"):
        prompt = f"Eres un asistente que puede leer un texto y resumirlo en {idioma}. El resumen tendrá 10 oraciones o menos."
        response = openai.ChatCompletion.create(
            model=self.model_openai,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "El texto que quiero es el siguiente: \n" + texto},
            ],
        )
        respuesta = response.choices[0].message['content']
        return respuesta
