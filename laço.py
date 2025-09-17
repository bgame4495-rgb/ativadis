import streamlit as st

st.title("laço de repetição: while")

login_salvo = "Marta"
senha_salva = "123"

st.session_state.setdefault("desabilitar", False)
st.session_state.setdefault("tentativas", 0)

login = st.text_input("DIGITE SEU LOGIN:", disabled=st.session_state.desabilitar)
senha = st.text_input("dIGITE SUA SENHA: ", type="password",disabled=st.session_state.desabilitar)

if st.button("verificar"):
    if login == login_salvo and senha == senha_salva:
        st.success("bem vindo")
    else:
        st.session_state.tentativas += 1
        if st.session_state.tentativas <=3 :
            st.warning("login ou senha errada, tentativas: {st.session_state.tentativas}")
        else:
            st.session_state.desabilitar = True
            st.error("numero de tentativas invalida")
