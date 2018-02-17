from blockchain.block import Block
import time

BLOCKCHAIN = []
PENDING_TX = []
def create_genesis():
    return Block(0, time.time(), "0", {"nonce": 1, "transactions": None}, 1)

class Blockchain:
    chain = []
    def __init__(self, blockchain):
        self.chain = blockchain

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

            raise Exception("This block does not exist")

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
