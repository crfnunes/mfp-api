import logging
from flask import Flask, jsonify
import myfitnesspal
import os

# Configuração de logging
logging.basicConfig(
    level=logging.DEBUG,  # Altere o nível conforme necessário (DEBUG, INFO, ERROR)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]  # Exibir os logs no console
)

app = Flask(__name__)

MFP_USER = os.getenv("MFP_USER")
MFP_PASS = os.getenv("MFP_PASS")

client = myfitnesspal.Client(MFP_USER, MFP_PASS)

@app.route('/nutrientes/<data>', methods=['GET'])
def obter_nutrientes(data):
    try:
        app.logger.info(f"Buscando dados nutricionais para a data: {data}")  # Log para rastrear
        day = client.get_date(data)
        app.logger.info(f"Dados encontrados: {day.totals}")  # Log dos dados encontrados
        return jsonify(day.totals)
    except Exception as e:
        app.logger.error(f"Erro ao obter dados nutricionais: {str(e)}")  # Log de erro
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
