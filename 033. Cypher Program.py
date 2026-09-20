# Cypher Program

import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# ENCRYPT

plain_text = input("Enter the Text to Encrypt :")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original Text :{plain_text}")
print(f"Cipher Text :{cipher_text}")

# DECRYPT

cipher_text = input("Enter the Text to Decrypt:")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted Text :{cipher_text}")
print(f"Original Text :{plain_text}")