from functools import reduce

def hex_to_bytearray(hex_str):
    return bytearray.fromhex(hex_str)

def xor_bytearrays(*args):
    return bytearray([reduce(lambda a, b: a ^ b, byte) for byte in zip(*args)])

ciphered_msg_1 = hex_to_bytearray(input())
ciphered_msg_2 = hex_to_bytearray(input())
ciphered_msg_3 = hex_to_bytearray(input())

decoded_msg = xor_bytearrays(ciphered_msg_1, ciphered_msg_2, ciphered_msg_3)

plaintext = decoded_msg.decode('ascii')

print(plaintext)
