from Blockchain.Backend.util.util import hash256
class BlockHeader:
    def __init__(self, version, prevblockhash, merklroot, timestamp, bits):
        self.version = version
        self.prevblockhash = prevblockhash
        self.merklroot = merklroot
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = 0
        self.blockhash = ''

    def mine(self):
        while(self.blockhash[0 : 4]) != '0000':
            self.blockhash = hash256((str(self.version) + self.prevblockhash + self.merklroot + str(self.timestamp)
                                     + self.bits + str(self.nonce)).encode()).hex()
            self.nonce += 1
            print(f"Mining started {self.nonce}", end = '\r')