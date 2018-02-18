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
        private_key = os.urandom(32)
        signing_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
        verifying_key = signing_key.get_verifying_key()
        public_key = bytes.fromhex("04") + verifying_key.to_string()

        sha256_1 = hashlib.sha256(public_key)

        ripemd160 = hashlib.new("ripemd160")
        ripemd160.update(sha256_1.digest())

        hashed_public_key = bytes.fromhex("00") + ripemd160.digest()
        checksum_full = hashlib.sha256(hashlib.sha256(hashed_public_key).digest()).digest()
        checksum = checksum_full[:4]
        bin_addr = hashed_public_key + checksum

        wallet_address = base58.b58encode(bin_addr)

        self.priv_key = private_key.hex()
        self.pub_key = public_key.hex()
        self.wal_addr = wallet_address
    def get_private_key(self):
        return self.priv_key
    def get_public_key(self):
        return self.pub_key
    def get_wallet_address(self):
        return self.wal_addr

#gen = WalletGenerator()
#print ("\nprivate key: " + gen.get_private_key() + "\n\npublic key: " + gen.get_public_key() + "\n\nwallet address: " + gen.get_wallet_address())
