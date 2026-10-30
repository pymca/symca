
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

# Generate RSA keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

# Generate AES key
aes_key = Fernet.generate_key()
cipher = Fernet(aes_key)

# Take message input
message = input("Enter message: ")

# Encrypt message using AES
encrypted_message = cipher.encrypt(message.encode())

# Encrypt AES key using RSA public key
encrypted_aes_key = public_key.encrypt(
    aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

# Decrypt AES key using RSA private key
decrypted_aes_key = private_key.decrypt(
    encrypted_aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

# Decrypt message using recovered AES key
decrypted_message = Fernet(decrypted_aes_key).decrypt(
    encrypted_message
)

print("\nEncrypted AES Key:", encrypted_aes_key.hex()[:50], "...")
print("Encrypted Message:", encrypted_message.decode())
print("Decrypted Message:", decrypted_message.decode())
