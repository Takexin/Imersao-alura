#Importing the API
import google.generativeai as genai

#desafio: O que vc quiser, regras: relacao com conteudo da imersao, usar a api do google,
#pode criar quantos projetos quiser,
#avaliacao por github,
#sabado as 23:59 data de entrega,
#pegar os 30 melhores projetos votados pelo povo no discord
#nao pode conteudo de odio ou algo inapropriado
#notas: utilidade, criatividade, eficacia(quao bem resolve o problema), apresentacao

#putting in the API key
genai.configure(api_key="AIzaSyCG9H9NOaY3yXzyUQSvqVDcr_pIVD9cWFA")

#Listing all possible models
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
"""gemini pro: just text
#pro vision: multimodal
#gemini 1.0 pro: most stable version(currently)
#0.001: more experimental features
#latest: most recent"""

#setting up settings for the model
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
#choosing the model we want
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings,
                              system_instruction="Você fala como um homem heterotop super exagerado, utilizando constantemente gírias e termos de academia.")
chat = model.start_chat(history=[])
prompt = input("Waiting for prompt: ")

while prompt != "finish":
    response = chat.send_message(prompt)
    print("Response: ", "\n", response.text, "\n")
    prompt = input("Waiting for prompt: ")
