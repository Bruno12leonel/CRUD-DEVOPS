import requests
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

st.set_page_config(page_title='Usuários')

url = "http://flask_app:4000/users"


query_list = requests.get(url)
data = query_list.json()
data = pd.DataFrame(data)
st.write(data)

id = st.text_input("Digite o id para excluir")

deletar = st.button("Deletar")

if deletar :
    url = f'http://flask_app:4000/users/{int(id)}'
    response = requests.delete(url)
