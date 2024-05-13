import main
import streamlit as st
number_test = 0
import sys
        
st.title("Gymbro conversation")
message = st.chat_message("Assintant", avatar="ai")
message.write("This is a test")
st.button(label="Botao", on_click=main.teste_gravar)
st.button(label="Parar de gravar ", on_click=main.parar_audio)
