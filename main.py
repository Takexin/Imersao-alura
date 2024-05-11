#Importando as APIs e bibliotecas
import google.generativeai as genai
from pvrecorder import PvRecorder
import wave
import struct
import tkinter as tk

#Configurando a API key
genai.configure(api_key="AIzaSyCG9H9NOaY3yXzyUQSvqVDcr_pIVD9cWFA")

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
def janela(texto):
    root = tk.Tk()
    root.title("Tkinter Example")
    root.geometry('400x200')

    # criando botao 
    button = tk.Button(root, text="Run Blank Function", command=gravar_audio())
    button.pack()

    root.mainloop()

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
prompt = input("Aperte 'enter' para começar: ")
while prompt != "terminar":
    gravar_audio()
    response = chat.send_message(genai.upload_file('audio.wav'))
    print("Response: ", "\n", response.text, "\n")
    recorder = PvRecorder(device_index=-1, frame_length=512)
    prompt = input("escreva 'terminar' para finalizar, ou aperte 'enter' para continuar: ")

