from azure.storage.blob import BlockBlobService
from azure.common import AzureHttpError
import io
import pandas as pd
import json


def get_blob():

    with open('CONFIDENTIAL.json', 'r') as confidential_file:
        data = confidential_file.read()

    confidential_object = json.loads(data)

    block_blob_service = BlockBlobService(account_name=confidential_object['account_name'],
                                          account_key=confidential_object['account_key'])

    blob = block_blob_service.get_blob_to_bytes('tcmdatablob', '10002/2/14/201502/data')

    return blob.metadata
