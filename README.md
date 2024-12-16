# Pedido para Excel

## Visão Geral

O **Pedido para Excel** é uma aplicação desenvolvida para facilitar a conversão de pedidos de vendas gerados pelo sistema **Consinco** em planilhas no formato **XLSX**. Com isso, empresas que utilizam o **TOTVS Varejo Supermercado** podem organizar as informações de pedidos de forma mais clara e acessível, otimizando o fluxo de trabalho.

A aplicação combina o poder de ferramentas como **Flask**, **Pandas**, **pdfplumber** e **openpyxl** para realizar a extração, organização e formatação dos dados, garantindo um processo rápido e eficiente.

## Funcionalidades

- **Envio de Arquivos PDF:** Permite fazer upload de pedidos de vendas no formato PDF.
- **Extração de Dados Automatizada:** Identifica informações essenciais, como:
  - Código do produto
  - Nome do produto
  - Preço unitário, conjunto ou fardo
- **Geração de Planilhas Excel:** Cria planilhas **XLSX** estruturadas e organizadas.
- **Estilização Personalizada:** As planilhas geradas são estilizadas automaticamente para facilitar a leitura.

## Tecnologias Utilizadas

### Backend
- **Flask:** Para criar a aplicação web.

### Manipulação de Dados
- **pdfplumber:** Para extração de informações do PDF.
- **Pandas:** Para organizar e estruturar os dados extraídos.
- **openpyxl:** Para geração e estilização das planilhas.

## Fluxo de Uso

1. **Upload:** Envie o arquivo PDF do pedido de vendas.
2. **Processamento:** Aguarde a extração e organização dos dados.
3. **Download:** Baixe a planilha Excel gerada com as informações estruturadas.

## Hospedagem Online

A aplicação está disponível online. Acesse pelo link:

[**Pedido para Excel**](https://pedido-excel.vercel.app/)

---

Sinta-se à vontade para contribuir ou reportar problemas nesta aplicação.
