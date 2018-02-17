import argparse
import flask
import requests
import ecdsa
import hashlib
from miner import proofofwork
from blockchain import blockchain
from blockchain import block
from node import node
from wallet import wallet
from wallet import walletgen

#Thanks to Peter Wensel! :)
class GetBlock(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(GetBlock, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print(values)
        print("Calling action")


getter = argparse.ArgumentParser(description='Gets Blocks')
parser.add_argument('--get_block', action=GetBlock)


class WalletAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(WalletAction, self).__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string)

        setattr(namespace, self.dest, values)
parser = argparse.ArgumentParser(description='Wallet Commands')
parser.add_argument('--send', metavar = '', type=, nargs='', help='')
parser.add_argument('--wallet')
parser.add_argument('--send')
