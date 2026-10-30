
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = input("Enter text to encrypt: ")

data = message.encode()
encrypted_data = cipher.encrypt(data)

print("\nEncrypted Data:")
print(encrypted_data.decode())

decrypted_data = cipher.decrypt(encrypted_data)

print("\nDecrypted Data:")
print(decrypted_data.decode())


# c:\python314\python.exe -m pip install cryptography