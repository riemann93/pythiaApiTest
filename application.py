"""
Exposing of the pythia api
"""

from flask import Flask
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
import azure_connection


app = Flask(__name__)
api = Api(app)

return_json = azure_connection.get_blob()


class TestClass1(Resource):
    def get(self):
        return {'Hello': 'World?'}


class Blob(Resource):
    def get(self):
        return return_json


api.add_resource(TestClass1, '/test1')
api.add_resource(Blob, '/blob')

if __name__ == '__main__':
    app.run(debug=True)
