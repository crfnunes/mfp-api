from flask import Flask, jsonify
import myfitnesspal
import os
import logging

# Configuração do logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log', filemode='a')

app = Flask(__name__)

MFP_USER = os.getenv("MFP_USER")
MFP_PASS = os.getenv("MFP_PASS")

client = myfitnesspal.Client(MFP_USER, MFP_PASS)

@app.route('/nutrientes/<data>', methods=['GET'])
def obter_nutrientes(data):
    try:
        logging.info(f'Iniciando requisição para obter dados nutricionais do dia {data}')
        
        # Tentando obter os dados nutricionais para a data especificada
        day = client.get_date(data)
        
        # Log de sucesso
        logging.info(f'Dados nutricionais obtidos para {data}: {day.totals}')
        
        return jsonify(day.totals)
    
    except Exception as e:
        # Log de erro caso ocorra uma exceção
        logging.error(f'Erro ao obter dados nutricionais para {data}: {str(e)}')
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    # Log de inicialização do servidor
    logging.info('Iniciando servidor Flask...')
    
    app.run(host="0.0.0.0", port=5000)
