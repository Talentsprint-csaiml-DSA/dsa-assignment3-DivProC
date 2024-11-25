import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequencies(data):
    return Counter(data)

def build_huffman_tree(frequencies):
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def generate_huffman_codes(node, prefix='', codes=None):
    if codes is None:
        codes = {}

    if node.char is not None:
        codes[node.char] = prefix
    else:
        generate_huffman_codes(node.left, prefix + '0', codes)
        generate_huffman_codes(node.right, prefix + '1', codes)

    return codes

def huffman_encode(data):
    frequencies = calculate_frequencies(data)
    root = build_huffman_tree(frequencies)
    codes = generate_huffman_codes(root)
    encoded_data = ''.join(codes[char] for char in data)
    return encoded_data, codes
def huffman_coding(data):
    return huffman_encode(data)[0]

