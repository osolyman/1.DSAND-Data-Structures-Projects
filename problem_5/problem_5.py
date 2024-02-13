import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        # encoding the information of the block
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.head = None

    def append_block(self, data):
        timestamp = datetime.now()
        # if the chain has no blocks yet
        if self.head is None:
            # now we add a block and pointing to it by the head
            self.head = Block(timestamp, data, None)

        # otherwise I append the block at the end of the chain
        else:
            new_block = self.head # we create a new pointer starting from the head
            while new_block.next:
                new_block = new_block.next

            # after we reach the last block in the chain
            new_block.next = Block(timestamp, data, new_block.hash) # adding the new block after the last block of the chain
            new_block.next.hash = new_block.next.calc_hash() # calculating the hash of the added block

    def display_blocks(self):
        # if the chain is empty
        if self.head is None:
            print("You have no Blocks to display\n")
        
        # otherwise we print every block information
        else:
            # creating a pointer to go through our chain to print every block's infos
            current_block = self.head
            while current_block:
                print(f"Timestamp: {current_block.timestamp}")
                print(f"Data: {current_block.data}")
                print(f"Hash: {current_block.hash}")
                print(f"Previous Hash: {current_block.previous_hash}")
                print()
                current_block = current_block.next # moving to the next block

# Test Cases
# Test Case 1: Adding blocks to the blockchain
blockchain = Blockchain()
blockchain.append_block("Transaction Data 1")
blockchain.append_block("Transaction Data 2")
blockchain.append_block("Transaction Data 3")
blockchain.display_blocks()

# Test Case 2: Edge case with an empty blockchain
empty_blockchain = Blockchain()
empty_blockchain.display_blocks()  # Output: No blocks in the blockchain

# Test Case 3: Edge case with a very large blockchain
large_blockchain = Blockchain()
for i in range(100):
    large_blockchain.append_block(f"Transaction Data {i+1}")
large_blockchain.display_blocks()
