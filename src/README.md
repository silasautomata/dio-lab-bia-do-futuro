# passo a passo de execução

Esta pasta contém o código do seu agente financeiro.

## setup do ollama

#1. instalar ollama(ollama.com)
#2. baixar um modelo leve
ollaa pull gpt-oss

#3. testar se funciona
ollama run gpt-oss "ola!
"
```
##Codigo completo
#todo codigo-fonte esta mo arquivo app.py.

```

## Como Rodar

``
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. garantir que ollama esta rodando
ollama serve

# 3.Rodar a aplicação
streamlit run app.py
```
