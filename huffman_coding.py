import heapq

#Node Class
class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


    def __lt__(self, other):
        return self.freq < other.freq

#Hoffman code outside of a class:
"""
def string_to_frequency_dict(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def build_huffman_tree(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def huffman_codes(node, code = "", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = code
        huffman_codes(node.left, code + "0", codebook)
        huffman_codes(node.right, code + "1", codebook)
    return codebook

def encode_string(s, codes):
    encoded = ""
    for char in s:
        encoded += codes[char]
    return encoded

def huffman_coding(s):
    frequency = string_to_frequency_dict(s)
    root = build_huffman_tree(frequency)
    codes = huffman_codes(root)
    print("Huffman Codes:", codes)
    return encode_string(s, codes)

def decode_string(encoded, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded = ""
    current_code = ""
    for bit in encoded:
        current_code += bit
        if current_code in reverse_codes:
            decoded += reverse_codes[current_code]
            current_code = ""
    return decoded

print(huffman_coding("hello world"))
print(decode_string("11100001010110111101111001010001", huffman_codes(build_huffman_tree(string_to_frequency_dict("hello world")))))"""

class HuffmanString:
    def __init__(self, string):
        self.string = string
        self.frequency = self.string_to_frequency_dict()
        self.root = self.build_huffman_tree()
        self.codes = self.huffman_codes()
        self.encoded_string = self.encode_string()

    def string_to_frequency_dict(self):
        frequency = {}
        for char in self.string:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        return frequency

    def build_huffman_tree(self):
        heap = [Node(char, freq) for char, freq in self.frequency.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)

        return heap[0]

    def huffman_codes(self, node=None, code="", codebook={}):
        if node is None:
            node = self.root
        if node.char is not None:
            codebook[node.char] = code
        else:
            self.huffman_codes(node.left, code + "0", codebook)
            self.huffman_codes(node.right, code + "1", codebook)
        return codebook

    def encode_string(self):
        encoded = ""
        for char in self.string:
            encoded += self.codes[char]
        return encoded

    def __str__(self):
        return self.encoded_string

def decode_string(encoded, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded = ""
    current_code = ""
    for bit in encoded:
        current_code += bit
        if current_code in reverse_codes:
            decoded += reverse_codes[current_code]
            current_code = ""
    return decoded

taran_huffman_str = HuffmanString("Taran the goat")
print("Huffman Codes:", taran_huffman_str.codes)
print("Encoded String:", taran_huffman_str)
print("Decoded String:", decode_string(taran_huffman_str.encoded_string, taran_huffman_str.codes))

