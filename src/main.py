import streamlit as st
import os
from google import genai
from app import load_data, system_prompt


# ===============================
# CONFIG STREAMLIT
# ===============================
st.set_page_config(
    page_title="Agente Financeiro IA",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Agente Financeiro Inteligente")
st.write("Converse com seu agente financeiro baseado nos seus dados reais.")

# ===============================
# API KEY
# ===============================
# Defina a variável de ambiente GEMINI_API_KEY no Windows:
# setx GEMINI_API_KEY "SUA_CHAVE_AQUI"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("⚠️ Defina a variável de ambiente GEMINI_API_KEY antes de executar o app.")
    st.stop()

client = genai.Client(api_key=GEMINI_API_KEY)

# ===============================
# CARREGAMENTO DE DADOS
# ===============================
@st.cache_data
def carregar_contexto():
    return load_data()

contexto = carregar_contexto()
sistema = system_prompt()

# ===============================
# INPUT DO USUÁRIO
# ===============================
pergunta = st.text_area(
    "Digite sua pergunta financeira:",
    placeholder="Ex: Posso investir parte do meu patrimônio em renda variável?"
)

# ===============================
# BOTÃO DE ENVIO
# ===============================
if st.button("📊 Analisar"):
    if not pergunta.strip():
        st.warning("Digite uma pergunta.")
        st.stop()

    # Monta o prompt final
    prompt_final = f"""
{sistema}

### CONTEXTO DO CLIENTE
{contexto}

### PERGUNTA DO USUÁRIO
{pergunta}

Responda de forma clara, objetiva e profissional.
"""

    with st.spinner("Analisando seu perfil financeiro..."):
        # Chama o modelo Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt_final
        )

    resposta_texto = response.text

    # Mostra a resposta em texto
    st.subheader("🤖 Resposta do Agente Financeiro")
    st.write(resposta_texto)

    


#C:/Users/Julio/AppData/Local/Programs/Python/Python312/python.exe -m streamlit run src/main.py
