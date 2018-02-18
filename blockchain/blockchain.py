from blockchain.block import Block
import time

BLOCKCHAIN = []

class Blockchain:
    chain = []
    def __init__(self, blockchain):
        self.chain = blockchain

    def create_genesis(self):
        return Block(0, time.time(), "0", {"nonce": 1, "transactions": None}, 1, 1)

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
        if len(self.chain) == 0:
            genesis = self.create_genesis()
            print ("No block found, so genesis was created")
            return genesis
        else:
            latest = self.chain[-1]
            return latest.readable()

bc = Blockchain({})
genesis = bc.create_genesis()
BLOCKCHAIN.append(genesis)
print (bc.get_latest_block().readable())
