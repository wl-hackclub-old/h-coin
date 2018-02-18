import ecdsa
import os
import hashlib
import base58

class WalletGenerator:
    priv_key = ""
    pub_key = ""
    wal_addr = ""
    def __init__(self):
        # Generate a keypair using ECDSA
        private_key = os.urandom(32).hex()
        sign_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
        verif_key = sign_key.get_verifying_key()

        public_key = bytes.fromhex("04") + verif_key.to_string()

        # Generate a wallet address
        ripemd160 = hashlib.new("ripemd160")
        ripemd160.update(hashlib.sha256(public_key.decode('hex')).digest())
        middleman = '\00' + ripemd160.digest()
        checksum = hashlib.sha256(hashlib.sha256(middleman).digest()).digest()[:4]

        wallet_address = base58.b58encode(middleman + checksum)

        self.priv_key = private_key
        self.pub_key = public_key
        self.wal_addr = wallet_address
    def get_private_key(self):
        return self.priv_key
    def get_public_key(self):
        return self.pub_key
    def get_wallet_address(self):
        return self.wal_addr

gen = WalletGenerator()
print ("\nprivate key: " + gen.get_private_key() + "\n\npublic key: " + gen.get_public_key() + "\n\nwallet address: " + gen.get_wallet_address())
