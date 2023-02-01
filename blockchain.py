class Blockchain:
    def __init__(self):
        self.chain = []                     #stores blockchain
        self.current_transactions = []      #stores transactions
        
    def new_block(self):
        # create new blocks and then add them to the existing chain
        pass
    
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
        pass
    
    @property
    def last_block(self):
        # calls and returns the last block of the chain
        pass
    
    def register_node(self):
        # register a new node and add it to the network
        pass
    
    def valid_proof(self):
        # ensure that submitted block to chain solves the problem
        pass

    def valid_chain(self):
        # make sure subsequent blocks in chain are valid
        pass
    
    
    
    