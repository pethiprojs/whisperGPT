import os
from dotenv import load_dotenv
import openai
import json
from executa import executa


load_dotenv()
openai.api_key = os.getenv("OPENAI_CHATGPT_API_KEY")
standard_text = "Meu código já possui o código de 3 API's em Python.\n\n aud_in(), ao ser chamada grava 30 segundos de áudio do usuário.\n\nwhisper_input(aud),  recebe o áudio gravado e transcreve o áudio para texto.\n\nchat_input(text), recebe o texto transcrito e envia para uma IA processar o texto e retorna um código em python.\n\nmy_bedroom(code), recebe e executa o código caso o comando de texto tenha sido para o quarto.\n\nmy_kit(code), recebe e executa o código caso o comando de texto tenha sido para a cozinha.\n\nutilizando as APIs já PRONTAS, descritas anteriormente, converta o seguinte texto em código python utilizando as funções anteriores:\n\n'"

def gpt_input(text_in):
    prompt_text = standard_text + text_in + "'"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt_text,
        max_tokens=300
    )
    transcription = response.choices[0].text.strip()
    # the json file to save the output data   
    save_file = open("savedata.json", "w")  
    json.dump(response, save_file, indent = 6)  
    save_file.close()  

    return transcription


gpt_code = gpt_input("ligue as luzes da sala")
print(gpt_code)
# gpt_code = "print('executando com sucesso')"
executa(gpt_code)

# https://community.openai.com/t/providing-context-to-the-chat-api-before-a-conversation/195853/3