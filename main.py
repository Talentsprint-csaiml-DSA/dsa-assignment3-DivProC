
import heapq
from collections import defaultdict, Counter

class Hufpoint:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequencies(data):
    freq = Counter(data)
    return freq

def build_tree(frequencies):
    priority_queue = [Hufpoint(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Hufpoint(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    
    return priority_queue[0]

def build_codes(node, code='', codes={}):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = code
    build_codes(node.left, code + '0', codes)
    build_codes(node.right, code + '1', codes)

    return codes

def huffman_coding(data):
    frequencies = calculate_frequencies(data)
    root = build_tree(frequencies)
    codes = build_codes(root)
    
    encoded_data = ''.join(codes[char] for char in data)
    return encoded_data
  
