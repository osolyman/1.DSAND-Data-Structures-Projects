import sys
import heapq

class Node:
    # Initializing the node
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left_element = None
        self.right_element = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(data):
    # frequency of each char
    frequency = {}
    for char in data:
        # incrementing the frequency of the char with 1 in case, if it already exists in the dictionery
        # or adding this char and its frequency which is 1 in case, if it doesn't exist in the dictionery
        frequency[char] = frequency.get(char, 0) + 1

    # creating the tree
    heap = [Node(char, freq) for char, freq in frequency.items()] # creating list of nodes

    if len(heap) <= 1:  # checking if there is only one unique character or if the data is empty
        if not heap:
            return "", None  # return empty string and None for an empty string
        else:
            # if there is only one unique character, create a node to represent it in the tree
            root = Node(None, heap[0].freq)
            root.left_element = heap[0]
            return "0" * heap[0].freq, root  # return a string of zeros with the frequency and the root

    heapq.heapify(heap) # the list of nodes is now a min-heap

    while len(heap) > 1:
        # removing the two minimum frequencies from the heap
        left_element = heapq.heappop(heap)
        right_element = heapq.heappop(heap)
        # adding them together
        merged = Node(None, left_element.freq + right_element.freq)
        merged.left_element = left_element
        merged.right_element = right_element
        # reinserting the newly created node int the queue
        heapq.heappush(heap, merged)

    root = heap[0]

    # generating the unique binary code for each char
    codes = {}
    def generating_binaryCodes(node, code = ''):
        if node: # checking if the node exists in the tree or not
            if node.char: # checking if that node is a leaf node
                codes[node.char] = code
            generating_binaryCodes(node.left_element, code + '0')
            generating_binaryCodes(node.right_element, code + '1')

    generating_binaryCodes(root)

    # encoding the input
    encoded_data = ''.join([codes[char] for char in data])

    return encoded_data, root      

def huffman_decoding(data,tree):
    decoded_data = ""
    current_node = tree

    for bit in data: # for every bit in the data
        if bit == '0':
            current_node = current_node.left_element # if bit is 0 we move to the left child
        else:
            current_node = current_node.right_element # if bit is 1 we move to the right child
        
        if current_node.char: # if it is a leaf node
            decoded_data += current_node.char # appending the char of that bit to the created decoded string
            current_node = tree # reset the current node to the root after we reached the leaf node
        
    return decoded_data

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    print("-------------------------------------------------------------------------------------\n")

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
string_1 = "AAAAAAABBBCCCCCCCDDEEEEEE"

if not string_1:
    print("The data is empty.\n")
else:
    print("The size of the data is: {}\n".format(sys.getsizeof(string_1)))
    print("The content of the data is: {}\n".format(string_1))

    encoded_data_1, tree_1 = huffman_encoding(string_1)

    if encoded_data_1:
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data_1, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data_1))

        decoded_data_1 = huffman_decoding(encoded_data_1, tree_1)

        if decoded_data_1:
            print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data_1)))
            print("The content of the decoded data is: {}\n".format(decoded_data_1))
        else:
            print("Can't decode an empty string.\n")
    else:
        print("Encoding is not applicable for an empty string.\n")

print("-------------------------------------------------------------------------------------\n")

## Test Case 2
string_2 = ""

if not string_2:
    print("The data is empty.\n")
else:
    print("The size of the data is: {}\n".format(sys.getsizeof(string_2)))
    print("The content of the data is: {}\n".format(string_2))

    encoded_data_2, tree_2 = huffman_encoding(string_2)

    if encoded_data_2:
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data_2, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data_2))

        decoded_data_2 = huffman_decoding(encoded_data_2, tree_2)

        if decoded_data_2:
            print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data_2)))
            print("The content of the decoded data is: {}\n".format(decoded_data_2))
        else:
            print("Can't decode an empty string.\n")
    else:
        print("Encoding is not applicable for an empty string.\n")

print("-------------------------------------------------------------------------------------\n")

## Test Case 3
string_3 = "AAAAAAAAAAAAAAAA"

if not string_3:
    print("The data is empty.\n")
else:
    print("The size of the data is: {}\n".format(sys.getsizeof(string_3)))
    print("The content of the data is: {}\n".format(string_3))

    encoded_data_3, tree_3 = huffman_encoding(string_3)

    if encoded_data_3:
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data_3, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data_3))

        decoded_data_3 = huffman_decoding(encoded_data_3, tree_3)

        if decoded_data_3:
            print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data_3)))
            print("The content of the decoded data is: {}\n".format(decoded_data_3))
        else:
            print("Can't decode an empty string.\n")
    else:
        print("Encoding is not applicable for an empty string.\n")

print("-------------------------------------------------------------------------------------\n")