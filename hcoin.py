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

BIND_ADDRESS = '0.0.0.0'
BIND_PORT = '5000'

p = Propagator()

@app.route("/my_peers")
def return_my_peers():
    # print(json.dump(p.my_peers()))
    return jsonify(p.my_peers())
@app.route("/get_peers")
def return_get_posts():
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

class BindAddress(argparse.Action):
        def __init__(self, option_strings, dest, nargs=1, **kwargs):
            if nargs != 1:
                raise ValueError("Only one argument is allowed")
            super(BindAddress, self).__init__(option_strings, dest, **kwargs)
        def __call__(self, parser, namespace, values, option_string=None):
            BIND_ADDRESS = values
class BindPort(argparse.Action):
        def __init__(self, option_strings, dest, nargs=1, **kwargs):
            if nargs != 1:
                raise ValueError("Only one argument is allowed")
            super(BindPort, self).__init__(option_strings, dest, **kwargs)
        def __call__(self, parser, namespace, values, option_string=None):
            print(int(values))
            BIND_PORT = values
            app.run(host=BIND_ADDRESS, port=int(BIND_PORT))
class SendCoin(argparse.Action):
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        if nargs != 1:
            raise ValueError("Only one argument is allowed")
        super(SendCoin, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string):
        send()
# class NetDebug(argparse.Action):
#         def __init__(self, option_strings, dest, nargs=0, **kwargs):
#             if nargs != 0:
#                 raise ValueError("Only zero argument is allowed")
#             super(NetDebug, self).__init__(option_strings, dest, **kwargs)
#         def __call__(self):
#             app.run(host=BIND_ADDRESS, port=int(BIND_PORT))


parser = argparse.ArgumentParser(description='Gets Blocks')
parser.add_argument('--get_block', action=GetBlock)
parser.add_argument('--bind-port', action=BindPort)
parser.add_argument('--bind-address', action=BindAddress)
# parser.add_argument('--net-debug', action=app.run(host=BIND_ADDRESS, port=int(BIND_PORT)))
parser.add_argument('--send', action = SendCoin)
args = parser.parse_args()

# if __name__ == '__main__':
