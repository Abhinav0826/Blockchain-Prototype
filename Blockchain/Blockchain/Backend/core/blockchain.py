import sys
sys.path.append('/Users/abhinavkonda/Developer/Blockchain/Blockchain')

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.util.util import hash256
from Blockchain.Backend.core.database.database import BlockchainDB
import time
import json

ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
    def __init__(self):
        self.chain = []
        self.genesisblock()

    @staticmethod
    def write_on_disk(block):
        blockchaindb = BlockchainDB()
        blockchaindb.write(block)

    @staticmethod
    def fetch_last_block():
        blockchaindb = BlockchainDB()
        return blockchaindb.lastblock()

    def genesisblock(self):
        blockheight = 0
        prevblockhash = ZERO_HASH
        self.addblock(blockheight, prevblockhash)

    def addblock(self, blockheight, prevblockhash):
        timestamp = int(time.time())
        transaction = f"Codies Alert sent {blockheight} Bitcoins to Abhi"
        merkleroot = hash256(transaction.encode()).hex()
        bits = 'ffff001f'
        blockheader = BlockHeader(VERSION, prevblockhash, merkleroot, timestamp, bits)
        blockheader.mine()
        # self.write_on_disk([Block(blockheight, 1, blockheader.__dict__, 1, transaction).__dict__])
        self.chain.append(Block(blockheight, 1, blockheader.__dict__, 1, transaction).__dict__)
        print(json.dumps(self.chain, indent = 4))

    def main(self):
        while True:
            # lastblock = self.fetch_last_block()
            lastblock = self.chain[::-1]
            blockheight = lastblock[0]['Height'] + 1
            prevblockhash = lastblock[0]['BlockHeader']['blockhash']
            self.addblock(blockheight, prevblockhash)

if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.main()