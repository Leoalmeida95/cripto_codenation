from flask import Flask
from flask_restful import Api, Resource
import requests
from os import getenv

app = Flask(__name__)
app.config["APPLICATION_ROOT"] = "/cripto"

api = Api(app)

@app.route('/', methods=['GET'])
def get(self):
    data=''
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=' + getenv('TOKEN')
    headers = {'Content-type': 'multipart/form-data; charset=UTF-8'}
    response = requests.post(url, data=data, headers=headers)
    return {'site': 'APP'}

api.add_resource('/codenation', 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + getenv('TOKEN'))

if __name__ == '__main__':
    app.run(debug=getenv('DEBUG'))