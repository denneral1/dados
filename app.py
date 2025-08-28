from flask import Flask, jsonify
import csv

app = Flask(__name__)

def ler_csv():
    dados = []
    with open('banco_exercicios.csv', mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dados.append(linha)
    return dados

@app.route('/exercicios', methods=['GET'])
def get_exercicios():
    dados = ler_csv()
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)