import secrets
import argparse
import random
import time
import datetime
import base64
import pyotp
from cryptography.fernet import Fernet
from hotp import hotp
from encryption import encrypt_data, decrypt_data


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

def is_hex(s):
    try:
        int(s, 16)
        return True
    except Exception:
        return False
    
def handle_errors(hexkey) -> int:
     # Gestion des erreurs
    if is_hex(hexkey) == False:
        print("error: key must be hexadecimal.")
        return False
    elif len(hexkey) < 64:
        print(": error: key must be at least 64 hexadecimal characters.")
        return False
    return True

# TOTP = HOTP(K, C)
# Mot de passe à usage unique basé sur le temps
def totp(k, t):
    s_since_epock = time.mktime(datetime.datetime.now().timetuple())
    time_steps = int(s_since_epock / t)
    totp = hotp(k=k, c=time_steps)
    return totp


def main():
    args = args_parser()

    try:
        if (args.hexadecimal): # -hex
            # Generer une clé en hexa
            hexkey = generate_random_hexa()
            print("hexkey")
        elif (args.encryptionkey): # -ek
            # Generer une clé de chiffrement
            key = Fernet.generate_key()
            print("Encryption key: ", key.decode())
        elif (args.hexkey): # -g
            if handle_errors(args.hexkey):
                key = input("Please enter an encryption key: ")
                with open("ft_otp.key", 'wb') as hexfile:
                    hexfile.write(args.hexkey.encode())
                    hexfile.close()
                encrypt_data(encryptionkey=key)
        elif (args.passfile): # -k
            key = input("Please enter an decryption key: ")
            hexkey = decrypt_data(decryptionkey=key, filename=args.passfile)
            t = 30 # secondes
            totp_val = totp(k=hexkey, t=t)
            secret = base64.b32encode(hexkey)
            real_totp = pyotp.TOTP(base64.b32encode(secret))
            print("my otp   :", totp_val)
            print("real otp :", real_totp.now())
    except Exception as e:
        print(e)
    
    return 0

if __name__ == "__main__":
    main()