#import module requirements
import time
import json
import hashlib

class Blockchain:
    def __init__(self):
        self.chain = []                     #stores blockchain
        self.current_transactions = []      #stores transactions
        self.new_block(previous_hash=1, proof=100) #create genesis block
        
    def new_block(self, proof, previous_hash=None):
        # create new blocks and then add them to the existing chain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        #clear transactions and add block to the chain
        self.current_transactions = []
        self.chain.append(block)
        return block
    
    def new_transaction(self, sender, recipient, amount):
        # creates new transactions with sender, recipient, amount 
        # appends transaction to existing transaction list
        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            }
        )
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # used to hash a block
        block_string = json.dumps(block, sort_keys=True).encode()
        # returns a SHA-256 block hash
        return hashlib.sha256(block_string).hexdigest()
    
    @property
    def last_block(self):
        # calls and returns the last block of the chain
        return self.chain[-1]
    
    def register_node(self):
        # register a new node and add it to the network
        pass
    
    def valid_proof(self):
        # ensure that submitted block to chain solves the problem
        pass

    def valid_chain(self):
        # make sure subsequent blocks in chain are valid
        pass
    
    
    
    