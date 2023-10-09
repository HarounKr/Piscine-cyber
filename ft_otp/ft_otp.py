import secrets
import argparse
import random
from cryptography.fernet import Fernet

def args_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-hex", "--hexfile",help="Generate hexadecimal key for at least 64 characters", type=str)
    parser.add_argument("-g", "--otpfile", help="Store hexa key safely in an encrypted file called ft_otp.key", type=str)
    parser.add_argument("-k", "--passfile", help="The program generates a new temporary password based on the key given as argument and prints it on the standard output", type=str)

    args = parser.parse_args()
    return args

def generate_random_hexa() -> str:
    nbytes = random.randint(32, 82)
    hex = secrets.token_hex(nbytes=nbytes)
    return hex

def encrypt_hex_file(hexkey):
    key = Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

def main():

    args = args_parser()
    try:
        if (args.hexfile):
            hex = generate_random_hexa()
            with open(args.hexfile, 'w') as file:
                file.write(hex)
                file.close()
            # save_hex_key(hexkey=hex)
    except Exception as e:
        print(e)
    return 0
    

if __name__ == "__main__":
    main()