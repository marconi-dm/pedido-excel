import re
import pdfplumber
import pandas as pd


class PdfExtractor:
    def __init__(self, pdf_file):
        """
        Inicializa a classe com o arquivo PDF que será processado.
        """
        self.pdf_file = pdf_file
        self.formatted_data = []  # Lista para armazenar as linhas relevantes do PDF
        self.processed_data = []  # Lista para armazenar os dados estruturados

    def extract_text(self):
        """
        Extrai o texto da primeira página do PDF e filtra apenas as informações úteis.
        """
        with pdfplumber.open(self.pdf_file) as pdf:
            text = ''  # String para acumular o texto das páginas
            for page in pdf.pages:
                text += page.extract_text_simple(x_tolerance=3, y_tolerance=3) + '\n'  # Extrai o texto com tolerâncias ajustadas


        # Divide o texto em linhas e define as palavras-chave que marcam a seção desejada
        lines = text.split('\n')
        # Verifica se o pedido de venda é válido para conversão
        if not any("Pedido de Venda" in line for line in lines):
                raise Exception("Documento não é um pedido de vendas válido")
            
        is_target_section = False
        keywords = ["I.P.I", "Vlr. ICMS", "Peso Bruto Total", "TOTAL ICMS ST", "Observações:"]

        for line in lines:
            # Ignorar linhas vazias
            if not line.strip():  # Verifica se a linha é vazia ou contém apenas espaços
                continue
            # Quando encontrar uma palavra-chave, começa a capturar as linhas relevantes
            if any(keyword in line for keyword in keywords):
                is_target_section = True
                continue
            if is_target_section:
                self.formatted_data.append(line)  # Adiciona as linhas relevantes à lista

    def process_data(self):
        """
        Processa os dados extraídos para separar informações como código, nome e preço.
        """
        for idx, line in enumerate(self.formatted_data):
            if 'A VISTA' in line:  # Verifica se a linha contém "A VISTA"
                parts = line.split("A VISTA")  # Divide a linha em duas partes com base em "A VISTA"
                parts[0] = parts[0][:-3]  # Remove os últimos 3 caracteres da primeira parte (ajuste necessário)
                self.processed_data.append(parts)  # Adiciona as partes processadas na lista final
            else:
                if self.processed_data:  # Se for uma linha complementar, concatena a sobrea ao item anterior
                    self.processed_data[-1][0] += f" {line.strip()}"

    def extract_structured_data(self):
        """
        Estrutura os dados processados em um formato organizado, pronto para criar um DataFrame.
        """
        product_codes = []  # Lista para os códigos dos produtos
        product_names = []  # Lista para os nomes dos produtos
        prices = []  # Lista para os preços

        regex_pattern = r"^(\d+)(.*)"  # Expressão regular para separar código e nome

        for line in self.processed_data:
            match = re.match(regex_pattern, line[0])  # Tenta separar código e nome na primeira parte
            if match:
                product_codes.append(match.group(1))  # Adiciona o código à lista
                product_names.append(match.group(2).strip())  # Adiciona o nome à lista

            # Captura o preço da segunda parte da linha
            prices.append(line[1].split()[0])

        # Retorna os dados organizados em um DataFrame
        return pd.DataFrame({
            "Código": product_codes,
            "Nome": product_names,
            "Preço": [f"R$ {price}" for price in prices],
        })


