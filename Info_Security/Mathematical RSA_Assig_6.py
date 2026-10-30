
p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = pow(e, -1, phi)

message = int(input("Enter a number less than 3233: "))

ciphertext = pow(message, e, n)
decrypted = pow(ciphertext, d, n)

print("\nPublic Key:", (e, n))
print("Private Key:", (d, n))
print("Encrypted Message:", ciphertext)
print("Decrypted Message:", decrypted)
