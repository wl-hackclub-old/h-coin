from walletgen import WalletGenerator
LOCAL_TRANSACTION_AMOUNT_LIST = []
class Wallet:
    balance = 0
    ok_transaction = False
    def verify_balance(self, amount):
        for i in LOCAL_TRANSACTION_AMOUNT_LIST:
            self.balance = self.balance + i
            if self.balance < self.amount:
                raise Exception("Insufficient funds")
            else:
                self.ok_transaction = True
    def send(self, amount, address):
        if self.ok_transaction == True:
            self.balance = balance-amount
            LOCAL_TRANSACTION_AMOUNT_LIST.append(-1*amount)
        else:
            raise Exception("Transaction could not complete")
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

l = LogWallet()
print(l.get_public())
print(l.get_address())
print(l.get_private())
