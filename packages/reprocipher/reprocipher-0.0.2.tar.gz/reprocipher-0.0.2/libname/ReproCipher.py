import random
import string

# Set a fixed seed for reproducibility
random.seed(42)

def substitution_cipher(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = 97 if char.islower() else 65
            encrypted_text += chr((ord(char) + key - base) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def random_cipher_key():
    key = random.randint(-26, 26)
    return random_cipher_key() if key == 0 else key

def random_text():
    key = random.randint(0, 6)
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=key)), key

def encrypt(text, key, random_text1, random_text2, key1, key2, length):
    divide = random.randint(0, length - 1)
    encrypt_text = ''
    for i, char in enumerate(text):
        if i == divide:
            encrypt_text += char + random_text1
            continue
        encrypt_text += char
    return encrypt_text + random_text2 + str(key) + str(key1) + str(key2) + str(length)

def main(text):
    key = random_cipher_key()
    cipher_text = substitution_cipher(text, key)
    length = len(cipher_text)
    random_text1, key1 = random_text()
    random_text2, key2 = random_text()
    return (encrypt(cipher_text, key, random_text1, random_text2, key1, key2, length))

if __name__ == "__main__":
    print("This algorythm developed by Ravindu Priyankara")