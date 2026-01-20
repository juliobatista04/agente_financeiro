# src/app.py
import json
import pandas as pd

def load_data():
    perfil = json.load(open(
        r'C:\\Users\\Julio\\ESTUDOS\\genIA\\Edu\\data\\perfil_investidor.json',
        encoding='utf-8'
    ))

    transacoes = pd.read_csv(
        r'C:\\Users\\Julio\\ESTUDOS\\genIA\\Edu\\data\\transacoes.csv'
    )

    historico = pd.read_csv(
        r'C:\\Users\\Julio\\ESTUDOS\\genIA\\Edu\\data\\historico_atendimento.csv'
    )

    produtos = json.load(open(
        r'C:\\Users\\Julio\\ESTUDOS\\genIA\\Edu\\data\\produtos_financeiros.json',
        encoding='utf-8'
    ))

    contexto = f"""
CLIENTE: {perfil['nome']} ({perfil['idade']} anos)
PERFIL: {perfil['perfil_investidor']}

OBJETIVO:
{perfil['objetivo_principal']}

PATRIMÔNIO:
Total: R$ {perfil['patrimonio_total']}
Reserva: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""
    return contexto


def system_prompt():
    return """
Você é um agente financeiro inteligente.
Seu papel é orientar clientes com base EXCLUSIVA nos dados fornecidos.

REGRAS:
1. Use apenas as informações do contexto
2. Nunca invente dados financeiros
3. Se não houver informação suficiente, diga claramente
4. Linguagem clara, profissional e acessível
5. Responda sempre em português
"""
