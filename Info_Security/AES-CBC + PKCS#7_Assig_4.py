
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

message = input("Enter message: ")

key = os.urandom(32)
iv = os.urandom(16)

padder = padding.PKCS7(128).padder()
padded_data = padder.update(message.encode()) + padder.finalize()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()

ciphertext = encryptor.update(padded_data) + encryptor.finalize()

print("\nEncrypted Data:")
print(ciphertext.hex())

cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
decryptor = cipher.decryptor()

decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

unpadder = padding.PKCS7(128).unpadder()
decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()

print("\nDecrypted Data:")
print(decrypted_data.decode())
