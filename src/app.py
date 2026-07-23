import json
import pandas as pd
import requests
import streamlit as st

# configuração #
OLLAMA_URL = "http://localhost:11434/api/generate"
modelo = "gpt-oss"

# carregar dados #
perfil = json.load(open("./data/perfil_Investidor.json"))
transacoes = pd.read_csv("./data/transacoes.csv")
historico = pd.read_csv("./data/historico_atendimento.csv")
produtos = json.load(open("./data/produtos_financeiros.json"))

# montar contexto #

contexto = f"""
CLIENTE:{perfil['nome']},{perfil['idade']} anos, perfil{perfil['perfil_investidor']}
OBJETIVO:{perfil['objetivo_principal']}
PATRIMONIO: R${perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTO ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONIVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}

"""
# system prompt #
SYSTEM_PROMPT = """Você é o Edu, um educador financeiro amigavel e didatico.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando dados do cliente como exemplo praticos.

REGRAS:
1. NUNCA recomende investimentos especificos, apenas explique como funciona;
2. use od dados fornecidos para dar exemplos personalizados;
3. Linguagem siomples, como se explicasse para um amigo;
4. Se não souber algo, admita: "nao tenho essa informação, mas posso explicar...";
5. Sempre pergunte se o cliente entendeu.
6. Resposta de forma sucinta e direta, com no maximo 3 paragrafos.
7. JAMAIS responda a perguntas dora do tema ensino de finanças pessoais.
"""

# CHAMAR OLLAMA #

def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": modelo,"prompt":prompt,"stream":False})
    return r.json()['response']


# INTERFACE #
st.title(" Edu, seu educador financeiro")

if pergunta :=st.chat_input("Sua duvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))


# executar codigo # 

 #streamlit run src/app.py#
