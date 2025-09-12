import streamlit as st

st.title("Contador de media")

n1 = st.number_input("nota de Português: ",step=1)
n2 = st.number_input("II Unidade: ",step=1)
n3 = st.number_input("III Unidade: ",step=1)
n4 = st.number_input("IV Unidade: ",step=1)


if st.button("iniciar"):
    media = n1 + n2 +n3 +n4 /4
    st.write(f"Media Geral: {media}")
