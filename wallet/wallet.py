from wallet.walletgen import WalletGenerator
class Wallet:
    balance = 0
    address = ""
    def send(self, amount, address):
        balance = balance-amount
# you hooligans!
class Log:
    def __init__(self, this_address, proof):
        this_address = open("walletinfo.txt", r+)
        this_address.write("Wallet Key: " + get_wallet_address())
        this_address.write("Public Key: " + get_public_key())
        this_address.write("Private Key: " + get_private_key())
        this_address.close()
    def get_address(this_address):
        this_address = open("walletinfo.txt", r)
        print this_address.readline(1)
    def get_public(this_address):
        this_address = open("walletinfo.txt", r)
        print this_address.readline(2)
    def get_private(this_address):
        this_address = open("walletinfo.txt", r)
        print this_address.readline(3)
