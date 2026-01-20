# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── main.py              # Aplicação principal 
├── app.py               # dados

```
## Pré-requisitos

- Python 3.10+
- Conta no Google AI Studio
- Chave de API do Gemini

## Como Rodar

```bash
# Instalar Streamlit
pip install streamlit

# Instalar SDK do Google Gemini
pip install google-generativeai

# (Opcional) Suporte a variáveis de ambiente via .env
pip install python-dotenv


# Rodar a aplicação
streamlit run main.py
```
