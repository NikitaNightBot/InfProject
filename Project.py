import hashlib # * For generating hash
import pyperclip # * For copying encrypted data to clipboard
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes # * To implement AES-256-CBC encryption
# * To generate random key and initialization vector
import string
import random

def main():
    # * Command line interface choose option via ``match: case:`` structure
    
    match int(input("""
[1] Hash
[2] Encryption (AES-256)
                    
[_] Exit
""")):
        case 1:
            match str(input("""
[File] Hash a file (via file path)
[String] Hash a string (text input)
""")).lower():
                case "file":
                    # * User gets to choose from available algorithms, then inputs the file path, hashed contents of the file get copied to clipboard
                    pyperclip.copy(getattr(hashlib, input(f'Choose from available algorithms: {hashlib.algorithms_available}\n'))(
                open(f'{(str(input("Enter file path: ")))}', 'r').read().encode('utf-8')).hexdigest())
                case "string":
                    # * User gets to choose from available algorithms, then inputs the string, hashed string gets copied to clipboard
                    pyperclip.copy(getattr(hashlib, input(f'Choose from available algorithms: {hashlib.algorithms_available}\n'))(
                str(input("Enter string: ")).encode('utf-8')).hexdigest())
            print("Hash succesfully copied to clipboard.")
        case 2:
            # * Generates random key and Initialization Vector for AES-256-CBC (string)
            keytext = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=32))
            ivtext = ''.join(random.choices(string.digits, k=16))

            # * Encodes key and IV for later use

            key = keytext.encode('utf-8')
            iv = ivtext.encode('utf-8')
            

            # * The message its going to encrypt

            bintext = str(input("Plaintext: "))
            
            # * Padding
            
            bintext = bintext + (16 - len(bintext) % 16) * " "
            bintext = bintext.encode('utf-8')

            # * Print text, key, and IV

            print(f"Key: {keytext}")
            print(f"IV: {ivtext}")

            # * Encrypt the bintext with randomly generated key and IV.

            cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            ct = encryptor.update(bintext) + encryptor.finalize()
            decryptor = cipher.decryptor()
            dt = decryptor.update(ct) + decryptor.finalize()

            # * Print encoded text (as hex)
            # ! For some reason matches only 1/2 of what you'd get at https://www.devglan.com/online-tools/aes-encryption-decryption , probally because it counts each character in the key as 8 bits instead of 6.

            print(f"Encrypted text (hex): {ct.hex()}")
            print(f"Selfencrypt -> selfdecrypt text: {dt.decode().rstrip()}") # * .rstrip() to unpad
        case _:
            exit()

if __name__ == '__main__':
    main()
    
