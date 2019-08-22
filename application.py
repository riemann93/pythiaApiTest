"""
Exposing of the pythia api
"""

from flask import Flask
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
import azure_connection


app = Flask(__name__)
api = Api(app)


class Landing(Resource):
    def get(self):
        return {'Hello': 'World!'}


class Blob(Resource):
    def get(self, tid, sid, mid, date):

        string = '{}/{}/{}/{}/data'.format(tid, sid, mid, date)
        return_json = azure_connection.get_blob(string)
        return return_json


api.add_resource(Landing, '/')
api.add_resource(Blob, '/blob/<tid>/<sid>/<mid>/<date>')

if __name__ == '__main__':
    app.run(debug=True)
