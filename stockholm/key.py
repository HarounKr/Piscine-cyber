from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open('key.key', mode='wb') as file:
    file.write(key)