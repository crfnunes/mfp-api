from flask import Flask, jsonify
import myfitnesspal
import os

app = Flask(__name__)

MFP_USER = os.getenv("MFP_USER")
MFP_PASS = os.getenv("MFP_PASS")

client = myfitnesspal.Client(MFP_USER, MFP_PASS)

@app.route('/nutrientes/<data>', methods=['GET'])
def obter_nutrientes(data):
    try:
        day = client.get_date(data)
        return jsonify(day.totals)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
