"""
Implement the Huffman Encoding Algorithm we went over in class:
Design an algorithm that takes as input a text document or long string. Create the Huffman frequency map, the Huffman tree, transform the input based on the Huffman tree and write out the input text to a file.
You must print out your input set, your frequency map, your tree to the terminal window and write out your compressed file. You must provide screen shots of your code working.
Design an algorithm that takes as input the output of the previous part and reconstructs the document.
You must print out your input set, and write out your reconstructed document to a file. You must provide screen shots of your code working.

You should submit a readme.txt file with an explanation of your code and algorithms. You must provide exact instructions on how to run your code and you must submit screen shots of your running code.

"""
import heapq
from collections import defaultdict, namedtuple
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
def build_huffman_tree(frequency_map):
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency_map.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]  # Root of the Huffman Tree
def build_huffman_codes(node, prefix="", code_map={}):
    if node is not None:
        if node.char is not None:
            code_map[node.char] = prefix
        build_huffman_codes(node.left, prefix + "0", code_map)
        build_huffman_codes(node.right, prefix + "1", code_map)
    return code_map
def huffman_encode(input_text):
    frequency_map = defaultdict(int)
    for char in input_text:
        frequency_map[char] += 1

    huffman_tree_root = build_huffman_tree(frequency_map)
    huffman_codes = build_huffman_codes(huffman_tree_root)
    encoded_text = ''.join(huffman_codes[char] for char in input_text)
    return encoded_text, huffman_codes
def huffman_decode(encoded_text, huffman_codes):
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    current_code = ""
    decoded_text = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""
    return decoded_text
if __name__ == "__main__":
    import sys
    from pathlib import Path
    raw_text = ""
    input_name = "stdin"
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
        input_name = input_path.name
        raw_text = input_path.read_text()
    else:
        raw_text = sys.stdin.read()

    print(f"File Input: {input_name}")
    print("Input Text:", raw_text)

    encoded_text, huffman_codes = huffman_encode(raw_text)
    print("Huffman Codes:", huffman_codes)
    print("Encoded Text:", encoded_text)

    decoded_text = huffman_decode(encoded_text, huffman_codes)
    print("Decoded Text:", decoded_text)