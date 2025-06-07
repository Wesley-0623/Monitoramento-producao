import streamlit as st

def autenticar_usuario():
    st.session_state.setdefault("usuario", None)
    if st.session_state["usuario"]:
        return st.session_state["usuario"]

    with st.form("login"):
        st.title("Login")
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        submitted = st.form_submit_button("Entrar")
        if submitted:
            if usuario == "admin" and senha == "admin":
                st.session_state["usuario"] = {"nome": "Administrador", "tipo": "admin"}
                return st.session_state["usuario"]
            elif usuario == "user" and senha == "user":
                st.session_state["usuario"] = {"nome": "Usuário", "tipo": "padrao"}
                return st.session_state["usuario"]
            else:
                st.error("Usuário ou senha incorretos")
    return None