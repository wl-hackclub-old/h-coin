import time
import hashlib


class Block:

    block_hash = ""

    def __init__(self, index, timestamp, prev_hash, data, nonce):
        self.index = index
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.data = data
        self.nonce = nonce
        self.block_hash = hashlib.sha256((str(index) + str(timestamp) + str(prev_hash) + str(data) + str(nonce)).encode()).hexdigest()

    def get_hash(self):
        return self.block_hash
    def readable(self):
        return "Block " + str(self.index) + " (" + str(self.get_hash()) + "); created " + str(self.timestamp) + "; prev hash: " + str(self.prev_hash) + "; data: " + str(self.data) + "; nonce: " + str(self.nonce)
