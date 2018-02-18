from blockchain.block import Block
import time

class Blockchain:
    chain = []
    def __init__(self, blockchain):
        self.chain = blockchain

    def create_genesis(self):
        return Block(0, time.time(), "0", {"nonce": 1, "transactions": None}, 1)

    def add_block(self, block):
        self.chain.append(block)

    def get_block(self, search):
        if isinstance(search, int):
            if self.chain[search] == None:
                raise Exception("This block does not exist")
            else:
                return self.chain[search].readable()
        elif isinstance(search, str):
            for block in self.chain:
                if block.get_hash() == search:
                    return block.readable()

    def get_transactions(self, block):
         return block.get_data("transactions")

    def get_latest_block(self):
        return self.chain[-1].readable()
    def get_blockchain(self):
        return BLOCKCHAIN
"""
bc = Blockchain(BLOCKCHAIN)
genesis = create_genesis()
BLOCKCHAIN.append(genesis)
print (bc.get_latest_block())
"""
