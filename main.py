import heapq
from collections import Counter, defaultdict

def calculate_frequencies(data):
    return Counter(data)


def build_huffman_tree(frequencies):
    heap = [[freq, [char, ""]] for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def generate_huffman_codes(huffman_tree):
    return {char: code for char, code in huffman_tree}

def huffman_coding(data):
    frequencies = calculate_frequencies(data)
    huffman_tree = build_huffman_tree(frequencies)
    codes = generate_huffman_codes(huffman_tree)
    encoded_data = ''.join(codes[char] for char in data)
    return encoded_data
