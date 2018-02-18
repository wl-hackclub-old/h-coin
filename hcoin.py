import argparse
import requests
import ecdsa
import hashlib
from flask import Flask
from flask import jsonify
from networking.Networking import Propagator
import json
"""
from miner import proofofwork
from blockchain.block import Block
from blockchain.blockchain import Blockchain
from node import node
from wallet.wallet import Wallet
from wallet.walletgen import WalletGen
"""

app = Flask(__name__)


p = Propagator()

@app.route("/my_peers")
def return_my_peers():
    # print(json.dump(p.my_peers()))
    return jsonify(p.my_peers())
@app.route("/get_peers")
def return_get_posts():
    p.get_peers()
    return "hello"

#Thanks to Peter Wensel! :)
class GetBlock(argparse.Action):
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        if nargs != 1:
            raise ValueError("Only one argument is allowed")
        super(GetBlock, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        p = Public("http://localhost:5000")
        chain = p.return_blockchain()
        blockchain = Blockchain(chain)
        print (blockchain.get_block(values))


parser = argparse.ArgumentParser(description='Gets Blocks')
parser.add_argument('--get_block', action=GetBlock,)
args = parser.parse_args()

class SendCoin(argparse.Action):
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        if nargs != 1:
            raise ValueError("Only one argument is allowed")
        super(SendCoin, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string):
        setattr(namespace, self.dest, values)
try:
    app.run(host='0.0.0.0')
except Exception as e:
    print(e)
