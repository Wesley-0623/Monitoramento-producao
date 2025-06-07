import streamlit as st

def mostrar_menu(usuario):
    st.sidebar.title("Sistema de Gestão de Produção")
    st.sidebar.markdown(f"**{usuario['nome']} ({'Administrador' if usuario['tipo'] == 'admin' else 'Usuário'})**")
    menu = st.sidebar.radio("Navegação", [
        "Dashboard",
        "Produção (Fardos)",
        "Produção (Aglutinado)",
        "Máquinas",
        "Relatórios",
        "Usuários"
    ])
    st.sidebar.button("Sair", on_click=lambda: st.session_state.clear())
    st.title(menu)
    st.success(f"Você está na página: {menu}")