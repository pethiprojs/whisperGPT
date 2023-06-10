import os
import telebot
from pydub import AudioSegment

bot = telebot.TeleBot('')
AudioSegment.ffmpeg = "./"

# started = 0
# title = ""
# audio_no = 0
# flag = False
# converting_audio = False
# audio_list = []
#########################################################################################
# audio_path =  'download/'
# out_path = 'out/'
# template_path = 'templates/audio/'
# path_text =''
#########################################################################################
# os.chdir('./src/')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Podcast já começou.\nEnvie seus áudios.")


@bot.message_handler(commands=['stop'])
def send_stop(message):
    bot.reply_to(message, "Conexão finalizada")


@bot.message_handler(commands=['eventos'])
    # chamar a API que pega as últimas chamadas


# def text_converter(path_audio):
#     try:
#         new_audio = AudioSegment.from_file(path_audio + '.ogg',"wav")
#     except:
#         converted = AudioSegment.from_ogg(path_audio + '.ogg' )
#         converted.export(path_audio + ".wav", format="wav")
#         # os.remove(audio_path + title + '/' + audio)
#         new_audio = AudioSegment.from_wav(path_audio + '.wav')
    
#     final_text=""
#     r = sr.Recognizer()
#     with sr.AudioFile(path_audio + '.wav') as source:
#         audio_text = r.record(source)
#         final_text += r.recognize_google(audio_text, language='pt-br')
#     global path_text
#     global title
#     with open(path_text + '/' + title + str(audio_no) + '.txt' , 'w') as text:
#         for i in final_text:
#             text.write(i)

### para o áudio : https://github.com/jiaaro/pydub



@bot.message_handler(content_types=['voice'])
def audio_messages(message):
    file_info = bot.get_file(message.voice.file_id)
    download_file = bot.download_file(file_info.file_path)
    with open( "file","wb" ) as new_audio:
        new_audio.write(download_file)
    # CHAMAR AQUI A API DO WHISPER
    bot.reply_to(message, "INSERIR AQUI A RESPOSTA DA CONVERSÃO DO ÁUDIO")
    # CHAMAR AQUI A API DO CHATGPT

bot.infinity_polling()