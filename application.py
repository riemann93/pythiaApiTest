"""
Exposing of the pythia api
"""

from flask import Flask
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
import azure_connection


app = Flask(__name__)
api = Api(app)
# credentials_obj = azure_connection.read_confidential()


class TestClass1(Resource):
    def get(self):
        return {'Hello': 'World?'}


class TestClass2(Resource):
    def get(self):
        return azure_connection.read_confidential()['account_name']


api.add_resource(TestClass1, '/test1')
api.add_resource(TestClass2, '/test2')

if __name__ == '__main__':
    app.run(debug=True)
