from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


def read(keys):

    data_list = []
    for key in keys:
        try:
            with io.BytesIO() as myblob:
                block_blob_service = BlockBlobService(account_name='tcmdatablob',
                                                      account_key='Gvue/WaE18KgR72SotQvABGJC8qkhZ9U6xvLqF7GvMt+o9wl/fsBenPAgD0r5PtysI7GJHNs5a2Ed7Xzvdx7Mw==')
                block_blob_service.set_proxy(host='194.138.0.31', port=9400)
                # As a stream
                block_blob_service.get_blob_to_stream('tcmdatablob', key, myblob)
                myblob.seek(0)
                data_list.append(pd.read_parquet(myblob))
        except AzureHttpError:
            print('no data for {}'.format(key))

    if data_list:
        df = pd.concat(data_list)
        return df
    else:
        return pd.DataFrame()