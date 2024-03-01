import hashlib
from Crypto.PublicKey import RSA
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import uuid
from datetime import datetime
import random
def sha256(data):
    return hashlib.sha256(str(data).encode('utf-8')).hexdigest()

def generate_private_key():
    key = RSA.generate(2048)
    return key.export_key()

def generate_public_key(private_key, access_key):
    return sha256(str(private_key) + str(access_key))

def sha512(data):
    return hashlib.sha512(str(data).encode('utf-8')).hexdigest()

def gen_access_key(private_key):
    return sha512(base85_gen(
        str(sha256(
            str(uuid.uuid4().bytes)
            + str(get_random_bytes(random.randint(1, 1000)))
            + str(datetime.now().timestamp())
        ))
        + str(private_key)
    ))





def check_access_key(access_key, public_key, private_key):
    if generate_public_key(private_key, access_key) == public_key:
        return True
    else:
        return False



def base85_gen(data): 
    return base64.b85encode(str(data).encode('utf-8')).decode('utf-8')

def aes_128_gen(data):
    key = get_random_bytes(16)  # Generate a 128-bit key
    cipher = AES.new(key, AES.MODE_CBC)
    combined_data_bytes = str(data).encode('utf-8')
    ciphertext, tag = cipher.encrypt_and_digest(combined_data_bytes)
    return key, ciphertext, tag