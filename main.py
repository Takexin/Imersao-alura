#Importando as APIs e bibliotecas
import google.generativeai as genai
from pvrecorder import PvRecorder
import wave
import struct








parar_de_gravar = False

#Configurando a API key
genai.configure(api_key="SUA-API-KEY")

#Criando instancia do pvrecorder
recorder = PvRecorder(device_index=-1, frame_length=512)
audio = []

#Captando audio do microfone
def gravar_audio():
    try:
        recorder.start()
        print('fale')
        while True:
            frame = recorder.read()
            audio.extend(frame)
    except KeyboardInterrupt:
        recorder.stop()
        with wave.open('audio.wav', 'w') as f:
            f.setparams((1, 2, 16000, 512, 'NONE', 'NONE'))
            f.writeframes(struct.pack('h' * len(audio), *audio))
    finally:
        recorder.delete()
def parar_audio():
    global parar_de_gravar
    if parar_de_gravar==False:
        parar_de_gravar=True
    else:
        parar_de_gravar=False
    print(parar_de_gravar)
    return parar_de_gravar

def teste_gravar():
    global parar_de_gravar
    try:
        recorder.start()
        print('fale')
        while True:
            frame = recorder.read()
            audio.extend(frame)
            if parar_de_gravar:
                raise Exception
    except:
        recorder.stop()
        print("parou")
        with wave.open('audio.wav', 'w') as f:
            f.setparams((1, 2, 16000, 512, 'NONE', 'NONE'))
            f.writeframes(struct.pack('h' * len(audio), *audio))
            parar_de_gravar = False
    finally:
        pass

def conversa():
    global recorder
    #Configurando o chatbot
    generation_config = {
        "candidate_count": 1,
        "temperature": 0.5,
    }
    safety_settings = {
        "HARASSMENT": "BLOCK_NONE",
        "HATE": "BLOCK_NONE",
        "SEXUAL": "BLOCK_NONE",
        "DANGEROUS": "BLOCK_NONE"
    }
    #Escolhendo o modelo
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                safety_settings=safety_settings,
                                system_instruction="Você fala como um homem heterotop super exagerado, utilizando constantemente gírias e termos de academia.")
    chat = model.start_chat(history=[])   
    response = chat.send_message(genai.upload_file('audio.wav'))
    recorder = PvRecorder(device_index=-1, frame_length=512)
    return response.text()