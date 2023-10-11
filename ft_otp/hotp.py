import base64
import hmac

# RFC 6238
# RFC 4226

# retourne les 4 bits de poid faible
# 0b defini une valeur binaire
# On compare avec l'operateur ET les 4 derniers bits de val avec 0b1111 pour obtenir les bits de poid faible
def low_order_4_bits(val):
    return val & 0b1111 # 15 ou 0xf
    
# retourne les 31 derniers bits
# selon le RFC pour avoir 31 bits, le premier octect va etre masquer avec 0x7F et les 3 derniers avec 0xFF(11111111)

def last_31_bits(p):
    res = bytearray()
    res.append(p[0] & 0x7F) # 01111111
    for b in p[1:]:
        res.append(b & 0xFF) # 11111111
    return res
    
# On recoit une chaine de 20 octets (hs)
def dynamic_truncation(hs):
    offset = low_order_4_bits(hs[19])
    p = hs[offset:offset + 4]
    bytes_array = last_31_bits(p)
    # print(bin(int(bytes_array.hex(), 16)))
    return bytes_array

def compute_hotp_value(bytes_array):
    # convert byte array to num
    s_num = int(bytes_array.hex(), 16)
    # generate otp
    otp = s_num % 10 ** 6
    return otp
    
    
def extract_digest(secret, counter):
    counter_bytes = counter.to_bytes(8, byteorder='big')
    hs_mac = hmac.new(secret, counter_bytes, 'sha1')
    digest = hs_mac.digest()
    return digest

# HMAC-based one-time password
def hotp(k, c):
    secret = base64.b32encode(k)
    digest = extract_digest(secret=secret, counter=c)
    bytes_array = dynamic_truncation(hs=digest)
    otp = compute_hotp_value(bytes_array=bytes_array)
    return otp