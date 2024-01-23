def encode(input_string):
    ascii_to_binary = lambda x: '{0:08b}'.format(x)
    triple_bits = lambda x: ''.join([bit*3 for bit in x])
    ascii_values = map(ord, input_string)
    binary_values = map(ascii_to_binary, ascii_values)
    tripled_binary_values = map(triple_bits, binary_values)
    return ''.join(tripled_binary_values)

def decode(input_bits):
    bits_to_ascii = lambda x: chr(int(''.join(['1' if x.count('1') > x.count('0') else '0' for x in [x[i:i+3] for i in range(0, len(x), 3)]]), 2))
    return ''.join(map(bits_to_ascii, [input_bits[i:i+8*3] for i in range(0, len(input_bits), 8*3)]))
