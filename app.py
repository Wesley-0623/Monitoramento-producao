import streamlit as st
from modules.login import autenticar_usuario
from modules.sidebar import mostrar_menu

st.set_page_config(page_title="Sistema de Gestão de Produção", layout="wide")

# Autenticação
usuario = autenticar_usuario()
if usuario:
    mostrar_menu(usuario)