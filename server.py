from flask import Flask, jsonify
from estuary_client import Estuary

app = Flask(__name__)
estuary = Estuary()


def construct_url(cid):
    return "https://" + cid + ".ipfs.dweb.link"


@app.route("/data/list")
def list_data():
    data = estuary.list_data()
    response = jsonify([construct_url(datum["cid"]["/"]) for datum in data])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
