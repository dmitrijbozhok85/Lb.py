from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_message(key, iv, message):
    my_cipher = AES.new(key, AES.MODE_OFB, iv)
    padded_message = pad(message, AES.block_size)
    encrypted_msg = my_cipher.encrypt(padded_message)
    return encrypted_msg

def decrypt_message(key, iv, encrypted_msg):
    my_cipher = AES.new(key, AES.MODE_OFB, iv)
    padded_message = my_cipher.decrypt(encrypted_msg)
    original_message = unpad(padded_message, AES.block_size)
    return original_message

my_key = get_random_bytes(16)
my_iv = get_random_bytes(AES.block_size)
my_message = b"This is a test."
print("Original: ", my_message)

my_encrypted_message = encrypt_message(my_key, my_iv, my_message)
print("Encrypted:", my_encrypted_message)

my_decrypted_message = decrypt_message(my_key, my_iv, my_encrypted_message)
print("Decrypted:", my_decrypted_message)
