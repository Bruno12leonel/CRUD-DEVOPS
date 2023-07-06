import requests
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

st.set_page_config(page_title='CRUD')

url = "http://flask_app:4000/users"




st.sidebar.success("Cadastrar")


username = st.text_input("Usuário")
email = st.text_input("Email")

cadastrar = st.button("Cadastrar")
if cadastrar:
    user = {'username' : username, 'email' : email}
    response = requests.post(url, json = user)


show_users = st.checkbox("Usuário cadastrados")

if show_users:
    query_list = requests.get(url)
    data = query_list.json()
    data = pd.DataFrame(data)
    st.write(data)
