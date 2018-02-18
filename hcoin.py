import argparse
import requests
import ecdsa
import json
import hashlib
from flask import Flask
from flask import jsonify
from networking.Networking import Propagator
from wallet.wallet import Wallet
from wallet.wallet import LogWallet
from wallet.walletgen import WalletGenerator
from blockchain.block import Block
from blockchain.blockchain import Blockchain

"""
from miner import proofofwork
"""

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
            raise ValueError("Type it exactly like this: amount,address")
        super(SendCoin, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string):
        value_arr = values.split(",")
        amount = value_arr[0]
        address = value_arr[1]

        my_wallet = Wallet()
        my_wallet.send(amount, address)
class GetBalance(argparse.Action):
    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        if nargs != 1:
            raise ValueError("Requires an address argument")
        super(GetBalance, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string):
        w = Wallet()
        print (w.get_balance())

# class NetDebug(argparse.Action):
#         def __init__(self, option_strings, dest, nargs=0, **kwargs):
#             if nargs != 0:
#                 raise ValueError("Only zero argument is allowed")
#             super(NetDebug, self).__init__(option_strings, dest, **kwargs)
#         def __call__(self):
#             app.run(host=BIND_ADDRESS, port=int(BIND_PORT))


parser = argparse.ArgumentParser(description='H-Coin Control')
parser.add_argument('--get_block', action=GetBlock)
parser.add_argument('--bind-port', action=BindPort)
parser.add_argument('--bind-address', action=BindAddress)
# parser.add_argument('--net-debug', action=app.run(host=BIND_ADDRESS, port=int(BIND_PORT)))
parser.add_argument('--send', action=SendCoin)
parser.add_argument('--get_balance', action=GetBalance)
args = parser.parse_args()

# if __name__ == '__main__':
