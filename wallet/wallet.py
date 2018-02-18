from wallet.walletgen import WalletGenerator
from networking.Networking import Propagator
import json
import os

p = Propagator()

class LogWallet:
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

        self.nodes = {}

        self.data = {}

        with open(self.dir_path + "/walletinfo.json", "r") as json_file:
            self.data = json.load(json_file)
    def read_private_key(self):
        return self.data["private"]
    def read_public_key(self):
        return self.data["public"]
    def update_balance(self, new_bal):
        self.data["balance"] = new_bal
        with open(self.dir_path + "/walletinfo.json", "w") as out:
            json.dump(self.data, out)
    def read_balance(self):
        return int(self.data["balance"])
    def sync_balance(self):
        self.data['balance'] = p.get_bal()

l = LogWallet()

class Wallet:
    def __init__(self):
        print('test')
        self.balance = l.read_balance()

    # def verify_balance(self, amount):
    #     for i in LOCAL_TRANSACTION_AMOUNT_LIST:
    #         self.balance = self.balance + i
    #     if self.balance >= int(amount):
    #         self.ok_transaction = True
    #     else:
    #         raise Exception("Insufficient funds")
    def send(self, amount, address):
        # self.verify_balance(amount)
        self.balance = int(l.read_balance()) - int(amount)
        l.update_balance(self.balance)
        p.propagate_unverified_transaction({'amount' : amount, 'address' : address})
        print ("Sent " + amount + " h-coin to " + address)
        print ("New balance: " + str(self.balance))
