"""
Exposing of the pythia api
"""

from flask import Flask
from flask_restful import Resource, Api
from flask_jsonpify import jsonify


app = Flask(__name__)
api = Api(app)


class TestClass1(Resource):
    def get(self):
        return {'Hello': 'World! test 1'}


class TestClass2(Resource):
    def get(self):
        return {'Hello': 'World! test 2'}


api.add_resource(TestClass1, '/test1')
api.add_resource(TestClass2, '/test2')

if __name__ == '__main__':
    app.run(debug=True)
