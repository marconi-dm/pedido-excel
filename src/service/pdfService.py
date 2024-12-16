from src.controller.dataController import PdfExtractor
from src.controller.xlsxController import SpreadsheetBuilder



class PdfService:
    @staticmethod
    def process_pdf(file):
        """
        Processa o PDF, extrai dados e retorna o Excel como buffer.

        Args:
            file: Arquivo PDF enviado pelo usuário.

        Returns:
            BytesIO: Buffer contendo o arquivo Excel gerado.
        """
        try:
            # Inicializa o extrator e realiza o processamento
            # Processar o PDF
            pdf_extractor = PdfExtractor(file)
            pdf_extractor.extract_text()  # Extrai o texto do PDF
            pdf_extractor.process_data()  # Processa os dados extraídos
            dataframe = pdf_extractor.extract_structured_data()  # Organiza os dados em um DataFrame

            # Salva os dados como um Excel em memória
            excel_buffer = SpreadsheetBuilder.save_to_excel(dataframe)
            return True, excel_buffer
        except Exception as e:
            # Retorna o erro
            return False, str(e)