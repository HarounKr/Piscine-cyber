from cryptography.fernet import Fernet

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