"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyCG9H9NOaY3yXzyUQSvqVDcr_pIVD9cWFA")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Send me the alphabet, but which letter has a random word attached to it"]
  },
  {
    "role": "model",
    "parts": ["A - Avocado\nB - Bee\nC - Cup\nD - Dog\nE - Elephant\nF - Fish\nG - Giraffe\nH - Hat\nI - Ice cream\nJ - Jellyfish\nK - Kite\nL - Lion\nM - Monkey\nN - Nest\nO - Octopus\nP - Pig\nQ - Queen\nR - Rabbit\nS - Snake\nT - Tiger\nU - Umbrella\nV - Violin\nW - Whale\nX - Xylophone\nY - Yacht\nZ - Zebra"]
  },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)