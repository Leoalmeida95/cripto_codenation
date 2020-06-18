import os
import json
import requests
import hashlib
from os.path import dirname, isfile, join
from flask import Flask, render_template, request, redirect
from flask_restful import Api, Resource
from dotenv import load_dotenv

# a partir do arquivo atual adicione ao path o arquivo .env
_ENV_FILE = join(dirname(__file__), '.env')
# existindo o arquivo faça a leitura do arquivo através da função load_dotenv
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

app = Flask(__name__)

api = Api(app)
    
@app.route('/', methods=['GET'])
def get():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={}'.format(os.getenv('TOKEN'))
    response = requests.get(url)

    _json ={}
    caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
    decifrado = ''
    if(response.status_code == 200):
        
        #pega os valores do json do codenation
        data = response.json()
        cifrado = data.get('cifrado')
        numero_casas = data.get('numero_casas')

        #percorre os caracteres do texto cifrado
        for char in cifrado:

            if char in caracteres:
                #retorna a posicao do caracter dentro da string 'caracteres'
                posicao = caracteres.find(char)
                posicao = posicao - numero_casas

                #calcula o char correspondente
                if posicao >= len(caracteres):
                    posicao = posicao - len(caracteres)
                elif posicao < 0:
                    posicao = posicao + len(caracteres)
                    decifrado = decifrado + caracteres[posicao]
                else:
                    decifrado = decifrado + caracteres[posicao]

            elif char == '.' or char == ' ' or char == ',':
                decifrado = decifrado + char

        data.update({'decifrado': decifrado})

        resumo_criptografico = hashlib.sha1(decifrado.encode('utf8')).hexdigest()
        data.update({'resumo_criptografico': resumo_criptografico})
        
        _json = json.dumps(data, indent=4)

        with open("output/answer.json", "w") as arquivo:
            arquivo.write(_json)
    else:
        return "Erro ao obter o json do codenation", 500

    return render_template('index.html')

@app.route('/codenation', methods=['POST'])
def submit():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=' + os.getenv('TOKEN')
    headers = {'Content-type': 'multipart/form-data'}
    file = request.con
    print(file)
    # response = requests.post(url, files=file, headers=headers)
    # return response.content
    return "sucesso"

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG'))