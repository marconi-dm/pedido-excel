from flask import Flask, request, send_file, render_template
from src.service.pdfService import PdfService
import logging

app = Flask(__name__, static_folder='src/static', template_folder='src/templates')

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Verifica se o documento foi enviado
        if 'file' not in request.files or not request.files['file'].filename:
            # Retorna a página com uma mensagem de erro
            return render_template("index.html", error="Nenhum arquivo enviado."), 400
        # Atribui o documento na variável file
        file = request.files['file']
        # Verifica se o documento é um pdf
        if not file.filename.lower().endswith('.pdf'):
            # Retorna a página com uma mensagem de erro
            return render_template("index.html", error="Por favor, envie um arquivo PDF válido."), 400
        # Envia o documento para tratamento e coleta a resposta do processo
        success, result = PdfService.process_pdf(file)
        # Caso retorne algum erro é retornado o erro
        if not success:
            logging.error(f"Erro ao processar o arquivo: {result}")
            return render_template("index.html", error=f"Erro ao processar o arquivo: {result}"), 500
        
         # Coleta o nome para criar a planilha
        filename = file.filename[:-4]
          
        # Retorna o arquivo gerado
        return send_file(
                result,
                as_attachment=True,
                download_name=f"{filename}.xlsx",
                mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            ),200 # Retorna sucesso do processamento

    # Para requisições GET, retorna a página inicial
    return render_template('index.html')
