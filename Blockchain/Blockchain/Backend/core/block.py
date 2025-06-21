class Block:
    """Block is a storage container that stores transactions"""
    def __init__(self, height, blocksize, blockheader, txcount, txs):
        self.Height = height
        self.Blocksize = blocksize
        self.BlockHeader = blockheader
        self.TxCount = txcount
        self.Txs = txs