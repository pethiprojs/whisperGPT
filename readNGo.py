import os
from dotenv import load_dotenv
import openai
import json
from executa import executa


load_dotenv()
openai.api_key = os.getenv("OPENAI_CHATGPT_API_KEY")
standard_text = "Meu código já possui o código de 3 API's em Python.\n\n aud_in(), ao ser chamada grava 30 segundos de áudio do usuário.\n\nwhisper_input(aud),  recebe o áudio gravado e transcreve o áudio para texto.\n\nchat_input(text), recebe o texto transcrito e envia para uma IA processar o texto e retorna um código em python.\n\nmy_bedroom(code), recebe e executa o código caso o comando de texto tenha sido para o quarto.\n\nmy_kit(code), recebe e executa o código caso o comando de texto tenha sido para a cozinha."



def gpt_input(text_in):
    prompt_text = "utilizando as APIs já PRONTAS, descritas anteriormente, converta o seguinte texto em código python utilizando as funções anteriores:\n\n'" + text_in
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {
                "role":"system",
                "content": standard_text
            },
            {
                "role":"user",
                "content": prompt_text
            }
        ],
        functions=[
            {
                "name": "executa",
                "description": "execute a given code",
                "parameters": {
                    "type": "string",
                    "properties": {
                        "code": {
                            "type": "string",
                            "description": "A code to run and execute the user-demanded-action",
                        },
                        # "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["code"],
                },
            }
        ],
        function_call="auto",
        temperature = 0,
        max_tokens=300
    )
    message = response.choices[0].message
    transcription = response.choices[0].message.content.strip()
    # the json file to save the output data   
    save_file = open("savedata.json", "w")  
    json.dump(response, save_file, indent = 6)
    save_file.close()

    # if message.get("function_call"):
    #     function_name = message["function_call"]["name"]
        

    return transcription


gpt_code = gpt_input("ligue as luzes da sala")
# print(gpt_code)
# gpt_code = "print('executando com sucesso')"
# executa(gpt_code)

# https://community.openai.com/t/providing-context-to-the-chat-api-before-a-conversation/195853/3