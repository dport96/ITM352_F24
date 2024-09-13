import cryptography
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt a string password
plaintext = input("Enter a message: ").encode()
ciphertext = cipher.encrypt(plaintext)

# Decrypt the string
decrypted_text = cipher.decrypt(ciphertext)

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted_text.decode()}")