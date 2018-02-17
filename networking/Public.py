from flask import Flask
import json
from flask import jsonify

public = Flask(__name__)

public_nodes = {}

#Matthew look here
blockchain = ['nothing']

with open("nodes.json", "r") as json_file:
    data = json.load(json_file)
    public_nodes = data

@public.route("/nodes")
def return_nodes():
    return json.dumps(public_nodes)

#Matthew Look Here
@public.route("/blockchain", methods=['POST'])
def return_blockchain():
    return jsonify(chain=blockchain)

#Matthew Look Here
@public.route("/blockchain/update", methods=['POSTS'])
def update_blockchain():
    data = request.get_json()
