import json
import requests
import os
from os.path import dirname, isfile, join
from flask import Flask
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
    if(response.status_code == 200):
        data = response.json()
        _json = json.dumps(data, indent=4)
        with open("output/answer.json", "w") as outfile:
            outfile.write(_json)
    else:
        return "Erro ao obter o json do codenation", 500
    #data=''
    #url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=' + getenv('TOKEN')
    #headers = {'Content-type': 'multipart/form-data; charset=UTF-8'}
    #response = requests.post(url, data=data, headers=headers)

    response = app.response_class(
        response=_json,
        status=200,
        mimetype='application/json'
    )

    return response

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG'))