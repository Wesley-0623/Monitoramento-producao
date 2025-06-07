
import streamlit as st
import pandas as pd
from datetime import date

# Cores personalizadas
st.set_page_config(page_title="Monitoramento de Produção", layout="wide")

# Sessão de login simples
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if username == "admin" and password == "admin":
            st.session_state.logged_in = True
            st.session_state.is_admin = True
        elif username == "usuario" and password == "1234":
            st.session_state.logged_in = True
            st.session_state.is_admin = False
        else:
            st.error("Credenciais inválidas.")

if not st.session_state.logged_in:
    login()
    st.stop()

# Interface principal
st.title("📊 Monitoramento de Produção - Reciclagem")
st.markdown("Desenvolvido para controle por filial com métricas de produção, aglutinado e OEE.")

# Seletor de Filial
filiais = ["GAL - Lins", "Andradina", "Barretos", "Campo Grande II", "Dourados", "Guapiaçu",
           "Nova Andradina", "Naviraí", "Campo Grande I", "Tirolez", "Massa Leve", "Lange", "Amparo"]
filial = st.selectbox("Selecione a filial", filiais)

# Seleção de data e turno
data = st.date_input("Data", value=date.today(), format="DD/MM/YYYY")
turno = st.radio("Turno", ["Dia", "Manhã", "Noite"], horizontal=True)

# Tabs para separar seções
aba = st.tabs(["📦 Produção", "🧪 Aglutinado", "📈 OEE", "📊 Gráficos"])

# Produção de Fardos
with aba[0]:
    st.subheader("Produção de Fardos")
    col1, col2 = st.columns(2)
    with col1:
        meta_fardos = st.number_input("Meta diária (Qtde de fardos)", min_value=0)
        peso_medio = st.number_input("Média de peso dos fardos (kg)", min_value=0.0)
    with col2:
        real_fardos = st.number_input("Real diário (Qtde de fardos)", min_value=0)

    meta_kg = meta_fardos * peso_medio
    real_kg = real_fardos * peso_medio

    st.metric("Meta (kg)", f"{meta_kg:.2f} kg")
    st.metric("Produzido (kg)", f"{real_kg:.2f} kg")

# Produção de Aglutinado
with aba[1]:
    st.subheader("Produção de Aglutinado")
    col1, col2 = st.columns(2)
    with col1:
        meta_aglutinado = st.number_input("Meta diária (kg)", min_value=0)
    with col2:
        real_aglutinado = st.number_input("Real diário (kg)", min_value=0)

    if real_aglutinado < meta_aglutinado:
        justificativa = st.text_area("Justificativa (obrigatória para meta não cumprida)")
        if justificativa.strip() == "":
            st.warning("⚠️ Justificativa obrigatória para metas não cumpridas.")
            st.stop()

    st.success("✔️ Produção de aglutinado registrada com sucesso.")

# OEE diário
with aba[2]:
    st.subheader("OEE - Eficiência Global do Equipamento")
    oee = st.slider("OEE diário (%)", min_value=0, max_value=100, value=85)
    paradas = st.text_area("Principais paradas do dia")

    st.info(f"OEE registrado: {oee}%")

# Painel Gráfico Simples
with aba[3]:
    st.subheader("Painel Comparativo (Simulação)")
    df = pd.DataFrame({
        "Indicador": ["Meta Fardos (kg)", "Real Fardos (kg)", "Meta Aglutinado (kg)", "Real Aglutinado (kg)"],
        "Valor": [meta_kg, real_kg, meta_aglutinado, real_aglutinado]
    })
    st.bar_chart(df.set_index("Indicador"))
