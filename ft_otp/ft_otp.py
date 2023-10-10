import secrets
import argparse
import random
import sys
from cryptography.fernet import Fernet
import string
import re

def args_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-hex", "--hexadecimal", help="Generate hexadecimal key for at least 64 characters", action="store_true")
    parser.add_argument("-g", "--hexkey", help="Store hexa key safely in an encrypted file called ft_otp.key", type=str)
    parser.add_argument("-k", "--passfile", help="The program generates a new temporary password based on the key given as argument and prints it on the standard output", type=str)
    parser.add_argument("-ek", "--encryptionkey", help="Generate key to encrypte hexadecimal file", action='store_true')

    args = parser.parse_args()
    return args

def generate_random_hexa() -> str:
    nbytes = random.randint(32, 82)
    hexkey = secrets.token_hex(nbytes=nbytes)
    return hexkey

def encrypt_data(encryptionkey: str) -> None:
    key = str.encode(encryptionkey)
    fernet = Fernet(key)
    # Ouvrir et lire le fichier a chiffrer
    with open('ft_otp.key', 'rb') as file:
        hexfile = file.read()
    # Chiffrer le contenu du fichier 
    encrypted_data = fernet.encrypt(hexfile)
    # revouvrir le fichier a chiffrer et ecrire le contenu chiffrer a l'interieur
    with open('ft_otp.key', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_data(decryptionkey: str, filename: str) -> bytes:
    key = str.encode(decryptionkey)

    # Utiliser la cle de chiffrement
    fernet = Fernet(key)
    # Ouvrir le fichier chiffrer
    with open(filename, 'rb') as enc_file:
        encyrpted = enc_file.read()
    # Dechiffrer le fichier
    decrypted = fernet.decrypt(encyrpted)
    return decrypted

def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False
    
def handle_errors(hexkey) -> int:
    if is_hex(hexkey) == False:
        print("error: key must be hexadecimal.")
        return False
    elif len(hexkey) < 64:
        print(": error: key must be at least 64 hexadecimal characters.")
        return False
    return True

def main():
    args = args_parser()

    try:
        if (args.hexadecimal):
            # Generer une clé en hexa
            hexkey = generate_random_hexa()
            print("Hex key generated: ", hexkey)
        elif (args.encryptionkey):
            key = Fernet.generate_key()
            print("Encryption key: ", key.decode())
        elif (args.hexkey):
            # Gestion des erreurs
            if handle_errors(args.hexkey):
                key = input("Please enter an encryption key: ")
                with open("ft_otp.key", 'wb') as hexfile:
                    hexfile.write(args.hexkey.encode())
                    hexfile.close()
                encrypt_data(encryptionkey=key)
        elif (args.passfile):
            key = input("Please enter an decryption key: ")
            hexkey = decrypt_data(decryptionkey=key, filename=args.passfile)
            print(hexkey)
    except Exception as e:
        print(e)
    
    return 0

if __name__ == "__main__":
    main()