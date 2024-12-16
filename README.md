Projeto Pedido para Excel




Visão Geral

O Pedido para Excel é uma aplicação desenvolvida para facilitar a conversão de pedidos de vendas gerados pelo sistema Consinco em planilhas no formato XLSX. Com isso, empresas que utilizam o TOTVS Varejo Supermercado podem organizar as informações de pedidos de forma mais clara e acessível, otimizando o fluxo de trabalho.

A aplicação combina o poder de ferramentas como Flask, Pandas, pdfplumber e openpyxl para realizar a extração, organização e formatação dos dados, garantindo um processo rápido e eficiente.

Funcionalidades

Envio de Arquivos PDF: Permite fazer upload de pedidos de vendas no formato PDF.

Extração de Dados Automatizada: Identifica informações essenciais, como:

Código do produto

Nome do produto

Preço unitário, conjunto ou fardo

Geração de Planilhas Excel: Cria planilhas XLSX estruturadas e organizadas.

Estilização Personalizada: As planilhas geradas são estilizadas automaticamente para facilitar a leitura.

Tecnologias Utilizadas

Backend

Flask: Para criar a aplicação web.

Manipulação de Dados

pdfplumber: Para extração de informações do PDF.

Pandas: Para organizar e estruturar os dados extraídos.

openpyxl: Para geração e estilização das planilhas.

Fluxo de Uso

Faça upload do arquivo PDF do pedido de vendas.

Aguarde a extração e processamento dos dados.

O download da planilha Excel é gerada com as informações organizadas.

Hospedagem Online

A aplicação também está disponível online. Acesse pelo link:
https://pedido-excel.vercel.app/
