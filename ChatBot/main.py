import os
import openai

openai.api_key = ""


def chatbot(promot):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "Me", "content": prompt}]
    )

    return response.choices[0].message.content()
