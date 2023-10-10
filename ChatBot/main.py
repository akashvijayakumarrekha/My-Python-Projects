import os
import openai

openai.api_key = ""


def chatbot(promot):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "Me", "content": prompt}]
    )

    return response.choices[0].message.content()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chatbot(user_input)
        print("Bot: ", response)
