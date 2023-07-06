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

id = st.text_input("Digite o id para atualizar")

username = st.text_input("Usuário")
email = st.text_input("Email")
    

atualizar = st.button("Atualizar")

if atualizar :
    url = f'http://flask_app:4000/users/{int(id)}'
    user = {'username' : username, 'email' : email}
    response = requests.put(url, json = user)
