import streamlit as st
import datetime

def pagina_producao_fardos(usuario):
    st.header("Registro de Produção - Fardos")

    filiais = [
        "GAL - Lins", "Andradina", "Barretos", "Campo Grande II", "Dourados", "Guapiaçu",
        "Nova Andradina", "Naviraí", "Campo Grande I", "Tirolez", "Massa Leve", "Lange", "Amparo"
    ]

    with st.form("form_fardos"):
        col1, col2 = st.columns(2)
        with col1:
            filial = st.selectbox("Filial", filiais)
            data = st.date_input("Data", value=datetime.date.today(), format="DD/MM/YYYY")
            turno = st.selectbox("Turno", ["Dia", "Manhã", "Noite"])
        with col2:
            meta_fardos = st.number_input("Meta Diária (fardos)", min_value=0)
            real_fardos = st.number_input("Realizado (fardos)", min_value=0)
            peso_medio = st.number_input("Peso médio dos fardos (kg)", min_value=0.0)

        meta_kg = meta_fardos * peso_medio
        real_kg = real_fardos * peso_medio

        st.markdown(f"**Meta (kg):** {meta_kg:.2f} kg")
        st.markdown(f"**Realizado (kg):** {real_kg:.2f} kg")

        justificativa = ""
        if real_kg < meta_kg:
            justificativa = st.text_area("Justificativa (obrigatória se não atingir a meta)", max_chars=300)
            if justificativa.strip() == "":
                st.warning("Justificativa obrigatória quando a meta não for atingida.")

        salvar = st.form_submit_button("Salvar Produção")

        if salvar:
            if real_kg < meta_kg and justificativa.strip() == "":
                st.error("Justificativa é obrigatória. Não foi possível salvar.")
            else:
                st.success("Produção registrada com sucesso!")