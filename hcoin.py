import argparse
import requests
import ecdsa
import hashlib
from flask import Flask
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
parser.add_argument('--get_block', action=GetBlock, nargs='+')


class WalletAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(WalletAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string)

        setattr(namespace, self.dest, values)
parser = argparse.ArgumentParser(description='Wallet Commands')
parser.add_argument('--send', action=WalletAction, nargs='+')
parser.add_argument('--wallet', action=Wall)
parser.add_argument('--send')
