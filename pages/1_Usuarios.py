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