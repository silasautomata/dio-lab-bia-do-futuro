# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, ou seja, dar continuidade ao atendiemnto de forma mais eficiente.|
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre as duvidas e necessidades de aprendizado do cliente |
| `produtos_financeiros.json` | JSON | conhecer os produts disponiveis para que eles possam ser ensinados ao cliente.|
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar essas informações de forma didatica.|

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

o produto fundo imobibiliario (FII) substitui o fundo multimercado, pois pessoalmente me sinto mais confiante em usar apenas produtos financeiros que eu conheço. Assim, poderei validar as respostas do Edi de forma mais assertiva.
---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

'''python
import pandas as pd
import json

#csvs
historico = pd.read_csv("data/historico_atendimento.csv")
transacoes = pd.read_csv("data/transacoes.csv")

#json
with open("data/perfil_investidor.json","r",encoding="utf-8") as f:
  perfil = json.lead(f)
with open("data/produtos_financeiros.json","r",encoding="utf-8") as f:
  produtos = json.lead(f)
'''

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, podemos simplesmente "injetar" os dados em nosso prompt, garantindo que agente tenha um melhor contexo possivel. lembrando que , em soluções masi robustas, o ideal é que essas informações sejam carregadas dinamicamente para que possamos ganhar flixibilidade.

'''text
DADOS DO CLIENTE E PERFIL:
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSAÇÕES DO CLIENTE:

data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

HISTORICO DO ATENDIEMNDO DO CLIENTE:

data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

PRODUTOS DISPONIVEIS PARA ENSINO:
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo imobiliario (FII)",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "dividende Yeld (DY) costuma ficar entre 6% a 12% ao ano",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil moderado que busca diversificação e renda recorrente mensal"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]
'''
---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O Exemplo de contexto montando abaixo, se baseia nos dados originais da base de conhecimento, mas o sintetiza deixando apenas as informaçoes mais relevantes, otimizando assim o consumo de tokens. Entretento, vale lembrar que mais importante do que economizar tokens, e ter as informações relevantes em seu contexto.
```
DADOS DO CLEINTE:
- Nome: João Silva
- Perfil: Moderado
- objetivos: Construirt reserca de emergencia
-reserva atual: R$ 10.000(meta:R$ 15.000)

RESUMO DA GASTOS:
- moradia: R$ 1.380
-alimentação: R$ 570
-trasnporte: R$ 295
-saude: R$ 188
-lazer: R$55,00
-total de saidas: R$ 2.488,90

PRODUTOS DISPONIVEIS PARA EXPLICAR:
-tesouso selic(risco baixo)
-CDB liqueides diaria(risco baixo)
-LCI/LCA(risco baixo)
-fundo imobiliario - FII(risco medio)
-fundo de açoes (risco alto)
...
```
