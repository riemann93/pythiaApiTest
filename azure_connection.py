"""
account_name='tcmdatablob',
account_key='Gvue/WaE18KgR72SotQvABGJC8qkhZ9U6xvLqF7GvMt+o9wl/fsBenPAgD0r5PtysI7GJHNs5a2Ed7Xzvdx7Mw==')
"""
from azure.storage.blob import BlockBlobService
from azure.common import AzureHttpError
import io
import pandas as pd
import json


def read_confidential():
    with open('CONFIDENTIAL.json', 'r') as confidential_file:
        data = confidential_file.read()

    confidential_object = json.loads(data)
    return confidential_object

    """
    def read_azure_blob(path):
        try:
            with io.bytesIO() as myblob:
                block_blob_service = BlockBlobService()
    """