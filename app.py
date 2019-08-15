from flask import Flask
from azure.storage.blob import BlockBlobService
from azure.common import AzureHttpError
import io
import pandas as pd


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"
