from wallet.walletgen import WalletGenerator
LOCAL_TRANSACTION_AMOUNT_LIST = []
class Wallet:
    balance = 5
    ok_transaction = False
    def verify_balance(self, amount):
        for i in LOCAL_TRANSACTION_AMOUNT_LIST:
            self.balance = self.balance + i
        if self.balance >= int(amount):
            self.ok_transaction = True
        else:
            raise Exception("Insufficient funds")
    def send(self, amount, address):
        self.verify_balance(amount)
        if self.ok_transaction == True:
            self.balance = self.balance-int(amount)
            LOCAL_TRANSACTION_AMOUNT_LIST.append(-1*amount)
            print ("Sent " + amount + " h-coin to " + address)
        else:
            print (self.ok_transaction)
            raise Exception("Transaction could not complete")
    def get_balance(self):
        return self.balance
    def local_update(self):
        for e in LOCAL_TRANSACTION_AMOUNT_LIST
# you hooligans!
class LogWallet:
    def __init__(self):
        generator = WalletGenerator()
        path = './walletinfo.txt'
        this_address = open(path, 'w')
        this_address.write("Wallet Key: " + generator.get_wallet_address())
        this_address.write("\nPublic Key: " + generator.get_public_key())
        this_address.write("\nPrivate Key: " + generator.get_private_key())
        this_address.close()
    def get_address(self):
        path = './walletinfo.txt'
        this_address = open("walletinfo.txt", 'r')
        lines = this_address.readlines()
        return lines[0]
        this_address.close()
    def get_public(self):
        path = './walletinfo.txt'
        this_address = open("walletinfo.txt", 'r')
        lines = this_address.readlines()
        return lines[1]
        this_address.close()
    def get_private(self):
        path = './walletinfo.txt'
        this_address = open(path, 'r')
        lines = this_address.readlines()
        return lines[2]
        this_address.close()
"""
l = LogWallet()
print(l.get_public())
print(l.get_address())
print(l.get_private())
"""
