import requests
import json
# class Miner:
#     def __init__():
#
#     def broadcast_block_found(block):
#         print('test')
#
class Public:
    def __init__(self, public_ledger_addr):
        self.public_ledger_addr = public_ledger_addr
    def return_blockchain(self):
        data = requests.post(self.public_ledger_addr + "/blockchain")
        return data.json()
    #Matthew Look Here
    def update_blockchain(self, thing):
        requests.post(self.public_ledger_addr + "/blockchain/update", data=thing)
