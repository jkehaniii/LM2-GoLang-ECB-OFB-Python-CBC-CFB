# Import AES from appropriate libraries
from Crypto.Cipher import AES

value = input("Enter a plaintext value: ")

# Initial key and plaintext value
key = b'0123456789abcdef'
plaintext = value

# Creates a cipher using CFB thanks to AES library
cipher = AES.new(key, AES.MODE_CFB)
ciphertext = cipher.encrypt(plaintext)
iv = cipher.iv

print(f"CFB encrypted: {ciphertext}")
