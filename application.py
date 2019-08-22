"""
Exposing of the pythia api
"""

from flask import Flask, request
from flask_restful import Resource, Api
import azure_connection
import jwt


app = Flask(__name__)
api = Api(app)


class Login(Resource):
    def post(self):
        auth = request.authorization

        return_json = {
            'username': auth,
            'password': auth.password
        }
        return return_json


class Blob(Resource):
    def get(self, tid, sid, mid, date):

        string = '{}/{}/{}/{}/data'.format(tid, sid, mid, date)
        return_json = azure_connection.get_blob(string)
        return return_json


api.add_resource(Login, '/login')
api.add_resource(Blob, '/blob/<tid>/<sid>/<mid>/<date>')

if __name__ == '__main__':
    app.run(debug=True)
