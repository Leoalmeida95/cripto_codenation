from flask import Flask
from flask_restful import Api, Resource
import requests
import os
from os.path import dirname, isfile, join
from dotenv import load_dotenv

app = Flask(__name__)
app.config["APPLICATION_ROOT"] = "/cripto"

# a partir do arquivo atual adicione ao path o arquivo .env
_ENV_FILE = join(dirname(__file__), '.env')

# existindo o arquivo faça a leitura do arquivo através da função load_dotenv
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

api = Api(app)
    
@app.route('/', methods=['GET'])
def get():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={}'.format(os.getenv('TOKEN'))
    response = requests.get(url)
    print(response)
    #data=''
    #url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=' + getenv('TOKEN')
    #headers = {'Content-type': 'multipart/form-data; charset=UTF-8'}
    #response = requests.post(url, data=data, headers=headers)
    return "OBTENDO JSON"

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG'))