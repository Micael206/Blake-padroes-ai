
import streamlit as st
from historico import obter_ultima_cor, prever_proxima_cor

st.set_page_config(page_title="Blaze Padrões com IA", layout="centered")

st.image("logo.png", width=200)
st.title("Blaze Padrões com IA")

st.markdown("**Este é um painel inteligente para analisar padrões da Blaze Double.**")

ultima_cor = obter_ultima_cor()
proxima_cor = prever_proxima_cor()

st.subheader("Última cor identificada:")
st.info(ultima_cor)

st.subheader("Previsão para a próxima entrada:")
st.success(proxima_cor)

st.markdown("---")
st.caption("Integração com IA em desenvolvimento...")
