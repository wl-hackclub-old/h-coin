from walletgen import WalletGenerator
class Wallet:
    balance = 0
    address = ""
    def send(self, amount, address):
        balance = balance-amount
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
    def get_address(this_address, path):
        path = './walletinfo.txt'
        this_address = open("walletinfo.txt", 'r')
        lines = this_address.readlines()
        return lines[0]
        this_address.close()
    def get_public(this_address, path):
        path = './walletinfo.txt'
        this_address = open("walletinfo.txt", 'r')
        lines = this_address.readlines()
        return lines[1]
        this_address.close()
    def get_private(this_address, path):
        path = './walletinfo.txt'
        this_address = open(path, 'r')
        lines = this_address.readlines()
        return lines[2]
        this_address.close()
l = LogWallet()
print(l.get_public)
print(l.get_address)
print(l.get_private)
