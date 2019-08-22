from azure.storage.blob import BlockBlobService
from azure.common import AzureHttpError
import io
import pandas as pd
import json


def get_blob(string):

    with open('CONFIDENTIAL.json', 'r') as confidential_file:
        data = confidential_file.read()

    confidential_object = json.loads(data)

    block_blob_service = BlockBlobService(account_name=confidential_object['account_name'],
                                          account_key=confidential_object['account_key'])

    # test string: '10002/2/14/201502/data'

    blob = block_blob_service.get_blob_to_bytes('tcmdatablob', string)

    blob_length = blob.properties.content_length
    blob_content = str(blob.content)
    blob_content_sliced = blob_content[0:10]
    blob_content_sliced += "***********************************************..."

    return_json = {
        "blob name": blob.name,
        "blob length": blob_length,
        "blob content": blob_content_sliced
    }

    return return_json
