# Import AES from appropriate libraries
from Crypto.Cipher import AES

# Initial key and plaintext value
key = b'0123456789abcdef'
plaintext = b'This is our plaintext message for IST 402'

# Creates a cipher using CFB thanks to AES library
cipher = AES.new(key, AES.MODE_CFB)
ciphertext = cipher.encrypt(plaintext)
iv = cipher.iv

print('Plaintext: {}'.format(plaintext))
print(f"CFB encrypted: {ciphertext}")
